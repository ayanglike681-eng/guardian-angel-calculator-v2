<template>
  <div class="min-h-screen flex flex-col items-center justify-center p-6 bg-white">
    <div class="w-full max-w-lg space-y-10">
      <!-- Header -->
      <div class="text-center space-y-4">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 tracking-tight">
          Guardian Angel
        </h1>
        <p class="text-gray-500 text-sm font-medium">
          Reveal the hidden geometry of your name.
        </p>
      </div>

      <!-- Mode Toggle -->
      <div class="flex justify-center">
        <div class="inline-flex bg-gray-100 rounded-lg p-1">
          <button
            @click="mode = 'chinese'"
            :class="['px-4 py-2 rounded-md text-sm font-medium transition-all',
              mode === 'chinese' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700']"
          >
            中文模式
          </button>
          <button
            @click="mode = 'english'"
            :class="['px-4 py-2 rounded-md text-sm font-medium transition-all',
              mode === 'english' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700']"
          >
            English
          </button>
        </div>
      </div>

      <!-- Chinese Mode -->
      <div v-if="mode === 'chinese'" class="space-y-4">
        <!-- Gender toggle -->
        <div class="flex justify-center gap-2">
          <button
            @click="gender = 'male'"
            :class="['px-6 py-2 rounded-full text-sm font-medium transition-all',
              gender === 'male' ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-500']"
          >男</button>
          <button
            @click="gender = 'female'"
            :class="['px-6 py-2 rounded-full text-sm font-medium transition-all',
              gender === 'female' ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-500']"
          >女</button>
        </div>

        <!-- Name fields -->
        <div class="space-y-3">
          <input
            v-model="ownName"
            type="text"
            class="w-full bg-transparent text-lg text-center text-gray-900 border-b border-gray-200 py-3 focus:border-gray-900 focus:outline-none placeholder-gray-300 transition-colors"
            :placeholder="'自己的名字'"
          />
          <input
            v-model="parent1Name"
            type="text"
            class="w-full bg-transparent text-lg text-center text-gray-900 border-b border-gray-200 py-3 focus:border-gray-900 focus:outline-none placeholder-gray-300 transition-colors"
            :placeholder="gender === 'male' ? '母亲的名字' : '父亲的名字'"
          />
          <input
            v-model="parent2Name"
            type="text"
            class="w-full bg-transparent text-lg text-center text-gray-900 border-b border-gray-200 py-3 focus:border-gray-900 focus:outline-none placeholder-gray-300 transition-colors"
            :placeholder="gender === 'male' ? '父亲的名字' : '母亲的名字'"
          />
          <input
            v-model="surname"
            type="text"
            class="w-full bg-transparent text-lg text-center text-gray-900 border-b border-gray-200 py-3 focus:border-gray-900 focus:outline-none placeholder-gray-300 transition-colors"
            placeholder="姓氏"
          />
        </div>

        <p class="text-[10px] text-gray-400 text-center leading-relaxed">
          命名规则：自己的名字 + {{ gender === 'male' ? '母亲' : '父亲' }}的名字 + {{ gender === 'male' ? '父亲' : '母亲' }}的名字 + 姓氏
        </p>
      </div>

      <!-- English Mode -->
      <div v-else class="space-y-4">
        <input
          v-model="englishName"
          type="text"
          class="w-full bg-transparent text-2xl md:text-3xl font-medium text-center text-gray-900 border-b border-gray-200 py-4 focus:border-gray-900 focus:outline-none placeholder-gray-200 transition-colors duration-300"
          placeholder="Type your name..."
          autofocus
          @keyup.enter="handleAction('wizard')"
        />
      </div>

      <!-- Gematria preview (shared) -->
      <div class="h-8 flex justify-center items-center">
        <div :class="['text-sm font-mono transition-all duration-300', hasInput ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-2']">
          <span class="text-gray-400 mr-2">GEMATRIA VALUE</span>
          <span class="text-gray-900 font-bold">{{ displayValue }}</span>
        </div>
      </div>

      <!-- Action buttons -->
      <div class="flex flex-col sm:flex-row gap-3 pt-2">
        <button
          @click="handleAction('wizard')"
          :disabled="!hasInput || store.isLoading"
          class="flex-1 bg-black text-white h-12 rounded-lg font-medium text-sm hover:bg-gray-800 disabled:opacity-30 disabled:cursor-not-allowed transition-all flex items-center justify-center"
        >
          <span v-if="store.isLoading" class="inline-block w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin mr-2"></span>
          Begin Ritual
        </button>

        <button
          @click="handleAction('dashboard')"
          :disabled="!hasInput || store.isLoading"
          class="flex-1 bg-white text-gray-900 border border-gray-200 h-12 rounded-lg font-medium text-sm hover:bg-gray-50 hover:border-gray-300 disabled:opacity-30 disabled:cursor-not-allowed transition-all flex items-center justify-center"
        >
          View Dashboard
        </button>
      </div>

      <div v-if="store.error" class="text-center text-red-500 text-sm">{{ store.error }}</div>

      <div class="pt-4 text-center">
        <p class="text-[10px] text-gray-300 uppercase tracking-widest font-medium">
          System v3.0 · FastAPI + Vue 3
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useAngelStore } from '../stores/angel'
import { calculateAngel, calculateChineseAngel } from '../api'

const store = useAngelStore()
const router = useRouter()

// Mode state
const mode = ref('chinese')
const gender = ref('male')

// Chinese fields
const ownName = ref('')
const parent1Name = ref('')
const parent2Name = ref('')
const surname = ref('')

// English field
const englishName = ref('')

const displayValue = ref(0)
const previewValue = ref(0)
let animationId = null
let debounceTimer = null

const hasInput = computed(() => {
  if (mode.value === 'chinese') {
    return !!(ownName.value.trim() || parent1Name.value.trim() || parent2Name.value.trim() || surname.value.trim())
  }
  return !!englishName.value.trim()
})

function animateTo(target) {
  if (animationId) cancelAnimationFrame(animationId)
  const start = displayValue.value
  if (start === target) return
  const duration = 400
  const startTime = performance.now()
  const step = (currentTime) => {
    const elapsed = currentTime - startTime
    const progress = Math.min(elapsed / duration, 1)
    const ease = 1 - Math.pow(1 - progress, 4)
    displayValue.value = Math.floor(start + (target - start) * ease)
    if (progress < 1) animationId = requestAnimationFrame(step)
  }
  animationId = requestAnimationFrame(step)
}

// Watch Chinese fields for live preview
watch([ownName, parent1Name, parent2Name, surname, gender], () => {
  if (debounceTimer) clearTimeout(debounceTimer)
  if (mode.value !== 'chinese') return

  if (!hasInput.value) {
    displayValue.value = 0
    previewValue.value = 0
    return
  }

  debounceTimer = setTimeout(async () => {
    try {
      const data = await calculateChineseAngel({
        gender: gender.value,
        ownName: ownName.value.trim() || ' ',
        parent1Name: parent1Name.value.trim() || ' ',
        parent2Name: parent2Name.value.trim() || ' ',
        surname: surname.value.trim() || ' ',
      })
      previewValue.value = data.totalValue || 0
    } catch {
      previewValue.value = 0
    }
  }, 400)
})

// Watch English field for live preview
watch(englishName, (name) => {
  if (debounceTimer) clearTimeout(debounceTimer)
  if (mode.value !== 'english') return

  if (!name || !name.trim()) {
    displayValue.value = 0
    previewValue.value = 0
    return
  }

  debounceTimer = setTimeout(async () => {
    try {
      const data = await calculateAngel(name.trim())
      previewValue.value = data.totalValue || 0
    } catch {
      previewValue.value = 0
    }
  }, 400)
})

// Reset preview on mode switch
watch(mode, () => {
  displayValue.value = 0
  previewValue.value = 0
  if (debounceTimer) clearTimeout(debounceTimer)
})

// Animate on preview change
watch(previewValue, (newVal) => animateTo(newVal))

onBeforeUnmount(() => {
  if (animationId) cancelAnimationFrame(animationId)
  if (debounceTimer) clearTimeout(debounceTimer)
})

async function handleAction(viewMode) {
  if (!hasInput.value) return
  store.isLoading = true
  store.error = null
  try {
    let apiResult
    if (mode.value === 'chinese') {
      apiResult = await calculateChineseAngel({
        gender: gender.value,
        ownName: ownName.value.trim() || ' ',
        parent1Name: parent1Name.value.trim() || ' ',
        parent2Name: parent2Name.value.trim() || ' ',
        surname: surname.value.trim() || ' ',
      })
    } else {
      apiResult = await calculateAngel(englishName.value.trim())
    }
    if (apiResult) {
      store.result = apiResult
      store.viewMode = viewMode
      store.currentStep = 1
      displayValue.value = apiResult.totalValue
      router.push(viewMode === 'dashboard' ? '/dashboard' : '/wizard')
    }
  } catch (e) {
    store.error = e.message || '请求失败，请确认后端已启动'
  } finally {
    store.isLoading = false
  }
}
</script>
