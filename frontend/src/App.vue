<script setup>
import { RouterView } from 'vue-router'

import NavComponent from '@/components/base/NavComponent.vue'
import FooterComponent from '@/components/base/FooterComponent.vue';
</script>

<template>
  <NavComponent/>
  <RouterView/>
  <FooterComponent/>
</template>
