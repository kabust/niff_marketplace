<script setup>
import RolloutArrow from "@/components/common/RolloutArrow.vue";

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  isActive: {
    type: Boolean,
    default: false
  }
})
</script>


<template>
  <div class="accordion">
    <div class="accordion-header-container" @click="$emit('toggle')">
      <h6 class="accordion-header">{{ title }}</h6>
      <RolloutArrow :reversed="props.isActive"/>
    </div>
    <div :class="['accordion-content', { active: props.isActive }]" >
      <slot></slot>
    </div>
  </div>
</template>


<style scoped>
.accordion {
  display: flex;
  flex-direction: column;
  cursor: pointer;
}

.accordion h6 {
  margin: 24px;
}

.accordion-header-container {
  display: flex;
  align-items: center;
}

.accordion-header {
  font-weight: bold;
  background: none;
  border: none;
  width: 100%;
  text-align: left;
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  margin: 0 24px;
  position: relative;
  transition: max-height 0.3s cubic-bezier(1,0,0,1);
}
.accordion-content::after {
  content: "";
  display: block;
  height: 0;
  transition: height 0.3s cubic-bezier(.86,0,.07,1);
}
.accordion-content.active {
  max-height: 500px; /* adjust as needed for content */
  display: block;
}
.accordion-content.active::after {
  height: 24px; /* bottom space when open */
}
</style>
