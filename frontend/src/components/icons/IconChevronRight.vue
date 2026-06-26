<template>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="className">
    <polyline points="9 18 15 12 9 6" />
  </svg>
</template>

<script setup>
defineProps({ className: { type: String, default: 'w-5 h-5' } })
</script>
