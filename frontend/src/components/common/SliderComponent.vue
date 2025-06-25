<script setup>
import { ref } from 'vue';

const props = defineProps({
  minValue: {
    type: Number,
    required: true
  },
  maxValue: {
    type: Number,
    required: true
  },
})

const price = ref({ min: props.minValue, max: props.maxValue })

const getRangeStyle = (value, min, max, isReversed = false) => {
  const percent = ((value - min) / (max - min)) * 100;
  if (isReversed) {
    return {
      background: `linear-gradient(to right, #e0e0e0 0%, #e0e0e0 ${percent}%, var(--color-text-orange-active) ${percent}%, var(--color-text-orange-active) 100%)`,
    } 
  } else {
    return {
      background: `linear-gradient(to right, var(--color-text-orange-active) 0%, var(--color-text-orange-active) ${percent}%, #e0e0e0 ${percent}%, #e0e0e0 100%)`,
    } 
  }
}
</script>


<template>
    <div class="slider">
      <input 
        type="range" 
        :min="props.minValue" 
        :max="props.maxValue / 2" 
        v-model="price.min" 
        :style="getRangeStyle(price.min, props.minValue, props.maxValue / 2, true)"/>
      <input 
        type="range" 
        :min="props.maxValue / 2 + 1" 
        :max="props.maxValue" 
        v-model="price.max" 
        :style="getRangeStyle(price.max, props.maxValue / 2 + 1, props.maxValue)"/>    
    </div>
    <div class="slider-values">
      <input type="number" v-model="price.min" />
      <input type="number" v-model="price.max" />
    </div>
</template>


<style scoped>
.slider {
  display: flex;
  flex-direction: column;
}

input[type="number"] {
  width: 60px;
  padding: 4px;
}

input[type="range"] {
  height: 1px;
  cursor: ew-resize;
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
