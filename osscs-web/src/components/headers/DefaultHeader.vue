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
          v-model:value="this.q"
          placeholder="请输入开源软件名称"
          class="header-search-bar"
          @search="onSearch"
          size="small"
        >
          <template #addonBefore>
            <a-select v-model:value="this.platforms" style="width: 90px">
              <a-select-option value="pypi">PyPI</a-select-option>
              <a-select-option value="maven">Maven</a-select-option>
            </a-select>
          </template>
        </a-input-search>
      </div>

      <div class="header-col header-btn">
        <a-dropdown>
          <template #overlay>
            <a-menu v-if="isAuthenticated != true">
              <a-menu-item key="1">
                <router-link :to="{ name: 'Login' }">登录</router-link>
              </a-menu-item>
              <a-menu-item key="2">
                <router-link :to="{ name: 'Signup' }">注册</router-link>
              </a-menu-item>
            </a-menu>
            <a-menu v-else>
              <a-menu-item key="1">
                <router-link :to="{ name: 'Profile' }">详情</router-link>
              </a-menu-item>
              <a-menu-item key="2"> 设置 </a-menu-item>
              <a-menu-item key="3" @click.prevent="onLogout">
                登出
              </a-menu-item>
            </a-menu>
          </template>
          <a-button
            type="primary"
            shape="circle"
            rel="noopener noreferrer"
            style="text-align: center"
          >
            <template #icon
              ><UserOutlined :style="{ fontSize: '20px' }"
            /></template>
          </a-button>
        </a-dropdown>
      </div>
    </a-layout-header>
    <!-- / Layout Header ( Navbar ) -->
  </component>
</template>

<script>
import { UserOutlined } from "@ant-design/icons-vue";
export default {
  components: {
    UserOutlined,
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
      q: "",
      platforms: "pypi",
      token: localStorage.getItem("apollo-token"),
    };
  },
  computed: {
    isAuthenticated() {
      if (
        this.token === null ||
        this.token === undefined ||
        this.token === ""
      ) {
        return false;
      } else {
        return true;
      }
    },
  },
  methods: {
    resizeEventHandler() {
      this.top = this.top ? 0 : -0.01;
      // To refresh the header if the window size changes.
      // Reason for the negative value is that it doesn't activate the affix unless
      // scroller is anywhere but the top of the page.
    },
    onSearch() {
      if (!this.q) {
        return;
      }
      this.$router.push({
        name: "Search",
        query: { platforms: this.platforms, q: this.q },
      });
    },
    onLogout() {
      localStorage.removeItem("apollo-token");
      this.$router.push({
        name: "Login",
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
  watch: {
    // 监听路由变化
    $route: {
      immediate: true, // 监听到路由的变化立即执行
      handler() {
        // 这里是监听路由后要做的事情
        this.token = localStorage.getItem("apollo-token");
      },
    },
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
