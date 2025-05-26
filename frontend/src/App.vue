<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
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
        <RouterLink to="/login">@niff.wear</RouterLink>
      </span>
      <span>
        <img alt="Niff logo" class="logo" src="@/assets/images/logo.svg" width="74px" height="24px"/>
      </span>
      <span>
        <RouterLink to="/login">Search</RouterLink>
      </span>
      <span>
        <RouterLink to="/login">Cart</RouterLink>
        <RouterLink to="/login">Profile</RouterLink>
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
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
  display: flex;
}

</style>
