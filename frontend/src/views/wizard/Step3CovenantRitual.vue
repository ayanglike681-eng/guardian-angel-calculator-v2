<template>
  <div class="max-w-5xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Guardian of the Sphere</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">行星层级契约</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
    </div>

    <!-- Planet selector — grid on desktop, scroll on mobile -->
    <div class="flex gap-3 overflow-x-auto pb-4 px-2 justify-start md:justify-center custom-scrollbar mb-4">
      <button
        v-for="(planet, i) in planets"
        :key="planet"
        @click="activePlanet = planet"
        :class="['flex flex-col items-center justify-center w-[72px] h-[88px] md:w-24 md:h-28 rounded-xl border transition-all duration-300 flex-shrink-0 animate-stat-reveal',
          activePlanet === planet
            ? 'bg-gray-900 text-white border-gray-900 shadow-lg scale-105'
            : 'bg-white text-gray-400 border-gray-200 hover:border-gray-400 hover:text-gray-600'
        ]"
        :style="{ animationDelay: `${i * 60}ms` }"
      >
        <span class="text-2xl md:text-3xl font-serif mb-1.5">{{ PLANET_SYMBOLS[planet] }}</span>
        <span class="text-[11px] font-medium">{{ planet }}</span>
      </button>
    </div>
    <p class="text-center text-[10px] text-gray-400 italic mb-10">
      点击行星切换命主星领域
    </p>

    <!-- Active planet detail -->
    <div class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden flex flex-col md:flex-row">
      <!-- Name side -->
      <div class="w-full md:w-1/2 p-8 md:p-10 flex flex-col items-center md:items-start justify-center text-center md:text-left bg-gradient-to-b from-gray-50/50 to-white">
        <transition name="fade" mode="out-in">
          <div :key="activePlanet" class="space-y-5">
            <div class="flex items-center gap-3 justify-center md:justify-start">
              <span class="text-3xl font-serif">{{ PLANET_SYMBOLS[activePlanet] }}</span>
              <span class="text-xs font-bold text-gray-400 uppercase tracking-[0.2em]">{{ activePlanet }}</span>
            </div>

            <div>
              <h3 class="text-5xl md:text-6xl hebrew-text font-bold text-black tracking-wide leading-tight">
                {{ result.planetaryGuardians[activePlanet].hebrew }}
              </h3>
            </div>

            <div>
              <p class="text-lg font-mono text-gray-500 tracking-[0.15em] uppercase">
                {{ result.planetaryGuardians[activePlanet].latin }}
              </p>
              <p class="text-sm text-gray-400 mt-1 font-serif italic">
                In the Heaven of {{ activePlanet }}
              </p>
            </div>

            <div class="inline-flex items-center gap-2 px-4 py-2 bg-gray-50 rounded-full border border-gray-100">
              <span class="w-2 h-2 bg-gray-900 rounded-full"></span>
              <span class="text-xs text-gray-600">
                上升星座: <strong>{{ zodiacMap[activePlanet] }}</strong>
              </span>
            </div>
          </div>
        </transition>
      </div>

      <!-- Explanation side -->
      <div class="w-full md:w-1/2 p-8 md:p-10 border-t md:border-t-0 md:border-l border-gray-100 bg-gray-50/30 space-y-5">
        <h4 class="text-sm font-bold text-gray-900 uppercase tracking-wide">The Seven Heavens</h4>
        <p class="text-sm text-gray-600 leading-relaxed font-sans">
          依据 Agrippa 与 Barette 的古老手稿，守护天使并非一成不变。他在七重天中，拥有不同的名字与权能。
        </p>
        <p class="text-sm text-gray-600 leading-relaxed font-sans">
          我们通过特定的字符变换表，去掉天使名中通用的神性后缀（EL），对前缀进行基于 <strong class="text-gray-900">{{ activePlanet }}</strong> 领域的转化。
        </p>
        <div class="bg-white p-4 rounded-lg border border-gray-100">
          <p class="text-xs text-gray-500 leading-relaxed font-serif italic">
            若你的上升星座是 <strong>{{ zodiacMap[activePlanet] }}</strong>，那么 <strong>{{ activePlanet }}</strong> 即是你的命主星。记下左侧这个名字 —— <strong class="text-gray-900 not-italic">{{ result.planetaryGuardians[activePlanet].latin }}</strong>，它将是你与守护灵最强有力的连接通道。
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { PLANET_ORDER, PLANET_SYMBOLS } from '../../data/constants'

defineProps({ result: { type: Object, required: true } })

const activePlanet = ref("月亮")
const planets = PLANET_ORDER

const zodiacMap = {
  "月亮": "巨蟹座",
  "水星": "双子座 / 处女座",
  "金星": "金牛座 / 天秤座",
  "太阳": "狮子座",
  "火星": "白羊座 / 天蝎座",
  "木星": "射手座 / 双鱼座",
  "土星": "摩羯座 / 水瓶座"
}
</script>
