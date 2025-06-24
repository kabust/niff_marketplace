<script setup>
import { ref } from 'vue'
import RolloutArrow from "@/components/common/RolloutArrow.vue";

const props = defineProps({
  show: Boolean
})

const emit = defineEmits(['close'])

const selectedCategories = ref([])
const categories = ['T-Shirts', 'Hoodies', 'Pants', 'Accessories']
const price = ref({ min: 300, max: 749 })

const sections = ref({
  category: true,
  price: true,
})

const toggle = (section) => {
  sections.value[section] = !sections.value[section]
}

const close = () => emit('close')
</script>

<template>
  <div v-if="show" class="modal-backdrop" @click.self="close">
    <div class="filter-modal">
      <div class="filter-header">
        <h4 class="modal-title">Filters</h4>
        <button class="close-btn" @click="close">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M18 6L6 18" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M6 6L18 18" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>

      <!-- Category Filter -->
      <div class="accordion">
        <div class="accordion-header-container">
          <h6 class="accordion-header" @click="toggle('category')">Category</h6>
          <RolloutArrow :reversed="sections.category"/>
        </div>
        <div v-if="sections.category" class="accordion-content active">
          <label v-for="item in categories" :key="item" class="checkbox-label">
            <input type="checkbox" v-model="selectedCategories" :value="item" />
            {{ item }}
          </label>
        </div>
        <div v-else class="accordion-content hidden">
          <label v-for="item in categories" :key="item" class="checkbox-label">
            <input type="checkbox" v-model="selectedCategories" :value="item" />
            {{ item }}
          </label>
        </div>
      </div>

      <!-- Price Filter -->
      <div class="accordion">
        <div class="accordion-header-container">
          <h6 class="accordion-header" @click="toggle('price')">Price</h6>
          <RolloutArrow/>
        </div>
        <div v-show="sections.price" class="accordion-content">
          <div class="price-inputs">
            <input type="number" v-model="price.min" />
            <input type="range" min="0" max="1000" v-model="price.min" />
            <input type="range" min="0" max="1000" v-model="price.max" />
            <input type="number" v-model="price.max" />
          </div>
        </div>
      </div>

      <!-- Add more filters below -->
    </div>
  </div>
</template>

<style scoped>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  z-index: 50;
  display: flex;
  justify-content: flex-end;
}

.filter-modal {
  width: 600px;
  max-width: 90%;
  background: #fff;
  height: 100%;
  overflow-y: auto;
  position: relative;
  animation: slide-in 0.3s ease forwards;
  z-index: 1;
}

@keyframes slide-in {
  from {
    transform: translateX(100%);
  }
  to {
    transform: translateX(0);
  }
}

.filter-header {
  height: 100px;
  display: flex;
  justify-content: center;
}

.close-btn {
  position: absolute;
  right: 40px;
  top: 40px;
  background: none;
  border: none;
  cursor: pointer;
}

.modal-title {
  margin: auto;
}

.accordion {
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.accordion-header-container {
  display: flex;
}

.accordion, .filter-header {
  border-bottom: var(--base-border-black);
}

.accordion-header {
  font-weight: bold;
  background: none;
  border: none;
  width: 100%;
  text-align: left;
  cursor: pointer;
}

.checkbox-label {
  display: block;
  margin: 5px 0;
  font-size: 14px;
}

.price-inputs {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  margin-top: 10px;
}

.price-inputs input[type="number"] {
  width: 60px;
  padding: 4px;
}

.accordion-content {
  transition: var(--base-transition);
}

.accordion-content.hidden {
  display: none;
}

.accordion-content.active{
  display: block;
  animation: slide-in-bottom 0.3s ease forwards;
}

@keyframes slide-in-bottom {
  from {
    transform: translateY(-50%);
  }
  to {
    transform: translateY(0);
  }
}
</style>
