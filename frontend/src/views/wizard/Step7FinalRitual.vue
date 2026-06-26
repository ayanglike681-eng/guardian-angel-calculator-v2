<template>
  <div class="animate-fade-in h-[80vh] overflow-y-auto custom-scrollbar p-4 md:p-10 bg-white rounded-3xl shadow-sm border border-gray-100">
    <div class="text-center space-y-4 border-b border-gray-100 pb-8 mb-8">
      <h2 class="text-xs font-bold tracking-[0.4em] text-primary uppercase">The Final Rite</h2>
      <h1 class="text-3xl md:text-5xl font-serif text-primary">守护天使召唤仪式</h1>
      <p class="text-sm text-secondary font-serif italic">
        "这是最后的环节，也是最重要的环节。面向东方，开始你的呼唤。"
      </p>
    </div>

    <div class="max-w-3xl mx-auto space-y-10 font-serif leading-relaxed text-gray-800 text-justify">
      <div class="bg-gray-50 p-6 rounded-xl border-l-4 border-gray-200">
        <p class="italic">
          "那不可理解的神，那头戴面纱的神；那施行公义的神，那永恒不灭的神。他的名字是应当被称颂的，正因他是七大天堂的王，而在他的宫殿与大地之间，是闪烁着的伟大造物们。"
        </p>
      </div>

      <div class="space-y-4">
        <p>
          "我召唤你，伟大的，纯洁的灵体啊，我奉那口衔公义之剑者，赐人智慧者召唤你：
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-2 pl-4 border-l border-gray-200 text-sm bg-[#FFFCF9] p-4 rounded">
          <div v-for="planet in planetOptions" :key="planet" class="flex justify-between items-center">
            <span class="text-gray-500">在{{ planet }}间，我召唤你：</span>
            <div class="text-right">
              <span class="font-bold text-primary block">{{ result.planetaryGuardians[planet].hebrew }}</span>
              <span class="text-xs text-gray-400">{{ result.planetaryGuardians[planet].latin }}</span>
            </div>
          </div>
        </div>
        <p>
          "我用七种方言召唤你的名字，并召唤你的根本之名 <strong class="text-primary text-lg mx-1">{{ result.hebrewName }}</strong>
          <span class="text-sm text-gray-400">({{ result.hebrewTransliteration }})</span>，
          提升我的灵魂，令我的思想与精神向上，令我能够感知到神圣的天使的存在。"
        </p>
      </div>

      <div>
        <div class="text-center mb-8">
          <h3 class="font-bold text-2xl text-primary mb-1">听啊，{{ result.hebrewName }}</h3>
          <p class="text-sm text-primary font-mono tracking-widest uppercase opacity-80">({{ result.hebrewTransliteration }})</p>
          <p class="text-sm text-gray-400 mt-2 italic">"我呼唤你强大的诸名！"</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 text-xs font-mono text-gray-600 bg-gray-50 p-4 rounded-xl">
          <div v-for="(item, idx) in result.powerNames" :key="idx" class="p-3 bg-white border border-slate-100 rounded-lg shadow-sm hover:border-gray-200 transition-all flex flex-col gap-1">
            <div class="flex items-center gap-2 border-b border-gray-50 pb-1 mb-1">
              <span class="text-[10px] text-gray-300 font-bold">{{ idx + 1 }}.</span>
              <span class="font-bold text-primary text-sm ml-auto">{{ item.hebrew }}</span>
            </div>
            <div class="text-[10px] text-gray-400 tracking-tighter truncate italic ml-auto">{{ item.latin }}</div>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <p class="font-bold text-red-800 text-sm text-center bg-red-50 p-2 rounded">
          * 向东方展示你的戒指，并如此宣言 *
        </p>
        <div class="text-center">
          <p class="text-2xl font-sans text-primary mb-2">Aneh Li Malach {{ result.latinResult }}!</p>
          <p class="text-sm text-gray-500">（回应我的呼唤，{{ result.latinResult }}!） <span class="px-2 py-0.5 bg-slate-200 rounded text-xs font-bold">X3</span></p>
        </div>

        <div class="bg-white border border-dashed border-gray-200 p-6 rounded-xl space-y-3 text-sm relative overflow-hidden">
          <div class="absolute top-0 right-0 p-2 opacity-10 text-6xl">&cross;</div>
          <p>你是 <strong class="text-primary">Qadosh</strong> <span class="text-xs text-gray-400">（向东画一个十字）</span></p>
          <p>你是 <strong class="text-primary">Elohi</strong> <span class="text-xs text-gray-400">（向南画一个十字）</span></p>
          <p>你是 <strong class="text-primary">Ha-Malachim</strong> <span class="text-xs text-gray-400">（向西画一个十字）</span></p>

          <div class="pt-4 border-t border-dashed border-gray-200/30">
            <label class="block text-xs font-bold text-primary uppercase mb-2">选择你的命主星 (Ascendant Ruler):</label>
            <div class="flex gap-2 overflow-x-auto pb-2 custom-scrollbar">
              <button
                v-for="p in planetOptions" :key="p"
                @click="rulingPlanet = p"
                :class="['px-3 py-1 rounded text-xs whitespace-nowrap transition-colors', rulingPlanet === p ? 'bg-primary text-white font-bold' : 'bg-slate-100 text-gray-500 hover:bg-slate-200']"
              >{{ p }}</button>
            </div>
            <p class="mt-3 leading-loose">
              "你是星星自身，是我在地上的记录者，在 <strong class="text-primary underline decoration-cta decoration-2 underline-offset-4">{{ rulingPlanet }}</strong> 的领域中，你被称作
              <strong class="text-primary text-lg mx-1">{{ result.planetaryGuardians[rulingPlanet].hebrew }}</strong>
              <span class="text-xs text-gray-400">（向北画一个十字）</span>。"
            </p>
          </div>
        </div>
      </div>

      <div class="space-y-4">
        <p>
          "你即是我，<strong class="text-primary">{{ result.hebrewName }}</strong> <span class="text-sm text-gray-400">({{ result.hebrewTransliteration }})</span>。前来吧，今晚就立刻前来。令我们之间的约显现，属灵的天使啊。
          我以知性的人的名义向你们宣告，我以刻在天堂大门上的名字向你们宣告，我以先知们陈述的话语向你们宣告："
        </p>
        <div class="bg-gray-800 text-gray-300 p-5 rounded-lg text-xs md:text-sm font-mono leading-loose shadow-inner">
          Dahaviel [X7] &middot; Qashriel [X7] &middot; Gahuriel [X7] &middot; Zakutiel [X7] &middot; Tophchiel [X7] &middot; Dahariel [X7] &middot; Matqiel [X7] &middot; Shauiel [X7]
        </div>
        <p class="text-center font-bold text-primary pt-4">
          "来吧，你们这些侍奉在 Hechal 前的天使们，凭你们立的约把门打开吧。愿神的祝福临到你们的头上，使你们接近更高的天堂。Amen。"
        </p>
      </div>

      <div class="border-t-2 border-gray-100 pt-8 mt-12 text-center">
        <h4 class="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4">Meditation Count Calculation</h4>
        <div class="inline-block bg-amber-50 border border-amber-100 p-6 rounded-2xl">
          <p class="text-sm text-amber-800 mb-2">你的守护天使数值：<strong>{{ result.totalValue }}</strong></p>
          <div class="text-3xl font-sans font-bold text-primary mb-2">
            {{ meditationCount }} <span class="text-sm font-sans text-gray-400 font-normal">遍</span>
          </div>
          <p class="text-xs text-gray-500 max-w-xs mx-auto">
            * 计算法则：各位数相乘 ({{ result.totalValue.toString().split('').filter(n => n !== '0').join(' × ') }})
          </p>
        </div>
        <div class="mt-8">
          <button @click="$emit('restart')" class="px-8 py-3 rounded-full border border-gray-300 text-gray-500 hover:bg-gray-50 hover:text-gray-800 transition-colors text-xs uppercase tracking-widest font-bold">
            完成仪式 &middot; Close Ritual
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({ result: { type: Object, required: true } })
defineEmits(['restart'])

const rulingPlanet = ref("太阳")
const planetOptions = ["月亮", "水星", "金星", "太阳", "火星", "木星", "土星"]

const meditationCount = computed(() => {
  return props.result.totalValue.toString().split('')
    .map(Number)
    .filter(n => n !== 0)
    .reduce((a, b) => a * b, 1)
})
</script>
