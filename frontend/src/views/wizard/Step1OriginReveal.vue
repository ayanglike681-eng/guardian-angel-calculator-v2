<template>
  <div class="max-w-2xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Origin Analysis</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">起源揭示</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
    </div>

    <!-- Name reveal card -->
    <div class="relative mb-14 mx-4 md:mx-0">
      <div class="absolute inset-0 bg-gradient-to-b from-gray-50 to-white rounded-3xl -z-10"></div>
      <div class="border border-gray-100 rounded-3xl p-8 md:p-12 text-center">
        <!-- Hebrew name — hero element -->
        <h3 class="text-5xl sm:text-6xl md:text-7xl hebrew-text font-bold text-black tracking-wider leading-tight mb-5 animate-fade-in">
          {{ result.hebrewLetters }}<span class="text-gold-400">אל</span>
        </h3>

        <!-- Latin transliteration -->
        <p class="text-lg md:text-xl font-mono text-gray-500 tracking-[0.25em] uppercase mb-8">
          {{ result.latinResult }}
        </p>

        <!-- Divider -->
        <div class="flex items-center gap-4 justify-center mb-8">
          <span class="h-px flex-1 bg-gray-100 max-w-16"></span>
          <span class="w-1 h-1 rounded-full bg-gold-400"></span>
          <span class="h-px flex-1 bg-gray-100 max-w-16"></span>
        </div>

        <!-- Gematria value -->
        <div class="inline-flex flex-col items-center">
          <span class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.2em] mb-1">Gematria</span>
          <span class="text-3xl md:text-4xl font-mono font-bold text-gray-900 tabular-nums">{{ result.totalValue }}</span>
        </div>
      </div>
    </div>

    <!-- Philosophical text — staggered reveal -->
    <div class="space-y-8 px-4 md:px-0 max-w-lg mx-auto">
      <div
        v-for="(text, i) in passages"
        :key="i"
        class="animate-stat-reveal"
        :style="{ animationDelay: `${300 + i * 200}ms` }"
      >
        <p
          :class="[
            'text-sm md:text-base leading-relaxed',
            i === 2 ? 'font-semibold text-gray-900' : 'text-gray-600 font-serif',
          ]"
        >
          {{ text }}
        </p>
        <div v-if="i < passages.length - 1" class="w-4 h-px bg-gray-200 mt-6"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ result: { type: Object, required: true } })

const passages = [
  '贤者们宣称"万物皆数"。每一个魔法师都知道，字母拥有对应的数值，拥有潜在的火光。名字不仅仅是一个称呼，它是强有力的灵魂纽带，谁掌握了名字，谁就掌握了钥匙。',
  '我们不仅仅是在计算数字，而是在追溯本质。你的守护天使，其本质乃是太阳之灵，其源泉乃是大光之光。通过你出生时被赋予的真名，我们将揭示那位与你灵魂永恒连接的"完美本性"。',
  '我们已将四元素的能量转化为数值，再将其映射回神圣的希伯来字母，最终显现出那位专属于你的守护天使之名。',
]
</script>
