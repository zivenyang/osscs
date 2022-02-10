<template>
  <!-- Layout Header ( Navbar ) -->
  <component :is="navbarFixed ? 'a-affix' : 'div'" :offset-top="top">
    <a-layout-header>
      <div class="header-col header-brand">
        <router-link :to="{ name: 'Home' }">
          <h6>&#127978;OSSCS</h6>
        </router-link>
      </div>

      <div class="header-search" v-show="!isHome">
        <a-input-search
          v-model:value="this.query"
          placeholder="请输入开源软件名称"
          class="header-search-bar"
          @search="onSearch"
          size="small"
        >
          <template #addonBefore>
            <a-select v-model:value="this.ossType" style="width: 90px">
              <a-select-option value="Maven">Maven</a-select-option>
              <a-select-option value="PyPI">PyPI</a-select-option>
            </a-select>
          </template>
        </a-input-search>
      </div>

      <div class="header-col header-btn">
        <a-button
          href="https://github.com/zivenyang/osscs"
          target="_blank"
          type="primary"
          shape="circle"
          rel="noopener noreferrer"
          style="text-align: center"
        >
          <template #icon
            ><GithubOutlined :style="{ fontSize: '20px' }"
          /></template>
        </a-button>
      </div>
    </a-layout-header>
    <!-- / Layout Header ( Navbar ) -->
  </component>
</template>

<script>
import { GithubOutlined } from "@ant-design/icons-vue";
export default {
  components: {
    GithubOutlined,
  },

  props: {
    // Header fixed status.
    navbarFixed: {
      type: Boolean,
      default: true,
    },
    // Is homepage.
    isHome: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      // Fixed header/sidebar-footer ( Affix component ) top offset.
      top: 0,
      query: "",
      ossType: "Maven",
    };
  },
  methods: {
    resizeEventHandler() {
      this.top = this.top ? 0 : -0.01;
      // To refresh the header if the window size changes.
      // Reason for the negative value is that it doesn't activate the affix unless
      // scroller is anywhere but the top of the page.
    },
    onSearch() {
      if (!this.query) {
        return;
      }
      this.$router.push({
        name: "Result",
        query: { ossType: this.ossType, query: this.query },
      });
    },
  },
  created() {
    // Registering window resize event listener to fix affix elements size
    // error while resizing.
    window.addEventListener("resize", this.resizeEventHandler);
  },
  unmounted() {
    // Removing window resize event listener.
    window.removeEventListener("resize", this.resizeEventHandler);
  },
};
</script>

<style lang="less" scoped>
.nav-link svg {
  margin-right: 5px;
  vertical-align: middle;
}
.nav-link span {
  vertical-align: middle;
}
.ant-menu-submenu-popup {
  width: 100%;
}
</style>