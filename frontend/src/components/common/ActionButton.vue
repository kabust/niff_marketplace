<script setup>
import Arrow from '@/assets/images/Arrow.svg'

defineProps({
  buttonText: {
    type: String,
    required: true,
  },
  arrow: {
    type: Boolean,
    required: false,
  }
})

</script>


<template>
  <button v-if="arrow">
    {{ buttonText }} <Arrow/>
  </button>
  <button v-else>
    {{ buttonText }}
  </button>
</template>


<style scoped>
button {
  color: var(--color-text-white);
  background-color: var(--color-text-orange-hover);
  width: 100%;
  height: 56px;
  border: 0;
  font-weight: 700;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: var(--base-transition);
}

button svg :deep(path) {
  stroke: var(--color-text-white);
  transition: var(--base-transition);
}

button:hover, button:hover svg :deep(path) {
  color: var(--color-text);
  stroke: var(--color-text);
  cursor: pointer;
}

button:active, button:active svg :deep(path) {
  background-color: var(--color-text-orange-active);
  color: var(--color-text);
  stroke: var(--color-text);
}

</style>
