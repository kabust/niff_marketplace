<script setup>
import Arrow from '@/assets/images/Arrow.svg'
import { RouterLink } from 'vue-router';

defineProps({
  buttonText: {
    type: String,
    required: true,
  },
  arrow: {
    type: Boolean,
    required: false,
  },
  to: {
    type: [String, Object],
    required: false,
    default: null
  }
})
</script>

<template>
  <RouterLink v-if="to" :to="to" class="button-link">
    {{ buttonText }} <Arrow v-if="arrow"/>
  </RouterLink>
  <button v-else>
    {{ buttonText }} <Arrow v-if="arrow"/>
  </button>
</template>

<style scoped>
button, .button-link {
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
  text-decoration: none;
}

button svg :deep(path), .button-link svg :deep(path) {
  stroke: var(--color-text-white);
  transition: var(--base-transition);
}

button:hover, button:hover svg :deep(path), .button-link:hover, .button-link:hover svg :deep(path) {
  color: var(--color-text);
  stroke: var(--color-text);
  cursor: pointer;
}

button:active, button:active svg :deep(path), .button-link:active, .button-link:active svg :deep(path) {
  background-color: var(--color-text-orange-active);
  color: var(--color-text);
  stroke: var(--color-text);
}

</style>
