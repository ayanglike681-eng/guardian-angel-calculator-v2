<template>
  <div v-if="squareData" class="max-w-5xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Solar Kamea</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">太阳幻方</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
      <p class="text-xs text-gray-400 mt-3 font-mono">6 × 6 · 三十六宫 · 太阳之印</p>
    </div>

    <!-- Main card -->
    <div class="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
      <div class="flex flex-col lg:flex-row">
        <!-- Left: grid -->
        <div class="w-full lg:w-7/12 p-6 md:p-10 flex flex-col items-center justify-center bg-gray-50/50">
          <div class="relative p-2 md:p-3 bg-white rounded-xl shadow-lg border border-gray-100 rotate-0 md:rotate-1 transition-transform hover:rotate-0 duration-700">
            <div class="grid grid-cols-6 gap-1.5 md:gap-2">
              <template v-for="(row, r) in squareData.grid" :key="r">
                <div
                  v-for="(val, c) in row"
                  :key="`${r}-${c}`"
                  :class="[
                    'w-10 h-10 md:w-12 md:h-12 flex items-center justify-center text-xs md:text-sm font-mono rounded-md transition-all duration-300',
                    r === c
                      ? 'bg-amber-50 text-amber-800 font-bold border border-amber-200 shadow-sm'
                      : 'bg-white text-gray-600 border border-gray-50 hover:border-gray-200 hover:shadow-sm'
                  ]"
                >
                  {{ val }}
                </div>
              </template>
            </div>
          </div>

          <p class="mt-6 text-xs font-serif italic text-gray-400 text-center">
            每行·每列·每对角线之和 = <span class="font-bold text-gray-600 font-mono not-italic">{{ targetSum }}</span>
          </p>
        </div>

        <!-- Right: parameters -->
        <div class="w-full lg:w-5/12 p-6 md:p-10 border-t lg:border-t-0 lg:border-l border-gray-100 bg-white flex flex-col justify-center space-y-6">
          <div>
            <h3 class="text-lg font-bold text-gray-900 mb-1">Solar Kamea</h3>
            <p class="text-xs text-gray-400 leading-relaxed">
              幻方是一扇精巧的门。基于<strong class="text-gray-600">太阳（六阶）</strong>法则，将守护天使的数值注入三十六宫。当计算出现非整数时，通过<strong class="text-gray-600">"雅各的梯子"</strong>对对角线修正，以恢复平衡。
            </p>
          </div>

          <!-- Parameter grid -->
          <div class="grid grid-cols-2 gap-3">
            <div
              v-for="param in parameters"
              :key="param.label"
              class="bg-gray-50 rounded-xl border border-gray-100 p-4 text-center group hover:border-gray-200 transition-colors"
            >
              <div class="text-[10px] text-gray-400 uppercase tracking-widest mb-1.5">{{ param.label }}</div>
              <div :class="['text-xl font-mono font-bold', param.color || 'text-gray-900']">
                {{ param.value }}
              </div>
              <div class="text-[10px] text-gray-400 mt-1 font-sans">{{ param.note }}</div>
            </div>
          </div>

          <!-- Lock line -->
          <div class="pt-4 border-t border-dashed border-gray-200 text-center">
            <span class="text-[10px] text-gray-400 uppercase tracking-widest">Locked at</span>
            <span class="text-lg font-mono font-bold text-gray-900 ml-2">{{ squareData.lock }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { generateAngelSquare } from '../../composables/useMagicSquare'

const props = defineProps({ value: { type: Number, required: true } })

const squareData = computed(() => generateAngelSquare(props.value))

const targetSum = computed(() => {
  if (!squareData.value) return 0
  return squareData.value.grid[0]?.reduce((a, b) => a + b, 0) || 0
})

const parameters = computed(() => [
  { label: 'Key', value: squareData.value.key, color: 'text-gray-900', note: '起始之钥' },
  { label: 'Handle', value: squareData.value.handle, color: 'text-gray-900', note: '数字根' },
  { label: 'Door', value: squareData.value.door, color: 'text-gray-900', note: '35 × Handle' },
  { label: 'Amend', value: `${squareData.value.remainder > 0 ? '+' : ''}${squareData.value.remainder}`, color: squareData.value.remainder !== 0 ? 'text-red-500' : 'text-gray-400', note: '雅各的梯子' },
])
</script>
