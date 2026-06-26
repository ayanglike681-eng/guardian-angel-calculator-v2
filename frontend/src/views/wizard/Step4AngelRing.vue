<template>
  <section v-if="result" class="max-w-5xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Covenant Seal</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">圣契之戒</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
    </div>

    <div class="flex flex-col lg:flex-row gap-12 items-start">
      <!-- Left: seal diagram -->
      <div class="w-full lg:w-1/2 bg-gray-50/70 border border-gray-100 rounded-2xl p-6 md:p-10 flex flex-col items-center justify-center relative min-h-[400px] overflow-hidden">
        <!-- Grid background -->
        <div class="absolute inset-0 opacity-[0.025]" style="background-image: linear-gradient(#000 1px, transparent 1px), linear-gradient(90deg, #000 1px, transparent 1px); background-size: 20px 20px;"></div>

        <svg viewBox="0 0 500 500" class="w-full max-w-[340px] h-auto z-10">
          <!-- Outer construction ring -->
          <circle cx="250" cy="250" r="240" fill="none" stroke="#e5e7eb" stroke-width="1" stroke-dasharray="4 6" />
          <!-- Main ring -->
          <circle cx="250" cy="250" r="228" fill="none" stroke="#171717" stroke-width="1.5" />
          <!-- Inner subtle ring -->
          <circle cx="250" cy="250" r="200" fill="none" stroke="#e5e7eb" stroke-width="0.5" />

          <!-- Pentagram -->
          <path
            d="M 250 50 L 368 412 L 58 188 L 442 188 L 132 412 Z"
            fill="none"
            stroke="#171717"
            stroke-width="1.5"
            stroke-linejoin="round"
          />

          <!-- Center Yod with glow -->
          <circle cx="250" cy="250" r="36" fill="none" stroke="#D4AF37" stroke-width="0.5" opacity="0.4" />
          <text x="250" y="278" text-anchor="middle" class="text-7xl fill-gold-400 hebrew-text font-bold">י</text>

          <!-- Four corners: sacred names -->
          <g class="hebrew-text text-2xl fill-gray-700 font-medium">
            <text x="385" y="160" text-anchor="middle">אחת</text>
            <text x="115" y="160" text-anchor="middle">רוח</text>
            <text x="425" y="325" text-anchor="middle">אלוהים</text>
            <text x="75" y="325" text-anchor="middle">חיים</text>
          </g>

          <!-- Bottom tetragram -->
          <text x="250" y="455" text-anchor="middle" class="text-4xl fill-gray-900 hebrew-text font-bold tracking-widest">
            {{ result.tetragram.letters }}
          </text>
        </svg>

        <p class="text-[10px] text-gray-400 mt-6 uppercase tracking-widest font-mono z-10">
          Fig 4.0: The Seal of the Covenant
        </p>
      </div>

      <!-- Right: text modules -->
      <article class="w-full lg:w-1/2 space-y-8">
        <div
          v-for="(mod, i) in modules"
          :key="i"
          class="animate-stat-reveal"
          :style="{ animationDelay: `${i * 150}ms` }"
        >
          <h3 class="text-sm font-bold text-gray-900 uppercase border-l-2 border-gray-900 pl-3 mb-3">
            {{ mod.title }}
          </h3>

          <!-- Inscription grid (special case for module 1) -->
          <div v-if="i === 1" class="grid grid-cols-2 gap-3 text-xs font-mono text-gray-600 mb-3">
            <div class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex flex-col gap-0.5">
              <span class="text-[10px] text-gray-400 uppercase">右上 · Achath</span>
              <span class="text-gray-900 font-medium">一</span>
            </div>
            <div class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex flex-col gap-0.5">
              <span class="text-[10px] text-gray-400 uppercase">左上 · Rvach</span>
              <span class="text-gray-900 font-medium">灵</span>
            </div>
            <div class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex flex-col gap-0.5">
              <span class="text-[10px] text-gray-400 uppercase">右下 · Elohim</span>
              <span class="text-gray-900 font-medium">神</span>
            </div>
            <div class="bg-gray-50 p-3 rounded-lg border border-gray-100 flex flex-col gap-0.5">
              <span class="text-[10px] text-gray-400 uppercase">左下 · Cheyim</span>
              <span class="text-gray-900 font-medium">永生</span>
            </div>
          </div>

          <p class="text-sm text-gray-600 leading-relaxed font-sans">
            {{ mod.body }}
          </p>

          <p v-if="mod.note" class="text-xs text-gray-400 italic mt-2">{{ mod.note }}</p>

          <!-- Inner ring formula -->
          <div v-if="i === 2" class="mt-4 pt-4 border-t border-dashed border-gray-200">
            <div class="text-[10px] uppercase font-bold tracking-widest text-gray-400 mb-2">内环公式</div>
            <div class="font-mono text-xs bg-gray-900 text-white/90 p-3 rounded-lg flex items-center gap-2 overflow-x-auto">
              <span class="w-2 h-2 rounded-full bg-gold-400 animate-pulse flex-shrink-0"></span>
              <span class="whitespace-nowrap">EL + AGLA + ELOHA + {{ result.hebrewName }}</span>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
defineProps({ result: { type: Object, required: true } })

const modules = [
  {
    title: '微观与宏观之桥',
    body: '守护天使之戒的构型在微观（个人）与宏观（星体）间架起了桥梁。戒指图样的主体是一个五角星，将圆划分为六个神圣区域，每一区域皆镌刻着力量与赞美的呼唤。',
  },
  {
    title: '四方铭文解析',
    body: '戒面四周镌刻着四组词句，宣告终极真理。',
    note: '"一"、"灵"、"神"、"永生" —— 合而为一，即是 "一是永生神的灵"。',
  },
  {
    title: '神圣之名',
    body: '戒面底部的 Tetragrammaton 是你的力量之名。最中央的 Yod 是神圣能量的原点——构成所有字母的基石，象征神之无所不在，亦代表存在于你内在的神圣火花。',
  },
]
</script>
