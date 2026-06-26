<template>
  <div class="flex justify-between items-center mt-10 p-6 bg-white rounded-xl shadow border border-gray-100">
    <button
      @click="$emit('prev')"
      :disabled="currentStep === 1"
      class="flex items-center gap-2 px-6 py-3 bg-gray-100 rounded-lg text-secondary uppercase font-bold text-xs hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
    >
      <IconChevronLeft class="w-4 h-4" /> Previous
    </button>

    <span class="text-xs font-bold text-secondary tracking-[0.2em]">
      PHASE {{ currentStep }} / {{ totalSteps }}
    </span>

    <button
      v-if="currentStep < totalSteps"
      @click="$emit('next')"
      class="flex items-center gap-2 px-6 py-3 bg-primary text-white rounded-lg uppercase font-bold text-xs hover:bg-gray-800 transition-colors shadow-lg shadow-gray-200"
    >
      Next <IconChevronRight class="w-4 h-4" />
    </button>
  </div>
</template>

<script setup>
import IconChevronLeft from './icons/IconChevronLeft.vue'
import IconChevronRight from './icons/IconChevronRight.vue'

defineProps({
  currentStep: { type: Number, required: true },
  totalSteps: { type: Number, required: true },
})

defineEmits(['prev', 'next'])
</script>
