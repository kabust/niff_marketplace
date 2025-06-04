<script setup>
import { defineProps } from 'vue';
import ImageCard from './ImageCard.vue';

defineProps({
  title: {
    type: String,
    required: true
  },
  price: {
    type: Number,
    required: true
  },
  designer: {
    type: String,
    required: false,
  },
  src: {
    type: String,
    required: true,
  },
  bg: {
    type: String,
    required: false,
  },
});
</script>

<template>
  <ImageCard :src="src" :bg="bg">
    <div class="product-card">
      <div class="product-info">
        <p class="product-designer" v-if="designer">{{ designer }}</p>
        <h6 class="product-title">{{ title }}</h6>
        <h6 class="product-price">${{ price.toFixed(2) }}</h6>
      </div>
    </div>
  </ImageCard>
</template>

<style scoped>
.product-card {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 16px;
  border: var(--base-border-black);
  border-top: none;
  border-right: none;
}

.product-info {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.product-info p {
  font-size: 16px;
  line-height: 24px;
  color: var(--color-text-gray);
}

</style>
