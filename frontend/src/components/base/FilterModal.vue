<script setup>
import { ref } from 'vue';
import AccordionComponent from "@/components/common/AccordionComponent.vue";
import RolloutArrow from "@/components/common/RolloutArrow.vue";

defineProps({
  show: Boolean
})

const emit = defineEmits(['close'])

const categories = ['T-Shirts', 'Hoodies', 'Pants', 'Accessories']
const price = ref({ min: 300, max: 749 })
const sizes = ['XS', 'S', 'M', 'L', 'XL']
const colors = ['White', 'Black', 'Add more from api']

const selectedCategories = ref([])
const selectedSizes = ref([])
const selectedColors = ref([])

const sections = ref({
  category: false,
  price: false,
  size: false,
  color: false
})

const toggle = (section) => {
  sections.value[section] = !sections.value[section]
}

const close = () => emit('close')
</script>

<template>
  <transition name="fade">
    <div v-if="show" class="modal-backdrop" @click.self="close">
      <transition name="slide" appear>
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
          <AccordionComponent
            title="Categories"
            :is-active="sections.category"
            @click="toggle('category')"
          >
            <label v-for="item in categories" :key="item" class="checkbox-label">
              <input type="checkbox" v-model="selectedCategories" :value="item" />
              {{ item }}
            </label>
          </AccordionComponent>

          <!-- Price Filter -->
          <AccordionComponent
            title="Price"
            :is-active="sections.price"
            @click="toggle('price')"
          >
            <div class="price-inputs">
              <input type="number" v-model="price.min" />
              <input type="range" min="0" max="1000" v-model="price.min" />
              <input type="range" min="0" max="1000" v-model="price.max" />
              <input type="number" v-model="price.max" />
            </div>
          </AccordionComponent>

          <!-- Size Filter -->
          <AccordionComponent
            title="Size"
            :is-active="sections.size"
            @click="toggle('size')"
          >
            <label v-for="item in sizes" :key="item" class="checkbox-label">
              <input type="checkbox" v-model="selectedSizes" :value="item" />
              {{ item }}
            </label>
          </AccordionComponent>

          <!-- Color Filter -->
          <AccordionComponent
            title="Color"
            :is-active="sections.color"
            @click="toggle('color')"
          >
            <label v-for="item in colors" :key="item" class="checkbox-label">
              <input type="checkbox" v-model="selectedColors" :value="item" />
              {{ item }}
            </label>
          </AccordionComponent>
        </div>
      </transition>
    </div>
  </transition>
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
  z-index: 1;
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

.accordion, .filter-header {
  border-bottom: var(--base-border-black);
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

/* transition classes for modal */
.slide-enter-active, .slide-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-enter-from, .slide-leave-to {
  transform: translateX(100%);
  opacity: 0;
}

.slide-enter-to, .slide-leave-from {
  transform: translateX(0);
  opacity: 1;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.fade-enter-to, .fade-leave-from {
  opacity: 1;
}


</style>
