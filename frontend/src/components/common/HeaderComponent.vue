<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
});
</script>

<template>
  <div class="header">
    <h3>{{ title }}</h3>
  </div>
</template>

<style scoped>
.header {
  display: flex;
  align-self: start;
  align-items: center;
  height: var(--header-height);
  border: var(--base-border-black);
}

.header h3 {
  font-size: 32px;
  font-weight: 700;
  padding: 32px 24px;
}
</style>
