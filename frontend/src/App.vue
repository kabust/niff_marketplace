<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <span>
        <RouterLink to="/">Shop</RouterLink>
        <RouterLink to="/login">Become a Seller</RouterLink>
        <RouterLink to="/login">Contact Us</RouterLink>
      </span>
      <span>
        <img alt="Instagram" src="@/assets/images/Instagram.svg">
        <RouterLink to="/login">@niff.wear</RouterLink>
      </span>
      <span>
        <RouterLink to="/"><img alt="Niff logo" class="logo" src="@/assets/images/logo.svg" width="74px" height="24px"/></RouterLink>
      </span>
      <span>
        <img alt="Cart" src="@/assets/images/Search.svg">
        <RouterLink to="/login">Search</RouterLink>
      </span>
      <span>
        <RouterLink to="/login"><img alt="Cart" src="@/assets/images/Cart.svg"></RouterLink>
        <RouterLink to="/login"><img alt="Profile" src="@/assets/images/Profile.svg"></RouterLink>
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

.logo {
  display: block;
}

nav {
  width: 100%;
  font-size: 16px;
  /* text-align: center; */
  margin-top: 0;
  display: flex;
  /* align-items: center; */
  border: 1px solid black;
  border-top: 0;
}

nav a {
  text-decoration: underline;
  color: var(--color-text);
  transition: 0.4s;
  padding: 3px;
}

@media (hover: hover) {
nav a:hover {
    color: var(--color-text-hover);
  }
}

@media (hover: hover) {
nav a:active {
    color: var(--color-text-muted);
  }
}

nav span {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 24px 54.5px;
  border-right: 1px solid black;
}

nav span:last-child {
  border-right: none;
}


</style>
