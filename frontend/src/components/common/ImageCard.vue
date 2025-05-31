<script setup>
import { ref } from 'vue';

const props = defineProps({
  imgSrc: {
    type: String,
    required: true,
  },
  imgBgSrc: {
    type: String,
    required: false,
  }
})

const hover = ref(false)

</script>

<template>
  <div class="image-card" @mouseenter="hover = true" @mouseleave="hover = false">
    <img :src="imgSrc" alt="primary" class="card-image base-image" />
    <img :src="imgBgSrc" alt="hover" class="card-image hover-image" :class="{ 'opacity-100': hover, 'opacity-0': !hover }" />
  </div>
</template>

<style scoped>
.image-card {
  width: 360px;
  height: 326px;
  transition: opacity 0.2s ease-in-out;
}
.image-card img {
  object-fit: fill;
  height: 100%;
  width: 100%;
  border: 1px solid var(--color-text);
  border-top: none;
}

.image-card {
  position: relative;
  width: 100%;
  height: auto;
  overflow: hidden;
}
.card-image {
  width: 100%;
  height: auto;
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  transition: opacity 0.5s ease-in-out;
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
