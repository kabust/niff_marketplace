<script setup>
import { RouterLink } from 'vue-router';
import Instagram from '@/assets/images/Instagram.svg'

defineProps({
  dark: {
    type: Boolean,
    default: true
  }
});
</script>


<template>
  <div class="instagram-link" :class="{ 'dark': dark }">
    <RouterLink to="/login">
      <Instagram /><span>@niff.wear</span>
    </RouterLink>
  </div>
</template>

<style scoped>
.instagram-link a {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  text-decoration: none;
  font-weight: 300;
  width: fit-content;
}

svg {
  width: 24px;
  height: 24px;
}

.instagram-link a,
.instagram-link svg :deep(path) {
  transition: var(--base-transition);
}

.instagram-link a:hover,
.instagram-link a:hover svg :deep(path) {
  color: var(--color-text-orange-hover);
  stroke: var(--color-text-orange-hover);
  cursor: pointer;
}

.instagram-link.dark a,
.instagram-link.dark svg :deep(path) {
  color: var(--color-text-white);
  stroke: var(--color-text-white);
}

.instagram-link.dark a:hover,
.instagram-link.dark a:hover svg :deep(path) {
  color: var(--color-text-orange-hover);
  stroke: var(--color-text-orange-hover);
  cursor: pointer;
}

</style>
