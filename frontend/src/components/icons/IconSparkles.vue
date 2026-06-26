<template>
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" :class="className">
    <path d="M12 3v1M12 21v1M4.2 11.2l1M18.8 11.2l1M6 17l.5-.5M17.5 6.5l.5-.5M7 7l.5.5M16 16l.5.5M2 22l1-1M22 2l-1 1" />
  </svg>
</template>

<script setup>
defineProps({ className: { type: String, default: 'w-5 h-5' } })
</script>
