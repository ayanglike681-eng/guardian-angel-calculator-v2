import { defineStore } from 'pinia'
import { ref } from 'vue'
import { calculateAngel } from '../api'

export const useAngelStore = defineStore('angel', () => {
  const inputName = ref('')
  const result = ref(null)
  const currentStep = ref(1)
  const viewMode = ref('wizard')
  const isLoading = ref(false)
  const error = ref(null)

  async function calculateName(mode = 'wizard') {
    if (!inputName.value.trim()) return
    isLoading.value = true
    error.value = null
    try {
      const data = await calculateAngel(inputName.value)
      result.value = data
      viewMode.value = mode
      currentStep.value = 1
    } catch (e) {
      error.value = e.message || 'Calculation failed'
      result.value = null
    } finally {
      isLoading.value = false
    }
  }

  function reset() {
    inputName.value = ''
    result.value = null
    currentStep.value = 1
    viewMode.value = 'wizard'
    error.value = null
  }

  return { inputName, result, currentStep, viewMode, isLoading, error, calculateName, reset }
})
