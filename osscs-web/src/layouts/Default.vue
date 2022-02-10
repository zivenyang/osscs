<!-- 
	This is the default layout, used in homepage.
 -->

<template>
  <div>
    <!-- Default Layout -->
    <a-layout class="layout-default" id="layout-default" :class="[layoutClass]">
      <a-back-top />
      <!-- Layout Header ( Navbar ) -->
      <DefaultHeader :isHome="isHome" :navbarFixed="navbarFixed" />
      <!-- / Layout Header ( Navbar ) -->

      <!-- Page Content -->
      <a-layout-content>
        <router-view />
      </a-layout-content>
      <!-- / Page Content -->

      <!-- Layout Footer -->
      <DefaultFooter />
      <!-- / Layout Footer -->
    </a-layout>
    <!-- / Default Layout -->
  </div>
</template>

<script>
import DefaultHeader from "../components/headers/DefaultHeader";
import DefaultFooter from "../components/footers/DefaultFooter";

export default {
  components: {
    DefaultHeader,
    DefaultFooter,
  },
  data() {
    return {};
  },
  computed: {
    // Sets layout's element's class based on route's meta data.
    layoutClass() {
      return this.$route.meta.layoutClass;
    },
    // Set homepage based on route's meta data.
    isHome() {
      return this.$route.meta.isHome;
    },
    navbarFixed() {
      return this.$route.meta.navbarFixed;
    },
  },
};
</script>
