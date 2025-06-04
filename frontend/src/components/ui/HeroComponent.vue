<script setup>
import { ref } from 'vue';
import HeaderComponent from '../common/HeaderComponent.vue';
import ActionButton from '../common/ActionButton.vue';
import ImageCard from '../common/ImageCard.vue';
import ProductCard from '../common/ProductCard.vue';
import CarouselComponent from '../common/CarouselComponent.vue';
import DesignerComponent from '../common/DesignerComponent.vue';

// Import images properly
import image1 from '@/assets/demo/image1.png';
import image2 from '@/assets/demo/image2.png';
import image3 from '@/assets/demo/image3.png';
import image4 from '@/assets/demo/image4.png';
import imageHover from '@/assets/demo/image-hover.png';
import frontImage1 from '@/assets/demo/front-image1.png';
import frontImage2 from '@/assets/demo/front-image2.png';

const buttonText = `Discover Products`;

const api_responses = ref([
  { src: image1, bg: imageHover, link: '' },
  { src: image2, bg: imageHover, link: '' },
  { src: image3, bg: imageHover, link: '' },
  { src: image4, bg: imageHover, link: '' },
  { src: image1, bg: imageHover, link: '' },
  { src: image2, bg: imageHover, link: '' },
  { src: image2, bg: imageHover, link: '' },
]);

let categoryComponents = ref([]);
api_responses.value.forEach(response => {
  let card = { name: ImageCard, props: response };
  categoryComponents.value.push(card);
});

let productComponents = ref([]);
api_responses.value.forEach(response => {
  let card = { name: ProductCard, props: {
    ...response,
    title: "Product Title",
    designer: "Designer Name",
    price: 130
  }};
  productComponents.value.push(card);
});

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
    <div class="right-side"><img :src="frontImage1" alt="demo1"></div>
  </div>

  <CarouselComponent carousel-header="Categories" :components="categoryComponents" />
  <ActionButton button-text="Discover Products" arrow="True" />

  <HeaderComponent title="New Designers" />
  <div class="designer-grid">
    <DesignerComponent :src="frontImage2" designer-name="Huy Morzhoviy" />
    <DesignerComponent :src="frontImage1" designer-name="John Doe" />
  </div>
  <ActionButton button-text="See All" arrow="True" />

  <CarouselComponent carousel-header="Featured Products" :components="productComponents" />
  <ActionButton button-text="See All" arrow="True" />
  
</template>


<style scoped>
.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
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
  border-right: var(--base-border-black);
}

.hero-grid .left-side span {
  width: 326px;
}

.designer-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.designer-grid .designer-component img {
  border-top: none;
}

</style>
