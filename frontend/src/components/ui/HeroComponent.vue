<script setup>
import { ref } from 'vue';
import ActionButton from '../common/ActionButton.vue';
import ImageCard from '../common/ImageCard.vue';

const buttonText = `Discover Products`;

const images = ref([
  "../src/assets/demo/image1.png",
  "../src/assets/demo/image2.png",
  "../src/assets/demo/image3.png",
  "../src/assets/demo/image4.png",
])

</script>


<template>
  <div class="hero-grid">
    <div class="left-side">
      <div>
        <h1>
          Designed by <span>Rebels</span>.<br>
          Worn by <span>Originals</span>.
        </h1>
        <p>Discover limited drops from the next wave of fashion talent</p>
      </div>
      <span>
        <ActionButton :button-text="buttonText" arrow="True"/>
      </span>
    </div>
    <div class="right-side"><img src="../../assets/demo/front-image1.png" alt="demo1"></div>
  </div>

  <div class="categories-carousel">
    <div class="header">
      <h3>Categories</h3>
      <div class="switcher">
        <span class="prev">
          <svg width="24" height="24" viewBox="0 -6 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M15 18L9 12L15 6" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
        <span class="next">
          <svg width="24" height="24" viewBox="0 -6 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 18L15 12L9 6" stroke="#111111" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </span>
      </div>
    </div>
    
    <ul>
      <li v-for="image in images">
        <ImageCard :img-src="image" :img-bg-src="'../src/assets/demo/image-hover.png'" />
      </li>
    </ul>

    <ActionButton button-text="Discover Products" arrow="True" />
  </div>
</template>


<style>
.hero-grid {
  display: grid;
  grid-template-columns: 2fr 2fr;
}

.hero-grid h1, .hero-grid span {
  font-size: 64px;
  line-height: 72px;
  font-weight: 700;
}

.hero-grid span {
  color: var(--color-text-orange-hover);
}

.hero-grid p {
  color: var(--color-text-muted);
}

.hero-grid img {
  width: 720px;
  height: 720px;
  object-fit: cover;
  object-position: center;
  width: 100%;
  margin: 0 auto;
  padding: 0;
  justify-items: center;
  vertical-align: bottom;
}

.hero-grid .left-side {
  padding: 32px;
  display: flex;
  flex-direction: column;
  gap: 32px;
  justify-content: center;
  border-right: 1px var(--color-border-black) solid;
}

.hero-grid .left-side span {
  width: 326px;
}

.categories-carousel ul {
  padding: 0;
  display: flex;
  list-style: none;
}

.categories-carousel .header {
  border: 1px var(--color-border-black) solid;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
}

.categories-carousel .header h3 {
  font-size: 32px;
  font-weight: 700;
}

</style>
