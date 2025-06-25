<script setup>
import { ref } from 'vue';
import AccordionComponent from "@/components/common/AccordionComponent.vue";
import SliderComponent from "@/components/common/SliderComponent.vue";

defineProps({
  show: Boolean
})

const emit = defineEmits(['close'])

const categories = ['T-Shirts', 'Hoodies', 'Pants', 'Accessories']
const sizes = ['XS', 'S', 'M', 'L', 'XL']
const colors = ['White', 'Black', 'Add more from api']
const sortBy = ['Price: Low to High', 'Price: High to Low', 'Newest First', 'Oldest First']

const minValue = 120;
const maxValue = 5300;

const selectedCategories = ref([])
const selectedSizes = ref([])
const selectedColors = ref([])
const selectedSortBy = ref()

const sections = ref({
  category: false,
  price: false,
  size: false,
  color: false,
  sortBy: false
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
            <svg class="close-btn" @click="close" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6L6 18" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M6 6L18 18" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>

          <!-- Category Filter -->
          <AccordionComponent
            title="Categories"
            :is-active="sections.category"
            @toggle="toggle('category')"
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
            @toggle="toggle('price')"
          >
            <div class="price-inputs">
              <SliderComponent :minValue="minValue" :maxValue="maxValue"/>
            </div>
          </AccordionComponent>

          <!-- Size Filter -->
          <AccordionComponent
            title="Size"
            :is-active="sections.size"
            @toggle="toggle('size')"
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
            @toggle="toggle('color')"
          >
            <label v-for="item in colors" :key="item" class="checkbox-label">
              <input type="checkbox" v-model="selectedColors" :value="item" />
              {{ item }}
            </label>
          </AccordionComponent>

          <!-- Sort By Filter -->
          <AccordionComponent
            title="Sort By"
            :is-active="sections.sortBy"
            @toggle="toggle('sortBy')"
          >
            <label v-for="item in sortBy" :key="item" class="checkbox-label">
              <input type="radio" v-model="selectedSortBy" :value="item" />
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
  right: 24px;
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
