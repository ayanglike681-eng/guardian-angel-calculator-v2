import math
import logging
from typing import Optional
from pypinyin import pinyin, Style
from app.data import (
    HEBREW_ALPHABET, LETTER_VALUES, HEBREW_MAP, ORDINAL_TO_VALUE,
    PLANETARY_ROWS, PLANET_ORDER, VALUE_TABLE, HEBREW_VALUE_TABLE,
    SOLAR_TEMPLATE
)

logger = logging.getLogger(__name__)


def hebrew_component_sum(hebrew_text: str, start_row: int = 1) -> int:
    total = 0
    for i, char in enumerate(hebrew_text):
        row = ((i + start_row - 1) % 64) + 1
        if row in HEBREW_VALUE_TABLE and char in HEBREW_VALUE_TABLE[row]:
            total += HEBREW_VALUE_TABLE[row][char]
        else:
            idx = HEBREW_ALPHABET.index(char) if char in HEBREW_ALPHABET else -1
            if idx != -1:
                total += LETTER_VALUES[idx]
    return total


def number_to_words(num: int) -> str:
    if num == 0:
        return "zero"
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion"]

    def convert_below_thousand(n: int) -> str:
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
        else:
            return ones[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + convert_below_thousand(n % 100))

    result = ""
    thousand_index = 0
    while num > 0:
        if num % 1000 != 0:
            segment = convert_below_thousand(num % 1000)
            if thousand_index > 0:
                segment += " " + thousands[thousand_index]
            if result:
                result = segment + " " + result
            else:
                result = segment
        num //= 1000
        thousand_index += 1
    return result.strip()


def extract_numbers_from_words(words: str) -> list:
    word_to_num = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    tokens = words.replace("-", " ").replace(" and ", " ").lower().split()
    numbers = []
    current_num = 0
    for word in tokens:
        if word in word_to_num:
            current_num += word_to_num[word]
        elif word == "hundred":
            current_num *= 100
        elif word == "thousand":
            current_num *= 1000
            numbers.append(current_num)
            current_num = 0
        elif word == "million":
            current_num *= 1000000
            numbers.append(current_num)
            current_num = 0
    if current_num > 0:
        numbers.append(current_num)
    return numbers


def decompose_number(num: int) -> list:
    if num == 0:
        return [0]
    str_num = str(num)
    length = len(str_num)
    components = []
    for i in range(length):
        digit = str_num[i]
        if digit != '0':
            position_value = int(digit) * (10 ** (length - i - 1))
            components.append(position_value)
    return components


def convert_to_hebrew_numbers(components: list) -> list:
    hebrew_nums = []
    for num in components:
        if num in [500, 600, 700, 800, 900]:
            hebrew_nums.append(num // 100)
        elif num >= 1000:
            hebrew_nums.append(num // 1000)
        elif num in [100, 200, 300, 400]:
            hebrew_nums.append(num)
        elif 20 <= num <= 90 and num % 10 == 0:
            hebrew_nums.append(num)
        elif 10 <= num <= 19:
            hebrew_nums.append(10)
            if num > 10:
                hebrew_nums.append(num - 10)
        elif 1 <= num <= 9:
            hebrew_nums.append(num)
    return hebrew_nums


def shift_letter(letter: str, steps: int = 1, forward: bool = True) -> str:
    if letter not in HEBREW_ALPHABET:
        return letter
    idx = HEBREW_ALPHABET.index(letter)
    if forward:
        new_idx = (idx - steps) % len(HEBREW_ALPHABET)
    else:
        new_idx = (idx + steps) % len(HEBREW_ALPHABET)
    return HEBREW_ALPHABET[new_idx]


def shift_text(text: str, steps: int = 1, forward: bool = True) -> str:
    return ''.join(shift_letter(ch, steps, forward) for ch in text)


def transliterate(text: str) -> str:
    mapping = {
        'א': 'A', 'ב': 'B', 'ג': 'G', 'ד': 'D', 'ה': 'H',
        'ו': 'V', 'ז': 'Z', 'ח': 'Ch', 'ט': 'T', 'י': 'Y',
        'כ': 'K', 'ל': 'L', 'מ': 'M', 'נ': 'N', 'ס': 'S',
        'ע': 'O', 'פ': 'P', 'צ': 'Ts', 'ק': 'Q', 'ר': 'R',
        'ש': 'Sh', 'ת': 'Th'
    }
    return ''.join(mapping.get(ch, ch) for ch in text)


def calculate_name_value(name: str) -> dict:
    clean_name = name.upper()
    clean_name = ''.join(clean_name.split())  # strip all whitespace (match JS /\s/g)
    total = 0
    details = []
    for i, char in enumerate(clean_name):
        pos = i + 1
        lookup_pos = ((pos - 1) % 64) + 1 if pos > 64 else pos
        key = f"{lookup_pos}-{char}"
        value = VALUE_TABLE.get(key, 0)
        total += value
        details.append({"letter": char, "value": value})
    return {"total": total, "details": details}


def digit_sum(num: int) -> int:
    return sum(int(d) for d in str(abs(num)))


def wrap22(num: int) -> int:
    if num == 0:
        return 22
    result = num
    while result > 22:
        result -= 22
    return result


def ordinal_to_hebrew_letter(ordinal: int) -> str:
    ord22 = wrap22(ordinal)
    value = ORDINAL_TO_VALUE[ord22]
    return HEBREW_MAP[value]


def calculate_tetragrammaton(total_value: int, final_hebrew_name: str) -> dict:
    big_adam = digit_sum(total_value)
    adam_spirit = digit_sum(big_adam)
    adam_flesh = big_adam
    eve_flesh = adam_spirit + adam_flesh
    eve_spirit = digit_sum(eve_flesh)
    union = big_adam + adam_spirit + eve_flesh + eve_spirit
    merged_spirits = adam_spirit * eve_spirit
    big_eve_raw = abs(union - merged_spirits)
    big_eve = wrap22(big_eve_raw)

    suffix = 'אל'
    main_name = final_hebrew_name
    if final_hebrew_name.endswith(suffix):
        main_name = final_hebrew_name[:-len(suffix)]

    front_sum = hebrew_component_sum(main_name, 1)
    back_sum = hebrew_component_sum(suffix, len(main_name) + 1)
    front_digit = digit_sum(front_sum)
    back_digit = digit_sum(back_sum)

    small_adam_flesh = digit_sum(front_digit + back_digit)
    small_adam_spirit = digit_sum(small_adam_flesh)
    small_adam = wrap22(small_adam_flesh)

    small_eve_flesh = small_adam + small_adam_spirit
    small_eve_spirit = digit_sum(small_eve_flesh)
    small_union = small_adam + small_adam_spirit + small_eve_flesh + small_eve_spirit
    small_merged = small_adam_spirit * small_eve_spirit
    small_eve_raw = abs(small_merged - small_union)
    small_eve = wrap22(small_eve_raw)

    ordinals = [big_adam, big_eve, small_adam, small_eve]
    letters = ''.join(ordinal_to_hebrew_letter(o) for o in ordinals)

    return {"ordinals": ordinals, "letters": letters}


def calculate_tetragram(input_name: str) -> dict:
    name_result = calculate_name_value(input_name)
    total = name_result["total"]
    _, final_result, _ = _build_hebrew_name(total)
    return calculate_tetragrammaton(total, final_result)


def _build_hebrew_name(total: int) -> tuple[str, str, str]:
    """Build hebrew angel name from total value.
    Returns (hebrew_letters_without_el, full_hebrew_name, latin_transliteration).
    """
    adjusted_value = total - 31
    words = number_to_words(abs(adjusted_value))
    extracted_nums = extract_numbers_from_words(words)
    all_components = []
    for n in extracted_nums:
        all_components.extend(decompose_number(n))

    if len(all_components) > 0 and 10000 <= all_components[0] < 100000:
        has_thousands = any(1000 <= c <= 9000 for c in all_components[1:])
        if has_thousands:
            all_components[0] = all_components[0] // 1000
        else:
            first = all_components[0] // 1000
            all_components = [first, 1000] + all_components[1:]

    hebrew_nums = convert_to_hebrew_numbers(all_components)
    hebrew_letters_list = []
    for n in hebrew_nums:
        letter = HEBREW_MAP.get(n)
        if letter is None:
            letter = HEBREW_MAP.get(n * 10, '')
        hebrew_letters_list.append(letter)
    hebrew_letters = ''.join(hebrew_letters_list)
    full_name = hebrew_letters + 'אל'
    latin = transliterate(full_name)
    return hebrew_letters, full_name, latin


def calculate_origin(input_name: str) -> dict:
    name_result = calculate_name_value(input_name)
    total = name_result["total"]
    adjusted_value = total - 31
    return {
        "原始数值": total,
        "调整后数值": adjusted_value,
        "希伯来字母数": len(str(adjusted_value)),
        "守护天使等级": math.ceil(adjusted_value / 100),
        "神圣数字": digit_sum(adjusted_value)
    }


def process_angel_data(input_name: str) -> Optional[dict]:
    if not input_name or not input_name.strip():
        return None

    try:
        name_result = calculate_name_value(input_name)
        total = name_result["total"]
        details = name_result["details"]
        origin_data = calculate_origin(input_name)

        hebrew_letters, final_result, latin_result = _build_hebrew_name(total)
        adjusted_value = total - 31

        tetragram = calculate_tetragram(input_name)

        power_names = []
        current_text = final_result
        for i in range(22):
            power_names.append({
                "id": i + 1,
                "hebrew": current_text,
                "latin": transliterate(current_text)
            })
            current_text = shift_text(current_text, 1, True)

        planetary_guardians = {}
        spirit_row = PLANETARY_ROWS["善灵之字"]
        name_prefix = final_result[:-2]  # remove 'אל'
        name_suffix = 'אל'

        for planet in PLANET_ORDER:
            converted_prefix = ""
            planet_row = PLANETARY_ROWS[planet]
            for char in name_prefix:
                idx = spirit_row.index(char) if char in spirit_row else -1
                if idx != -1:
                    converted_prefix += planet_row[idx]
                else:
                    converted_prefix += char
            hebrew_name = converted_prefix + name_suffix
            planetary_guardians[planet] = {
                "hebrew": hebrew_name,
                "latin": transliterate(hebrew_name)
            }

        return {
            "totalValue": total,
            "adjustedValue": adjusted_value,
            "hebrewLetters": hebrew_letters,
            "latinResult": latin_result,
            "hebrewTransliteration": latin_result,
            "powerNames": power_names,
            "details": details,
            "tetragram": tetragram,
            "originData": origin_data,
            "originalName": input_name,
            "hebrewName": final_result,
            "planetaryGuardians": planetary_guardians
        }
    except Exception as e:
        logger.error(f"Angel data processing error: {e}", exc_info=True)
        return None


def calculate_handle(num: int) -> int:
    n = abs(num)
    while n > 9:
        n = sum(int(d) for d in str(n))
    return 1 if n == 0 else n


def generate_angel_square(target_num: int) -> Optional[dict]:
    if not target_num:
        return None

    N = 6
    total_cells = 36
    handle = calculate_handle(target_num)

    door = (total_cells - 1) * handle
    raw_key = ((2 * target_num / N) - door) / 2
    key = int(math.floor(raw_key))

    sequence = [key + (i * handle) for i in range(total_cells)]

    current_sum = (6 * key) + (105 * handle)
    remainder = target_num - current_sum

    grid = [[0] * 6 for _ in range(6)]
    for row in range(6):
        for col in range(6):
            sequence_index = SOLAR_TEMPLATE[row][col] - 1
            grid[row][col] = sequence[sequence_index]

    if remainder != 0:
        for i in range(6):
            grid[i][i] += remainder

    return {
        "grid": grid,
        "handle": handle,
        "key": key,
        "door": door,
        "remainder": remainder,
        "lock": key + (35 * handle)
    }


def chinese_to_pinyin(text: str) -> str:
    """'张三丰' -> 'zhangsanfeng'"""
    return ''.join(item[0] for item in pinyin(text, style=Style.NORMAL))


def process_chinese_angel_data(gender: str, own_name: str, parent1_name: str,
                                parent2_name: str, surname: str) -> Optional[dict]:
    """Process Chinese name through pinyin conversion then gematria calculation.

    Naming rules:
      - male:   own + parent1(mother) + parent2(father) + surname
      - female: own + parent1(father) + parent2(mother) + surname
    """
    own_pinyin = chinese_to_pinyin(own_name)
    parent1_pinyin = chinese_to_pinyin(parent1_name)
    parent2_pinyin = chinese_to_pinyin(parent2_name)
    surname_pinyin = chinese_to_pinyin(surname)

    # Frontend ensures parent1/parent2 are in correct order based on gender:
    #   male:   parent1=mother, parent2=father  → own + mother + father + surname
    #   female: parent1=father, parent2=mother  → own + father + mother + surname
    full_name = own_pinyin + parent1_pinyin + parent2_pinyin + surname_pinyin

    return process_angel_data(full_name)
