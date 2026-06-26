<template>
  <div v-if="store.result" class="min-h-screen bg-gray-50 text-primary font-sans pb-20">
    <div class="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div class="max-w-5xl mx-auto px-4 h-12 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="w-1.5 h-1.5 rounded-full bg-primary"></span>
          <span class="text-xs font-semibold tracking-wide">ANGELIC ARCHIVE</span>
        </div>
        <button @click="handleReset" class="text-xs text-gray-400 hover:text-primary transition-colors">
          Reset
        </button>
      </div>
    </div>

    <div class="max-w-5xl mx-auto px-4 py-8 space-y-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="md:col-span-2 bg-white border border-gray-200 rounded-lg p-6">
          <div class="mb-6">
            <p class="text-[10px] font-medium text-gray-400 uppercase tracking-wider mb-1">Subject Identity</p>
            <h2 class="text-3xl font-semibold text-primary">{{ store.result.latinResult }}</h2>
          </div>
          <div class="flex items-end gap-8">
            <div>
              <p class="text-[10px] font-medium text-gray-400 uppercase tracking-wider mb-2">Hebrew</p>
              <p class="text-3xl font-medium hebrew-text">{{ store.result.hebrewName }}</p>
            </div>
            <div class="h-8 w-px bg-gray-200"></div>
            <div>
              <p class="text-[10px] font-medium text-gray-400 uppercase tracking-wider mb-2">Value</p>
              <p class="text-3xl font-mono font-medium text-primary">{{ store.result.totalValue }}</p>
            </div>
          </div>
        </div>

        <div class="bg-primary text-white rounded-lg p-6 flex flex-col justify-center">
          <p class="text-[10px] font-medium text-gray-400 uppercase tracking-wider mb-4">Tetragrammaton</p>
          <p class="text-4xl font-medium hebrew-text tracking-widest text-center">{{ store.result.tetragram.letters }}</p>
          <div class="flex justify-center gap-4 mt-4">
            <span class="text-[9px] text-gray-500">Father</span>
            <span class="text-[9px] text-gray-500">Mother</span>
            <span class="text-[9px] text-gray-500">Son</span>
            <span class="text-[9px] text-gray-500">Daughter</span>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        <div class="bg-white border border-gray-200 rounded-lg p-6">
          <div class="flex justify-between items-center mb-4">
            <h3 class="font-semibold text-sm">Solar Kamea</h3>
            <div class="flex gap-3 text-[10px] font-mono text-gray-400">
              <span>Key: {{ squareData.key }}</span>
              <span>Lock: {{ squareData.lock }}</span>
            </div>
          </div>
          <div class="flex justify-center">
            <div class="grid grid-cols-6 gap-px bg-gray-100 p-1">
              <template v-for="(row, r) in squareData.grid" :key="r">
                <div
                  v-for="(val, c) in row"
                  :key="`${r}-${c}`"
                  :class="['w-8 h-8 flex items-center justify-center text-xs font-mono', r === c ? 'bg-primary text-white' : 'bg-white text-gray-600']"
                >{{ val }}</div>
              </template>
            </div>
          </div>
        </div>

        <div class="bg-white border border-gray-200 rounded-lg p-6">
          <h3 class="font-semibold text-sm mb-4">Planetary Hierarchy</h3>
          <div class="space-y-0">
            <div
              v-for="planet in planets" :key="planet"
              class="flex items-center justify-between py-2 border-b border-gray-100 last:border-0"
            >
              <div class="flex items-center gap-3">
                <span class="text-sm text-gray-400 w-5">{{ PLANET_SYMBOLS[planet] }}</span>
                <span class="text-sm font-medium">{{ planet }}</span>
              </div>
              <span class="text-sm hebrew-text text-gray-600">{{ store.result.planetaryGuardians[planet].hebrew }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-white border border-gray-200 rounded-lg p-6">
        <h3 class="font-semibold text-sm mb-4">Seal Construction</h3>
        <div class="flex justify-center">
          <svg viewBox="0 0 500 500" class="w-full h-auto max-w-[200px]">
            <circle cx="250" cy="250" r="235" fill="none" stroke="currentColor" stroke-width="1.5" class="text-primary"/>
            <circle cx="250" cy="250" r="228" fill="none" stroke="currentColor" stroke-width="0.5" class="text-gray-300"/>
            <path d="M 250 50 L 368 412 L 58 188 L 442 188 L 132 412 Z" fill="none" stroke="currentColor" stroke-width="1" class="text-gray-600"/>
            <text x="250" y="275" text-anchor="middle" class="text-6xl fill-primary hebrew-text font-bold">&#1497;</text>
            <text x="250" y="445" text-anchor="middle" class="text-4xl fill-primary hebrew-text font-bold tracking-widest">
              {{ store.result.tetragram.letters }}
            </text>
          </svg>
        </div>
      </div>

      <div class="bg-white border border-gray-200 rounded-lg p-6">
        <h3 class="font-semibold text-sm mb-4">The 22 Names of Power</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2">
          <div
            v-for="(item, idx) in store.result.powerNames" :key="idx"
            class="p-2 border border-gray-100 rounded"
          >
            <div class="flex justify-between items-start mb-1">
              <span class="text-[9px] text-gray-300 font-mono">{{ String(idx + 1).padStart(2, '0') }}</span>
            </div>
            <div class="font-medium text-gray-900 text-sm hebrew-text">{{ item.hebrew }}</div>
            <div class="text-[9px] text-gray-400 font-mono">{{ item.latin || '-' }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="min-h-screen flex items-center justify-center text-gray-400">
    No data. Please go back and enter a name.
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAngelStore } from '../stores/angel'
import { generateAngelSquare } from '../composables/useMagicSquare'
import { PLANET_SYMBOLS } from '../data/constants'

const store = useAngelStore()
const router = useRouter()

const planets = ["太阳", "月亮", "水星", "金星", "火星", "木星", "土星"]

const squareData = computed(() => {
  if (!store.result) return { grid: [], key: 0, lock: 0, handle: 0, door: 0, remainder: 0 }
  return generateAngelSquare(store.result.totalValue)
})

function handleReset() {
  store.reset()
  router.push('/')
}
</script>
