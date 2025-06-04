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
  <div class="image-card" @mouseenter="hover = true" @mouseleave="hover = false">
    <img :src="src" alt="primary" class="card-image base-image" />
    <img :src="bg || src" alt="hover" class="card-image hover-image"
      :class="{ 'opacity-100': hover, 'opacity-0': !hover }" style="height: auto;" />
    <slot />
  </div>
</template>

<style scoped>
.image-card {
  width: 360px;
  height: 326px;
  transition: opacity 0.2s ease-in-out;
  position: relative;
  width: 100%;
  height: auto;
  overflow: hidden;
}

.image-card img {
  aspect-ratio: var(--default-image-aspect-ratio, 1 / 1);
  object-fit: cover;
  height: 100%;
  width: 100%;
  border: var(--base-border-black);
  border-right: none;
  border-top: none;
}

.card-image {
  width: 100%;
  height: auto;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  transition: var(--base-transition-ease-in-out);
}

.base-image {
  position: relative;
}

.hover-image {
  opacity: 0;
}

.image-card .opacity-100 {
  opacity: 100;
}

.image-card:hover {
  cursor: pointer;
}

.image-card:active {
  opacity: 0.5;
}
</style>
