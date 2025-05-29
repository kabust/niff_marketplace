<script setup>
import Arrow from '@/assets/images/Arrow.svg'

defineProps(['buttonText', 'arrow'])
</script>


<template>
  <button v-if="arrow">
    {{ buttonText }} <Arrow/>
  </button>
  <button v-else>
    {{ buttonText }}
  </button>
</template>


<style>
button {
  color: var(--color-text-white);
  background-color: var(--color-text-orange-hover);
  width: 326px;
  height: 56px;
  border: 0;
  font-weight: 700;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: color 0.3s ease, stroke 0.3s ease, background-color 0.3s ease;
}

button svg path {
  stroke: var(--color-text-white);
  transition: color 0.3s ease, stroke 0.3s ease, background-color 0.3s ease;
}

button:hover, button:hover svg path {
  color: var(--color-text);
  stroke: var(--color-text);
  cursor: pointer;
}

button:active, button:active svg path {
  background-color: var(--color-text-orange-active);
  color: var(--color-text);
  stroke: var(--color-text);
}

</style>
