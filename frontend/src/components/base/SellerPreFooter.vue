<script setup>
import ActionButton from '../common/ActionButton.vue';
import image from '@/assets/demo/front-image3.png';
</script>

<template>
  <div class="seller-pre-footer">
    <div class="left-side">
      <div>
        <h2>Start <span>selling</span> your designs today.</h2>
        <p>Join niff to launch your fashion brand, sell directly to customers, and grow without middlemen. 
          We handle the platform — you focus on the vision.</p>
      </div>
      <span>
        <ActionButton button-text="Become a Seller" arrow="True"/>
      </span>
    </div>
    <div class="right-side"><img :src="image" alt="seller-footer-image"></div>
  </div>
</template>

<style scoped>
.seller-pre-footer {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-content: space-between;
  background-color: var(--base-color-white);
  border-top: var(--base-border-black);
  border-bottom: var(--base-border-white);
}

.seller-pre-footer .left-side {
  width: 75%;
  display: flex;
  flex-direction: column;
  padding-left: 16px;
}

.seller-pre-footer .left-side p {
  padding-top: 8px;
  color: var(--color-text-gray);
}

.seller-pre-footer .left-side span {
  color: var(--color-text-orange-hover);
}

.seller-pre-footer .left-side button {
  width: 50%;
  margin-top: 32px;
}

.seller-pre-footer img {
  width: 100%;
  height: 620px;
  object-fit: cover;
  object-position: center;
  justify-items: center;
  vertical-align: bottom;
}

</style>
