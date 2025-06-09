<script setup>
import { ref } from 'vue';

defineProps({
  src: {
    type: String,
    required: true,
  },
  bg: {
    type: String,
    required: false,
  }
});

const hover = ref(false);

</script>

<template>
  <div class="image-card">
    <div class="image-container" @mouseenter="hover = true" @mouseleave="hover = false">
      <img :src="src" alt="primary" class="card-image base-image" />
      <img :src="bg || src" alt="hover" class="card-image hover-image"
        :class="{ 'opacity-100': hover, 'opacity-0': !hover }" />
    </div>
    <slot />
  </div>
</template>

<style scoped>
.image-card {
  width: 100%;
  display: flex;
  flex-direction: column;
  transition: 0.2s ease-in-out;
}

.image-card:hover {
  cursor: pointer;
}

.image-card:active {
  opacity: 0.5;
}

.image-container {
  width: 100%;
  position: relative;
  aspect-ratio: var(--default-image-aspect-ratio, 1 / 1);
}

.card-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border: var(--base-border-black);
  border-right: none;
  border-top: none;
  transition: opacity 0.2s ease-in-out;
}

.hover-image {
  opacity: 0;
}

.hover-image.opacity-100 {
  opacity: 1;
}

.hover-image.opacity-0 {
  opacity: 0;
}
</style>
