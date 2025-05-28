<script setup>
import { RouterLink, RouterView } from 'vue-router'

import Instagram from '@/assets/images/Instagram.svg'
import Search from '@/assets/images/Search.svg'
import Cart from '@/assets/images/Cart.svg'
import Profile from '@/assets/images/Profile.svg'


function search() {
  console.log("test");
}
</script>

<template>
  <header>
    <nav>
      <span class="info">
        <RouterLink to="/">Shop</RouterLink>
        <RouterLink to="/login">Become a Seller</RouterLink>
        <RouterLink to="/login">Contact Us</RouterLink>
      </span>
      <span class="inst">
        <RouterLink to="/login">
          <Instagram/>@niff.wear
        </RouterLink>
      </span>
      <span class="logo">
        <RouterLink to="/"><img class="logo" src="./assets/images/logo.svg" width="72px" height="24px" /></RouterLink>
      </span>
      <span class="search">
        <Search @click="search" class="search-icon" />
        <input type="search">
      </span>
      <span class="user">
        <RouterLink to="/login"><Cart/></RouterLink>
        <RouterLink to="/login"><Profile/></RouterLink>
      </span>
    </nav>

  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  width: 100vw;
  font-size: 16px;
  margin-top: 0;
  display: flex;
  border: 1px solid black;
  border-top: 0;
}

nav a {
  text-decoration: underline;
  color: var(--color-text);
  transition: 0.4s;
  padding: 3px;
}

nav a, nav svg :deep(path) {
    transition: color 0.3s ease, stroke 0.3s ease;
}

@media (hover: hover) {
nav a:hover, svg:hover :deep(path) {
    color: var(--color-text-hover);
    stroke: var(--color-text-hover);
  }
}

@media (hover: hover) {
nav .inst a:hover svg :deep(path) {
    color: var(--color-text-hover);
    stroke: var(--color-text-hover);
  }
}

@media (hover: hover) {
nav a:active, svg:active :deep(path) {
    color: var(--color-text-muted);
    stroke: var(--color-text-muted);
  }
}

@media (hover: hover) {
nav .inst a:active svg :deep(path) {
    color: var(--color-text-muted);
    stroke: var(--color-text-muted);
  }
}

@media (hover: hover) {
nav a:active {
    color: var(--color-text-muted);
  }
}

nav span {
  display: flex;
  flex: 1;

  height: 72px;
  justify-content: center;
  align-items: center;
  padding: 24px 54.5px;
  border-right: 1px solid black;
  gap: 24px;
}

nav span:last-child {
  border-right: none;
}

nav .info   { flex: 0 0 30%; }
nav .inst, .inst a {display: flex; flex: 0 0 15%; gap: 8px;}
nav .logo   { flex: 0 0 10%;}
nav .search { flex: 0 0 30%; gap: 8px;}
nav .user  { flex: 0 0 15%; }
nav .search-icon {cursor: pointer};

</style>
