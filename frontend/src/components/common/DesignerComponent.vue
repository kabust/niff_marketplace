<script setup>
defineProps({
  src: {
    type: String,
    required: true
  },
  designerName: {
    type: String,
    required: true
  },
  widthRelative: {
    type: Number,
    default: 100
  }
});
</script>

<template>
  <div class="designer-component">
    <span class="image-label" :style="{ right: 100 - widthRelative }">{{ designerName }}</span>
    <img :src="src" alt="Designer Image" :width="widthRelative + '%'" />
  </div>
</template>

<style scoped>
.image-label {
  position: absolute;
  background: var(--color-background);
  padding: 16px 32px;
  font-weight: 700;
  border-bottom: var(--base-border-black);
  border-left: var(--base-border-black);
}

.designer-component {
  position: relative;
  width: 100%;
  display: flex;
}

.designer-component img {
  object-fit: cover;
  object-position: center;
  aspect-ratio: 720 / 645;
  border: var(--base-border-black);
  border-top: none;
}
</style>
