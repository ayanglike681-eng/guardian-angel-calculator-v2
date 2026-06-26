<template>
  <div class="w-full bg-gray-200 rounded-full h-2">
    <div class="bg-primary h-2 rounded-full transition-all duration-500" :style="{ width: progress + '%' }"></div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentStep: { type: Number, required: true },
  totalSteps: { type: Number, required: true },
})

const progress = computed(() => Math.min(100, ((props.currentStep) / props.totalSteps) * 100))
</script>
