<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Arrow from '@/assets/images/Arrow.svg'

const route = useRoute();
const router = useRouter();

defineProps({
  totalPages: {
    type: Number,
    required: true
  }
});

const currentPage = ref(Number(route.query.page) || 1);

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    router.push({ query: { ...route.query, page: currentPage.value }});
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages) {
    currentPage.value++;
    router.push({ query: { ...route.query, page: currentPage.value }});
  }
};
</script>


<template>
  <div class="pagination-component">
    <div class="pagination-controls">
      <button @click="prevPage" :disabled="currentPage === 1"><Arrow class="arrow-left"/></button>
      <button class="current">{{ currentPage }}</button>
      <button>{{ currentPage + 1 }}</button>
      <button>{{ currentPage + 2 }}</button>
      <button @click="nextPage" :disabled="currentPage === totalPages"><Arrow class="arrow-right"/></button>
    </div>
  </div>
</template>

<style scoped>
.pagination-component {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px 0;
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

button {
  width: 56px;
  background-color: var(--color-background);
  color: var(--color-text);
  border: var(--base-border-black);
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  aspect-ratio: 1 / 1;
}

button, svg :deep(path) {
  transition: var(--base-transition);
}

button:not(.current):not(:disabled):hover, 
button:not(.current):not(:disabled):hover svg :deep(path) 
{
  stroke: var(--color-text-orange-hover);
  color: var(--color-text-orange-hover);
  border-color: var(--color-text-orange-hover);
}

button:not(.current):not(:disabled):active, 
button:not(.current):not(:disabled):active svg :deep(path) 
{
  stroke: var(--color-text-orange-active);
  color: var(--color-text-orange-active);
  border-color: var(--color-text-orange-active);
}

.arrow-left {
  transform: rotate(180deg);
}

.arrow-right {
  transform: rotate(0deg);
}

button:disabled {
  opacity: 0.5;
  cursor: default;
  border-color: var(--color-text-gray);
}

.current {
  background-color: var(--color-text-orange-hover);
  color: var(--color-text-white);
  border: none;
  font-weight: 700;
  width: 56px;
  aspect-ratio: 1 / 1;
}

</style>
