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
    <div class="accordion-header-container">
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
  padding: 40px 32px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}

.accordion-header-container {
  display: flex;
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
  transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1), display 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.accordion-content.active {
  max-height: 500px; /* adjust as needed for content */
  display: block;
  transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), display 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
