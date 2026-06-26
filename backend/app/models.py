from pydantic import BaseModel


class CalculateRequest(BaseModel):
    name: str


class CalculateChineseRequest(BaseModel):
    gender: str  # "male" or "female"
    ownName: str
    parent1Name: str
    parent2Name: str
    surname: str


class LetterDetail(BaseModel):
    letter: str
    value: int


class TetragramResult(BaseModel):
    ordinals: list[int]
    letters: str


class PowerName(BaseModel):
    id: int
    hebrew: str
    latin: str


class PlanetaryName(BaseModel):
    hebrew: str
    latin: str


class OriginData(BaseModel):
    原始数值: int
    调整后数值: int
    希伯来字母数: int
    守护天使等级: int
    神圣数字: int


class CalculateResponse(BaseModel):
    originalName: str
    totalValue: int
    adjustedValue: int
    hebrewLetters: str
    hebrewName: str
    latinResult: str
    hebrewTransliteration: str
    details: list[LetterDetail]
    tetragram: TetragramResult
    powerNames: list[PowerName]
    planetaryGuardians: dict[str, PlanetaryName]
    originData: OriginData
