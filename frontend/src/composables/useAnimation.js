import { ref, watch } from 'vue'

export function useAnimatedNumber(targetRef, duration = 500) {
  const displayValue = ref(0)
  let animationId = null

  watch(targetRef, (end) => {
    if (animationId) cancelAnimationFrame(animationId)
    const start = displayValue.value
    const target = parseInt(end) || 0
    if (start === target) return

    const startTime = performance.now()
    const animate = (currentTime) => {
      const elapsed = currentTime - startTime
      const progress = Math.min(elapsed / duration, 1)
      const ease = 1 - Math.pow(1 - progress, 4)
      displayValue.value = Math.floor(start + (target - start) * ease)
      if (progress < 1) {
        animationId = requestAnimationFrame(animate)
      }
    }
    animationId = requestAnimationFrame(animate)
  }, { immediate: true })

  return displayValue
}
