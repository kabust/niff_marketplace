<script setup>
import ActionButton from '../common/ActionButton.vue';

const buttonText = `Discover Products`;

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
    <div class="right-side"><img src="../../assets/demo/front-image1.png"></div>
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

</style>
