<script setup>
import { ref } from 'vue';
import { markRaw } from 'vue';

import ShopHeader from '@/components/ui/ShopHeader.vue';
import ProductCard from '@/components/common/ProductCard.vue';
import ProductsGrid from '@/components/common/ProductsGrid.vue';
import PaginationComponent from '@/components/common/PaginationComponent.vue';

import image1 from '@/assets/demo/image1.png';
import image2 from '@/assets/demo/image2.png';
import image3 from '@/assets/demo/image3.png';
import image4 from '@/assets/demo/image4.png';
import imageHover from '@/assets/demo/image-hover.png';

const api_responses = ref([]);

for (let i = 0; i < 16; i++) {
  api_responses.value.push({
    src: [image1, image2, image3, image4][i % 4],
    bg: imageHover,
    link: ''
  });
}

let productComponents = ref([]);
api_responses.value.forEach(response => {
  let card = { 
    name: markRaw(ProductCard), 
    props: {
      ...response,
      title: "Product Title",
      designer: "Designer Name",
      price: 130
    }
  };
  productComponents.value.push(card);
});

const itemsAmount = ref(productComponents.value.length);

const finalProductComponents = ref({
  totalPages: 3,
  limit: 16,
  components: productComponents.value
});

</script>


<template>
  <div class="shop-view">
    <ShopHeader header-title="All Products" :itemsAmount="itemsAmount" />
    <ProductsGrid :components="finalProductComponents.components" 
                  :total-pages="finalProductComponents.totalPages" 
                  :limit="finalProductComponents.limit" />
    <PaginationComponent :total-pages="finalProductComponents.totalPages" />
  </div>
</template>


<script setup>

</script>
