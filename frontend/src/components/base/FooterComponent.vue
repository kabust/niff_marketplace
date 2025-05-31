<script setup>
import ActionButton from '../common/ActionButton.vue';
import LogoWhite from '../common/LogoWhite.vue';
import InstagramLink from '../common/InstagramLink.vue'
</script>


<template>
<footer class="footer">
  <div class="footer-container">
    <div class="footer-section brand">
      <LogoWhite/>
      <p>“A marketplace for emerging streetwear designers. Powered by vision, not trends.”</p>
      <InstagramLink/>
    </div>

    <div class="footer-section">
      <h3>Shop</h3>
      <ul>
        <li><a href="#">All Collections</a></li>
        <li><a href="#">New Drops</a></li>
        <li><a href="#">Designer</a></li>
        <li><a href="#">Sales</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h3>About</h3>
      <ul>
        <li><a href="#">Our Story</a></li>
        <li><a href="#">How it Works</a></li>
        <li><a href="#">FAQ</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h3>Support</h3>
      <ul>
        <li><a href="#">Contact Us</a></li>
        <li><a href="#">Terms & Conditions</a></li>
        <li><a href="#">Privacy Policy</a></li>
      </ul>
    </div>

    <div class="footer-section designer">
      <h3>For Designers</h3>
      <p>Want to sell your collection on NIFF? <span>Join the new wave.</span></p>
      <ActionButton button-text="Apply Now" arrow="True"/>
    </div>
  </div>

  <div class="footer-bottom">
    <p>© 2025 NIFF. All rights reserved.</p>
  </div>
</footer>
</template>


<style scoped>
.footer {
  background-color: var(--color-background-dark);
  color: var(--color-text-white);
}

.footer-container {
  display: grid;
  grid-template-columns: 1.8fr 1.1fr 1.1fr 1.1fr 2.8fr;
  margin: auto;
  height: 276px;
  border: 1px solid var(--color-border-white);
}

.footer-section {
  border-right: 1px solid var(--color-border-white);
}

.footer-section:last-child {
  border: none;
  display: flex;
  flex-direction: column;
}

.footer-section:last-child p {
  margin-top: 0;
}

.footer-section:last-child button {
  margin-top: auto;
}

.footer-section h3 {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.5px;
  margin: 16px;
}

.footer-section ul {
  list-style: none;
  padding: 0;
  margin: 16px;
}

.footer-section ul li a {
  color: var(--color-text-white);
  text-decoration: underline;
  display: block;
  margin-bottom: 6px;
  transition: color 0.3s ease;
}

.footer-section ul li a:hover {
  color: var(--color-text-orange-hover);
}

.footer-section p {
  margin: 16px;
}

.footer .brand p {
  font-size: 14px;
  color: var(--color-text-white);
  line-height: 1.6;
  margin-top: 0;
}

.social {
  margin-top: 15px;
  font-size: 14px;
  display: flex;
  align-items: center;
}

.social i {
  margin-right: 8px;
}

.designer p {
  font-size: 14px;
}

.designer span {
  color: #ff4d00;
  text-decoration: none;
}

.footer-bottom {
  text-align: left;
  padding: 16px;
  margin: auto;
  border: 1px solid var(--color-border-white);
  border-top: none;
  height: 56px;
}
</style>
