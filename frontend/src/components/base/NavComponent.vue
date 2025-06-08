<script setup>
import { RouterLink } from 'vue-router'

import Search from '@/assets/images/Search.svg'
import Cart from '@/assets/images/Cart.svg'
import Profile from '@/assets/images/Profile.svg'
import LogoBlack from '../common/LogoBlack.vue'
import InstagramLink from '../common/InstagramLink.vue'

function search() {
  console.log("test");
}
</script>

<template>
  <header>
    <nav>
      <span class="info">
        <RouterLink to="/shop">Shop</RouterLink>
        <RouterLink to="/login">Become a Seller</RouterLink>
        <RouterLink to="/login">Contact Us</RouterLink>
      </span>
      <span class="inst">
        <InstagramLink :dark="false"/>
      </span>
      <span class="logo">
        <LogoBlack/>
      </span>
      <span class="search">
        <Search />
        <input @input="search" type="search" placeholder="Search">
      </span>
      <span class="user" style="gap: 24px;">
        <RouterLink to="/login"><Cart/>Cart</RouterLink>
        <RouterLink to="/login"><Profile/>Profile</RouterLink>
      </span>
    </nav>

  </header>

</template>

<style scoped>
header {
  max-height: 72px;
  position: relative;
  z-index: 1;
}

nav {
  width: 100vw;
  font-size: 16px;
  margin-top: 0;
  display: grid;
  border: var(--base-border-black);
  border-right: none;
  border-left: none;
  border-top: 0;
  grid-template-columns: 1fr 0.5fr 0.3fr 0.9fr 0.6fr;
}

nav a {
  text-decoration: underline;
  color: var(--color-text);
  transition: 0.4s;
  padding: 3px;
}

nav a, nav svg :deep(path) {
  transition: var(--base-transition);
}

@media (hover: hover) {
nav a:hover, svg:hover :deep(path) {
    color: var(--color-text-orange-hover);
    stroke: var(--color-text-orange-hover);
  }
}

@media (hover: hover) {
nav a:hover svg :deep(path) {
    color: var(--color-text-orange-hover);
    stroke: var(--color-text-orange-hover);
  }
}

@media (hover: hover) {
nav a:active, svg:active :deep(path) {
    color: var(--color-text-orange-active);
    stroke: var(--color-text-orange-active);
  }
}

@media (hover: hover) {
nav a:active svg :deep(path) {
    color: var(--color-text-orange-active);
    stroke: var(--color-text-orange-active);
  }
}

@media (hover: hover) {
nav a:active {
    color: var(--color-text-orange-active);
  }
}

nav span {
  display: flex;
  flex: 1;

  height: 72px;
  justify-content: center;
  align-items: center;
  padding: 24px 54.5px;
  border-right: var(--base-border-black);
  gap: 24px;
}

nav .search {
  justify-content: left;
  align-items: end;
}

nav .search input {
  border: none;
  transition: all 0.3s ease;
  font-size: 16px;
  background: none;
  width: 100%;
}

nav .search input::placeholder {
  transition: var(--base-transition);
}

nav .search input::placeholder {
  color: var(--color-text-gray);
  font-size: 16px;
}

nav .search input:hover::placeholder {
  color: var(--color-text-orange-hover);
}

nav .search input:focus-visible {
  outline: none;
}

nav span:last-child {
  border-right: none;
}

nav .inst, .inst a {display: flex; flex: 0 0 15%; gap: 8px;}
nav .search { gap: 8px;}
nav .user, .user a  { display: flex; flex: 0 0 15%; gap: 8px; }

</style>
