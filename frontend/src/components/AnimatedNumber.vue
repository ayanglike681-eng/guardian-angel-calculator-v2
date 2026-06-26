<template>
  <span>{{ displayValue }}</span>
</template>

<script setup>
import { toRef } from 'vue'
import { useAnimatedNumber } from '../composables/useAnimation'

const props = defineProps({ value: { type: Number, default: 0 } })

const displayValue = useAnimatedNumber(toRef(props, 'value'), 500)
</script>
