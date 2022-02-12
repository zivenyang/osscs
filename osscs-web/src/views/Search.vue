<template>
  <div class="page-search">
    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->

        <CardPackageList
          :platform="platform"
          :q="q"
          :packageList="packageList"
          :nextPage="nextPage"
          :paginations="paginations"
        ></CardPackageList>
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
  </div>
</template>
<script>
import CardPackageList from "@/components/cards/CardPackageList.vue";
import { ajax } from "@/utils/ajax";
import { PackageApis } from "@/utils/apis";

const pagination = {
  onChange: (page) => {
    console.log(page);
  },
  pageSize: 10,
};

export default {
  components: {
    CardPackageList,
  },
  data() {
    return {
      platform: "",
      q: "",
      packageList: [],
      nextPage: "",
      paginations: pagination,
    };
  },

  methods: {
    // 页面数据初始化，从GET请求中获取参数
    loadData() {
      this.platform = this.$route.query.platform;
      this.q = this.$route.query.q;
      this.getPackageList();
    },
    getPackageList() {
      ajax
        .get(PackageApis.packageListUrl, {
          params: {
            platform: this.platform,
            q: this.q,
          },
        })
        .then(({ data: { package_list, next_page } }) => {
          this.packageList = package_list;
          this.nextPage = next_page;
        });
    },
  },
  mounted() {
    this.loadData();
  },
  // 解决当前页面数据不刷新问题
  watch: {
    $route() {
      this.loadData();
    },
  },
};
</script>