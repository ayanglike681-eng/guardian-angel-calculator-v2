<template>
  <div class="max-w-7xl mx-auto px-4 py-12">
    <button
      @click="handleBackToInput"
      class="flex items-center gap-2 text-secondary hover:text-primary mb-8 cursor-pointer uppercase text-xs font-bold tracking-widest"
    >
      <IconChevronLeft class="w-4 h-4" /> Back to Input
    </button>

    <!-- Sticky Step Indicator -->
    <div class="sticky top-0 z-40 bg-white/90 backdrop-blur py-3 -mx-4 px-4">
      <StepIndicator :currentStep="currentVisibleStep" :totalSteps="7" />
    </div>

    <!-- All 7 steps stacked vertically -->
    <div class="space-y-4">
      <div ref="stepRefs" data-step="1">
        <Step1OriginReveal :result="store.result" />
      </div>
      <div data-step="2">
        <Step2SacredGeometry :result="store.result" />
      </div>
      <div data-step="3">
        <Step3CovenantRitual :result="store.result" />
      </div>
      <div data-step="4">
        <Step4AngelRing :result="store.result" />
      </div>
      <div data-step="5">
        <Step5HeliosConsecration :result="store.result" />
      </div>
      <div data-step="6">
        <Step6MagicSquare :value="store.result.totalValue" />
      </div>
      <div data-step="7">
        <Step7FinalRitual :result="store.result" @restart="handleBackToInput" />
      </div>
    </div>

    <!-- Back to top -->
    <div class="text-center mt-16 pb-12">
      <button
        @click="scrollToTop"
        class="text-xs text-gray-400 hover:text-gray-600 transition-colors uppercase tracking-widest"
      >
        Back to Top
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { useAngelStore } from '../../stores/angel'
import IconChevronLeft from '../../components/icons/IconChevronLeft.vue'
import StepIndicator from '../../components/StepIndicator.vue'
import Step1OriginReveal from './Step1OriginReveal.vue'
import Step2SacredGeometry from './Step2SacredGeometry.vue'
import Step3CovenantRitual from './Step3CovenantRitual.vue'
import Step4AngelRing from './Step4AngelRing.vue'
import Step5HeliosConsecration from './Step5HeliosConsecration.vue'
import Step6MagicSquare from './Step6MagicSquare.vue'
import Step7FinalRitual from './Step7FinalRitual.vue'

const router = useRouter()
const store = useAngelStore()

const currentVisibleStep = ref(1)
let observer = null

onMounted(() => {
  const steps = document.querySelectorAll('[data-step]')
  if (steps.length === 0) return

  observer = new IntersectionObserver(
    (entries) => {
      // Find the step that's most visible
      let maxRatio = 0
      let maxStep = 1
      entries.forEach((entry) => {
        if (entry.intersectionRatio > maxRatio) {
          maxRatio = entry.intersectionRatio
          maxStep = parseInt(entry.target.dataset.step)
        }
      })
      if (maxRatio > 0) {
        currentVisibleStep.value = maxStep
        store.currentStep = maxStep
      }
    },
    { threshold: [0, 0.25, 0.5, 0.75, 1] }
  )

  steps.forEach((el) => observer.observe(el))
})

onBeforeUnmount(() => {
  if (observer) observer.disconnect()
})

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function handleBackToInput() {
  store.reset()
  router.push('/')
}
</script>
