<script setup>
import { ref } from 'vue';
import Arrow from '@/assets/images/Arrow.svg';
import FilterModal from "@/components/base/FilterModal.vue";

defineProps({
  headerTitle: {
    type: String,
    default: 'All Products',
  },
  itemsAmount: {
    type: Number,
    default: 0,
  }
});

const showFilters = ref(false);
</script>

<template>
  <div class="shop-header">
    <h4>{{ headerTitle }}<sup>({{ itemsAmount }})</sup></h4>
    <button @click="showFilters = true">Filters  <Arrow/></button>
    <FilterModal :show="showFilters" @close="showFilters = false" />
  </div>
</template>

<style scoped>
.shop-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 28px 32px;
}

.shop-header sup {
  font-size: 24px;
  color: var(--color-text-gray);
}

button {
  background-color: var(--color-background);
  color: var(--color-text);
  border: var(--base-border-black);
  padding: 16px 64px;
  font-size: 16px;
  font-weight: 700;
  display: flex;
  gap: 8px;
  align-items: center;
}

button, button svg :deep(path) {
  transition: var(--base-transition);
}

button:hover, button:hover svg :deep(path) {
  color: var(--color-text-orange-hover);
  border-color: var(--color-text-orange-hover);
  stroke: var(--color-text-orange-hover);
  cursor: pointer;
}

button:active, button:active svg :deep(path) {
  color: var(--color-text-orange-active);
  border-color: var(--color-text-orange-active);
  stroke: var(--color-text-orange-active);
}

</style>
