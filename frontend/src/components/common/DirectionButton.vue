<script setup>
defineProps({
  direction: {
    type: String,
    default: 'next' // 'next' or 'prev'
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

</script>

<template>
  <button v-if="direction === 'prev'" class="prev" @click="$emit('prev')" :disabled="disabled">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M15 18L9 12L15 6" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>

  <button v-else-if="direction === 'next'" class="next" @click="$emit('next')" :disabled="disabled">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M9 18L15 12L9 6" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>
</template>

<style scoped>
button {
  height: 100%;
  aspect-ratio: 1 / 1;
  width: 100%;
  border: var(--base-border-black);
  border-right: none;
  background-color: transparent;
  cursor: pointer;
}

button:hover:disabled svg :deep(path) {
  stroke: var(--color-button-disabled);
}

button:hover:disabled {
  cursor: default;
}

button:disabled svg :deep(path) {
  stroke: var(--color-button-disabled);
}

button svg :deep(path) {
  transition: var(--base-transition);
}

@media (hover: hover) {
  button:hover svg :deep(path) {
    stroke: var(--color-text-orange-hover);
  }
}

button:active svg :deep(path) {
  stroke: var(--color-text-orange-active);
}
</style>