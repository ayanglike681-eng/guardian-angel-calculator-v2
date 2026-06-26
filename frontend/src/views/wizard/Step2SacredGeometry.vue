<template>
  <div class="max-w-5xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Tetragrammaton Structure</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">四字神名结构</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
    </div>

    <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start">
      <!-- Left: explanation + 4 element cards -->
      <div class="w-full lg:w-1/2 space-y-8">
        <p class="text-sm md:text-base text-gray-600 leading-relaxed font-serif">
          我们讨论的不仅是四个字母，而是神创造人的秘密。通过这套技法，守护天使的名字被变造为神圣的四字形式：
        </p>

        <!-- 4 element cards -->
        <div class="grid gap-3">
          <div
            v-for="(item, i) in elements"
            :key="item.label"
            class="group flex items-start gap-4 p-4 rounded-xl border border-gray-100 bg-white hover:border-gray-200 hover:shadow-sm transition-all duration-300 animate-stat-reveal"
            :style="{ animationDelay: `${i * 120}ms` }"
          >
            <!-- Ordinal badge -->
            <div class="flex-shrink-0 w-9 h-9 rounded-lg flex items-center justify-center font-mono text-sm font-bold"
              :class="i === 0 ? 'bg-gray-900 text-white' : i === 1 ? 'bg-gray-100 text-gray-700' : i === 2 ? 'bg-gray-50 text-gray-500 border border-gray-200' : 'bg-white text-gray-400 border border-gray-100'"
            >
              {{ result.tetragram.ordinals[i] }}
            </div>
            <div class="min-w-0 flex-1">
              <div class="flex items-baseline gap-2 mb-1">
                <strong class="text-sm text-gray-900">{{ item.label }}</strong>
                <span class="text-xs text-gray-400 font-mono">{{ item.sub }}</span>
              </div>
              <p class="text-xs text-gray-500 leading-relaxed">{{ item.desc }}</p>
            </div>
            <!-- Hebrew letter -->
            <div class="flex-shrink-0 w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center hebrew-text text-lg font-bold text-gray-700">
              {{ result.tetragram.letters[i] }}
            </div>
          </div>
        </div>

        <p class="text-sm text-gray-400 italic font-serif text-center">
          "如其在内，如其在外。" — 神圣几何的分解确认了灵体的结构平衡。
        </p>
      </div>

      <!-- Right: geometric diagram -->
      <div class="w-full lg:w-1/2 flex justify-center lg:sticky lg:top-24">
        <div class="relative w-80 h-80 md:w-96 md:h-96">
          <!-- Outer decorative ring -->
          <div class="absolute inset-0 border-2 border-gray-100 rounded-full"></div>
          <div class="absolute inset-3 border border-gray-200 rounded-full"></div>
          <div class="absolute inset-8 border border-gray-100 rounded-full"></div>

          <!-- Cross axes -->
          <div class="absolute top-0 bottom-0 left-1/2 w-px bg-gradient-to-b from-transparent via-gray-200 to-transparent"></div>
          <div class="absolute left-0 right-0 top-1/2 h-px bg-gradient-to-r from-transparent via-gray-200 to-transparent"></div>

          <!-- Diagonal axes -->
          <div class="absolute inset-0 flex items-center justify-center opacity-[0.08]">
            <div class="w-px h-full bg-gray-400 rotate-45"></div>
            <div class="w-px h-full bg-gray-400 -rotate-45"></div>
          </div>

          <!-- 4 cardinal letters -->
          <div class="absolute top-6 left-1/2 -translate-x-1/2 bg-white px-3 py-1 rounded-full border border-gray-100 shadow-sm">
            <span class="text-xl hebrew-text font-bold text-gray-900">{{ result.tetragram.letters[0] }}</span>
          </div>
          <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-white px-3 py-1 rounded-full border border-gray-100 shadow-sm">
            <span class="text-xl hebrew-text font-bold text-gray-900">{{ result.tetragram.letters[3] }}</span>
          </div>
          <div class="absolute right-6 top-1/2 -translate-y-1/2 bg-white px-3 py-1 rounded-full border border-gray-100 shadow-sm">
            <span class="text-xl hebrew-text font-bold text-gray-900">{{ result.tetragram.letters[1] }}</span>
          </div>
          <div class="absolute left-6 top-1/2 -translate-y-1/2 bg-white px-3 py-1 rounded-full border border-gray-100 shadow-sm">
            <span class="text-xl hebrew-text font-bold text-gray-900">{{ result.tetragram.letters[2] }}</span>
          </div>

          <!-- Center: combined tetragram -->
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="relative">
              <div class="absolute inset-0 bg-gold-400/20 rounded-full blur-xl"></div>
              <div class="relative w-20 h-20 md:w-24 md:h-24 bg-gray-900 text-gold-400 rounded-full flex items-center justify-center text-2xl md:text-3xl hebrew-text font-bold shadow-2xl ring-1 ring-gold-400/50">
                {{ result.tetragram.letters }}
              </div>
            </div>
          </div>

          <!-- Cardinal labels -->
          <span class="absolute -top-1 left-1/2 -translate-x-1/2 text-[9px] text-gray-300 uppercase tracking-widest font-medium">Father</span>
          <span class="absolute -bottom-1 left-1/2 -translate-x-1/2 text-[9px] text-gray-300 uppercase tracking-widest font-medium">Daughter</span>
          <span class="absolute -right-1 top-1/2 -translate-y-1/2 text-[9px] text-gray-300 uppercase tracking-widest font-medium">Mother</span>
          <span class="absolute -left-1 top-1/2 -translate-y-1/2 text-[9px] text-gray-300 uppercase tracking-widest font-medium">Son</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ result: { type: Object, required: true } })

const elements = [
  { label: '大亚当', sub: 'Father · 亚当之血肉', desc: '源自名字数值的宏大总和，神尚未吹入灵气之前的原始存在。' },
  { label: '大夏娃', sub: 'Mother · 亚当之肋', desc: '灵与肉的结合与分离，如同夏娃从亚当身上被取下，代表孕育与生命。' },
  { label: '小亚当', sub: 'Son · 衍生本质', desc: '将天使之名与神性后缀分离，通过神性之楔拆解出的纯粹本质。' },
  { label: '小夏娃', sub: 'Daughter · 最终显化', desc: '灵体的最终显化与神圣循环的完成。' },
]
</script>
