<script setup>
import { ref, computed, watch } from 'vue';

const props = defineProps({
  minValue: {
    type: Number,
    required: true
  },
  maxValue: {
    type: Number,
    required: true
  },
});

const price = ref({ min: props.minValue, max: props.maxValue });

// Ensure min does not exceed max and vice versa
watch(() => price.value.min, (val) => {
  if (val > price.value.max) price.value.min = price.value.max;
  if (val < props.minValue) price.value.min = props.minValue;
});
watch(() => price.value.max, (val) => {
  if (val < price.value.min) price.value.max = price.value.min;
  if (val > props.maxValue) price.value.max = props.maxValue;
});

// Compute the background gradient for the range track
const rangeStyle = computed(() => {
  const min = props.minValue;
  const max = props.maxValue;
  const minPercent = ((price.value.min - min) / (max - min)) * 100;
  const maxPercent = ((price.value.max - min) / (max - min)) * 100;
  return {
    background: `linear-gradient(to right, #e0e0e0 0%, #e0e0e0 ${minPercent}%, var(--color-text-orange-active) ${minPercent}%, var(--color-text-orange-active) ${maxPercent}%, #e0e0e0 ${maxPercent}%, #e0e0e0 100%)`
  };
});
</script>


<template>
  <div class="price-inputs">
    
    <div class="slider">
      <input 
        type="range" 
        :min="props.minValue" 
        :max="props.maxValue" 
        v-model.number="price.min" 
        :style="rangeStyle"
        step="10"
        @input="e => { if (price.min > price.max - 100) price.min = price.max - 100 }"
        />
      <input 
        type="range" 
        :min="props.minValue" 
        :max="props.maxValue" 
        v-model.number="price.max" 
        :style="rangeStyle"
        step="10"
        @input="e => { if (price.max < price.min + 100) price.max = price.min + 100 }"
        />
    </div>
    
    <div class="slider-values">
      <span class="slider-value">$<input type="number" v-model.number="price.min" :min="props.minValue" :max="price.max" />
      </span>
      
      <span class="slider-value">$<input type="number" v-model.number="price.max" :min="price.min" :max="props.maxValue" />
      </span>
    </div>
  
  </div>
</template>


<style scoped>
.slider {
  display: grid;
  flex-direction: column;
  width: 100%;
}

.slider > * {
  grid-column-start: 1;
  grid-row-start: 1;
}

.slider-values {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
  width: 100%;
}

.slider-values input[type="number"] {
  width: 75px;
  padding: 16px 16px 16px 0;
  text-align: center;
  border: none;
  border-radius: 0;
}

.slider-values input[type="number"]:focus {
  outline: none;
}

.slider-value {
  border: 1px solid var(--color-text);
  border-radius: 0;
  padding-left: 16px;
}

.price-inputs {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  margin-top: 10px;
}

input[type=number]::-webkit-outer-spin-button,
input[type=number]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type=number] {
  -moz-appearance: textfield;
}

input[type="range"] {
  height: 1px;
  cursor: ew-resize;
  display: inline-grid;
}

input[type="range"]::-webkit-slider-thumb {
  width: 24px;
  height: 24px;
  border-radius: 0%;
  background: var(--color-text-orange-hover);
  cursor: pointer;
  border: none;
}

input[type="range"]::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 0%;
  background: var(--color-text-orange-hover);
  cursor: pointer;
  border: none;
}

input[type="range"]::-ms-thumb {
  width: 24px;
  height: 24px;
  border-radius: 0%;
  background: var(--color-text-orange-hover);
  cursor: pointer;
  border: none;
}
</style>
