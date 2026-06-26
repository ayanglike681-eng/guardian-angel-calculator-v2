<template>
  <div class="max-w-5xl mx-auto py-12 md:py-16">
    <!-- Section header -->
    <div class="text-center mb-14">
      <p class="text-[10px] font-medium text-gray-400 uppercase tracking-[0.3em] mb-3">Rite of Helios Consecration</p>
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 tracking-tight">太阳之戒圣化仪式</h2>
      <div class="w-8 h-px bg-gold-400 mx-auto mt-4"></div>
      <p class="text-xs text-gray-400 mt-3 font-serif italic max-w-md mx-auto">
        PGM IV.1596–1715 · 借 Helios 之力圣化守护天使之戒
      </p>
    </div>

    <div class="flex flex-col lg:flex-row gap-12 lg:gap-16 items-start">
      <!-- Left: Helios Disk -->
      <div class="w-full lg:w-2/5 lg:sticky lg:top-24">
        <div class="aspect-square relative border-2 border-gray-100 rounded-full flex items-center justify-center bg-white shadow-sm">
          <!-- 12 face names radiating -->
          <div
            v-for="(hour, i) in HOURS_DATA"
            :key="i"
            class="absolute inset-0 flex justify-center"
            :style="{ transform: `rotate(${i * 30}deg)` }"
          >
            <div class="h-full w-8 relative">
              <span class="absolute top-5 left-1/2 -translate-x-1/2 text-[8px] md:text-[9px] font-mono tracking-[0.15em] text-gray-400 uppercase h-20 text-center writing-vertical-rl leading-tight">
                {{ hour.name }}
              </span>
            </div>
          </div>

          <!-- Inner ring -->
          <div class="absolute inset-[22%] border border-gray-200 rounded-full"></div>

          <!-- Red center — the sun -->
          <div class="w-28 h-28 md:w-32 md:h-32 bg-[#8B3A3A] rounded-full flex flex-col items-center justify-center text-white z-10 shadow-inner ring-1 ring-[#6B2A2A]">
            <div class="text-2xl md:text-3xl hebrew-text font-bold mb-1">{{ result.hebrewName }}</div>
            <div class="text-[8px] md:text-[9px] uppercase tracking-widest opacity-80 font-mono text-center px-1.5 leading-tight">
              {{ result.latinResult }}
            </div>
          </div>
        </div>
        <p class="text-center text-[10px] text-gray-400 mt-6 uppercase tracking-widest font-mono">
          The Disk of Helios
        </p>
      </div>

      <!-- Right: Ritual steps -->
      <div class="w-full lg:w-3/5 space-y-14">
        <!-- I. 仪式准备 -->
        <section class="animate-stat-reveal">
          <h3 class="text-sm font-bold text-gray-900 uppercase flex items-center gap-3 mb-5">
            <span class="w-6 h-6 bg-gray-900 text-white flex items-center justify-center text-xs rounded-md">I</span>
            仪式准备
          </h3>
          <div class="bg-gray-50 rounded-xl border border-gray-100 p-6 space-y-4">
            <p class="text-sm text-gray-700 leading-relaxed">
              准备一张<strong>仪式桌</strong>，桌面中央绘制<strong>红色圆心</strong>区域，用于放置待圣化的戒指。
            </p>
            <div class="space-y-3 text-sm text-gray-600">
              <p class="flex items-start gap-3">
                <span class="font-serif text-base leading-none mt-0.5">&dagger;</span>
                <span><strong class="text-gray-900">黑色蜡烛</strong>十二根，环绕圆盘铺设，对应太阳的十二种形态。若蜡烛不足，至少准备<strong class="text-gray-900">东、南、西、北四根</strong>方位蜡烛。</span>
              </p>
              <p class="flex items-start gap-3">
                <span class="font-serif text-base leading-none mt-0.5">&dagger;</span>
                <span>准备<strong class="text-gray-900">一个空碗</strong>，倒入圣油（Abramelin Oil）或初榨橄榄油。</span>
              </p>
              <p class="flex items-start gap-3">
                <span class="font-serif text-base leading-none mt-0.5">&dagger;</span>
                <span>将待圣化的戒指置于红色圆心之上。</span>
              </p>
            </div>
          </div>
        </section>

        <!-- II. 十二时辰祈祷 -->
        <section class="animate-stat-reveal" style="animation-delay: 150ms">
          <h3 class="text-sm font-bold text-gray-900 uppercase flex items-center gap-3 mb-5">
            <span class="w-6 h-6 bg-gray-900 text-white flex items-center justify-center text-xs rounded-md">II</span>
            十二时辰祈祷
          </h3>

          <p class="text-sm text-gray-500 italic font-serif mb-5">
            "每一时辰对应 Helios 在一天之中的十二张面庞，每一张面庞以一种动物为其化身。祈祷之时，须面对该时辰在圆盘上的方位，默思其面庞。"
          </p>

          <!-- 12 hours grid -->
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-5">
            <div
              v-for="h in HOURS_DATA"
              :key="h.id"
              class="flex items-center gap-4 p-3.5 rounded-lg border border-gray-100 bg-white hover:border-gray-200 transition-colors"
            >
              <div class="flex-shrink-0 w-7 h-7 rounded-full bg-gray-100 flex items-center justify-center text-[10px] font-bold text-gray-500">
                {{ h.id }}
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-baseline gap-2">
                  <span class="text-xs font-bold text-gray-900">{{ h.animal }}</span>
                </div>
                <p class="text-[10px] font-mono text-gray-400 uppercase mt-0.5 truncate">{{ h.name }}</p>
              </div>
              <div class="text-[11px] font-serif text-gray-600 tracking-wide flex-shrink-0">{{ h.greek }}</div>
            </div>
          </div>

          <p class="text-xs text-gray-400 italic text-center">
            十二张面庞祈祷完毕后，<strong class="text-gray-600">熄灭所有蜡烛</strong>。
          </p>
        </section>

        <!-- III. 正午受膏礼 -->
        <section class="animate-stat-reveal" style="animation-delay: 300ms">
          <h3 class="text-sm font-bold text-gray-900 uppercase flex items-center gap-3 mb-5">
            <span class="w-6 h-6 bg-gray-900 text-white flex items-center justify-center text-xs rounded-md">III</span>
            正午受膏礼
          </h3>

          <p class="text-sm text-gray-500 mb-6 leading-relaxed">
            等到十二个小时的祈祷完成后，<strong class="text-gray-700">不要在过程中熄灭蜡烛</strong>。等到中午太阳升至最高时，进行以下祈祷。此时你<strong class="text-gray-700">立足于世界之中</strong>，你是天空中的王。
          </p>

          <!-- Invocation names -->
          <div class="mb-6">
            <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">召唤之名</p>
            <div class="flex flex-wrap gap-2">
              <span v-for="name in invocationNames" :key="name"
                class="px-3 py-1.5 bg-gray-50 border border-gray-100 rounded-lg text-xs font-mono text-gray-600"
              >{{ name }}</span>
            </div>
          </div>

          <!-- Prayer card -->
          <div class="border-l-4 border-gray-900 pl-6 py-2">
            <div class="bg-[#FDFBF7] p-6 md:p-8 rounded-lg border border-[#E8E4DB]">
              <p class="text-sm md:text-base text-gray-800 leading-loose font-serif text-justify">
                你立足于世界之上，你是世界的长者，你是天空中的王。在这至圣至洁的时刻倾听我的呼唤，并将这戒指为圣，为了伟大的
                <span class="text-[10px] text-gray-400 mx-1 uppercase tracking-wider">Kmeph · Lutheuth · Orphuikhe · Ortilibekhuch · Ierkhe · Rum · Iperitao · Yai</span>
                我召唤天地间的光芒与黑暗，我召唤那创造了一切的伟大之神 <strong class="text-gray-900">Sarusin</strong>，
                为同我伟大的助手
                <strong class="text-gray-900 text-lg mx-1 hebrew-text align-middle">{{ result.hebrewName }}</strong>
                (<span class="uppercase tracking-wide text-sm">{{ result.latinResult }}</span>) 相连，
                惟愿我愿成就。
              </p>

              <div class="mt-8 pt-6 border-t border-[#E8E4DB] text-center space-y-2">
                <span class="block text-[10px] text-gray-400 uppercase tracking-[0.3em]">The One God Is</span>
                <span class="text-2xl font-bold text-gray-900 tracking-[0.2em] font-serif">SERAPIS</span>
              </div>
            </div>
          </div>
        </section>

        <!-- IV. 浸油圣化 -->
        <section class="animate-stat-reveal" style="animation-delay: 450ms">
          <h3 class="text-sm font-bold text-gray-900 uppercase flex items-center gap-3 mb-5">
            <span class="w-6 h-6 bg-gray-900 text-white flex items-center justify-center text-xs rounded-md">IV</span>
            浸油圣化
          </h3>
          <div class="bg-gray-50 rounded-xl border border-gray-100 p-6">
            <p class="text-sm text-gray-600 leading-relaxed mb-3">
              最后的浸油礼——"通过淹没来圣化"——贯穿整个 PGM 仪式传统。这是从第一篇对守护神的召唤开始便存在的仪式部件。
            </p>
            <p class="text-sm text-gray-600 leading-relaxed">
              将戒指浸入圣油碗中，宣告："<strong class="text-gray-900">以 Serapis 之名，此戒为圣。</strong>"完毕后，仪式即成。
            </p>
          </div>
        </section>

        <p class="text-center text-xs text-gray-400 pt-2">
          Source: PGM IV.1596–1715 · 元素之数与太阳之灵
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ result: { type: Object, required: true } })

const HOURS_DATA = [
  { id: 1, animal: '猫 (Cat)', name: 'Pharakuneth', greek: 'ΦΑΡΑΚΟΥΝΗΘ' },
  { id: 2, animal: '狗 (Dog)', name: 'Suphy', greek: 'ΣΟΥΦΙ' },
  { id: 3, animal: '蛇 (Serpent)', name: 'Amekranebecheoth Thouth', greek: 'ΑΜΕΚΡΑΝΕΒΕΧΕΟ ΘΩΥΘ' },
  { id: 4, animal: '圣甲虫 (Scarab)', name: 'Senthenips', greek: 'ΣΕΝΘΕΝΙΨ' },
  { id: 5, animal: '驴 (Donkey)', name: 'Enphankuph', greek: 'ΕΝΦΑΝΧΟΥΦ' },
  { id: 6, animal: '狮子 (Lion)', name: 'Bai Solbai', greek: 'ΒΑΙ ΣΟΛΒΑΙ' },
  { id: 7, animal: '山羊 (Goat)', name: 'Umethoth', greek: 'ΟΥΜΕΣΘΩΘ' },
  { id: 8, animal: '公牛 (Bull)', name: 'Diatiphe', greek: 'ΔΙΑΤΙΦΗ' },
  { id: 9, animal: '隼 (Falcon)', name: 'Pheusphoth', greek: 'ΦΗΟΥΣ ΦΩΟΥΘ' },
  { id: 10, animal: '狒狒 (Baboon)', name: 'Besbyki', greek: 'ΒΕΣΒΥΚΙ' },
  { id: 11, animal: '鹮 (Ibis)', name: 'Muroph', greek: 'ΜΟΥ ΡΩΦ' },
  { id: 12, animal: '鳄鱼 (Crocodile)', name: 'Aerthoe', greek: 'ΑΕΡΘΟΗ' },
]

const invocationNames = ['Kmeph', 'Lutheuth', 'Orphuikhe', 'Ortilibekhuch', 'Ierkhe', 'Rum', 'Iperitao', 'Yai']
</script>
