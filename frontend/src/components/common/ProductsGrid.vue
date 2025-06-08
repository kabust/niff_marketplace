<script setup>
const props = defineProps({
  components: {
    type: Array,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true
  },
  limit: {
    type: Number,
    required: true
  }
});

let components = props.components.map((component) => {
  return {
    name: component.name,
    props: {
      ...component.props,
      class: 'grid-item-component'
    }
  };
});
</script>

<template>
  <div class="products-grid-cards">
    <component
      v-for="(component, index) in components"
      :key="index"
      :is="component.name"
      v-bind="component.props"
    />
  </div>
</template>

<style scoped>
.products-grid-cards {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  border-top: var(--base-border-black);
}
</style>
