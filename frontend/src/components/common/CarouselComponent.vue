<script setup>
import { ref } from 'vue';
import DirectionButton from './DirectionButton.vue';

const props = defineProps({
  components: {
    type: Array,
    required: true,
  },
  carouselHeader: {
    type: String,
    required: true,
  },
  rowSize: {
    type: Number,
    default: 4, // Default to showing 4 items at a time
  },
  itemsPerClick: {
    type: Number,
    default: 1, // Default to moving 1 item at a time
  }
});

let components = props.components.map((component) => {
  return {
    name: component.name,
    props: {
      ...component.props,
      class: 'carousel-item-component'
    }
  };
});

let sliceStart = 0;
let sliceEnd = props.rowSize;

let currentIndex = ref(0);
let prevButtonDisabled = ref(sliceStart === 0);
let nextButtonDisabled = ref(sliceEnd >= components.length);

function updateComponentsSlice(direction) {
  if (direction === 'next') {
    sliceStart += props.itemsPerClick;
    sliceEnd += props.itemsPerClick;
    currentIndex.value += props.itemsPerClick;
  } else if (direction === 'prev') {
    sliceStart -= props.itemsPerClick;
    sliceEnd -= props.itemsPerClick;
    currentIndex.value -= props.itemsPerClick;
  }

  if (sliceStart < 0) {
    sliceStart = 0;
    sliceEnd = props.rowSize;
  }
  if (sliceEnd > components.length) {
    sliceEnd = components.length;
    sliceStart = Math.max(0, sliceEnd - props.rowSize);
  }

  prevButtonDisabled.value = sliceStart === 0;
  nextButtonDisabled.value = sliceEnd >= components.length;
}

</script>


<template>
  <div class="carousel-container" :style="{ '--row-size': rowSize }">
    <div class="header">
      <h3>{{carouselHeader}}</h3>
      <div class="switcher">
        <DirectionButton direction="prev" @prev="updateComponentsSlice('prev')" :disabled="prevButtonDisabled" />
        <DirectionButton direction="next" @next="updateComponentsSlice('next')" :disabled="nextButtonDisabled" />
      </div>
    </div>
    
    <ul class="carousel" 
    :style="{
      transform: `translateX(-${currentIndex * (100 / rowSize)}%)`,
    }">
      <li v-for="(component, index) in components" :key="index" class="carousel-item">
          <component :is="component.name" v-bind="component.props" />
      </li>
    </ul>
  </div>
</template>


<style scoped>
.carousel-container {
  overflow: hidden;
  width: 100%;
}

.carousel-container ul {
  padding: 0;
  display: flex;
  list-style: none;
  width: 100%;
  transform-style: preserve-3d;
  transition: transform 0.5s ease;
}

.carousel-item {
  flex: 0 0 calc(100% / var(--row-size, 4)); /* Uses CSS variable for dynamic sizing */
  max-width: calc(100% / var(--row-size, 4));
}

.carousel-container .header {
  height: var(--header-height);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
  padding-right: 0;
  border: var(--base-border-black);
  border-left: none;
  border-right: none;
}

.carousel-container .header h3 {
  font-size: 32px;
  font-weight: 700;
}

.carousel-container .switcher {
  display: flex;
  height: var(--header-height);
}
</style>
