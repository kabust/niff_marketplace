<script setup>
import {ref} from "vue";

const props = defineProps({
    reversed: {
      type: Boolean,
      default: false
    }
})

const isReversed = ref(props.reversed);
</script>

<template>
  <div class="rollout-arrow" :class="{'reversed': isReversed}">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M6 9L12 15L18 9" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</template>

<style scoped>

</style>
