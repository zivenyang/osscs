<template>
  <div class="page-search">
    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->

        <CardPackageList
          :platforms="platforms"
          :q="q"
          :packageList="packageList"
          :meta="meta"
          :getPackageList="getPackageList"
          :loading="loading"
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

// const pagination = {
//   onChange: (page) => {
//     console.log(page);
//   },
//   pageSize: 10,
// };

export default {
  components: {
    CardPackageList,
  },
  data() {
    return {
      platforms: "",
      q: "",
      packageList: [],
      meta: {},
      page: 1,
      perPage: 20,
      loading: true,
      // paginations: pagination,
    };
  },

  methods: {
    // 页面数据初始化，从GET请求中获取参数
    loadData() {
      this.platforms = this.$route.query.platforms;
      this.q = this.$route.query.q;
      this.packageList = [];
      this.meta = {};
      this.page = 1;
      this.loading = true;
      this.getPackageList();
      this.loading = false;
    },
    // onRefresh () {
    //   // 清空数据
    //   this.packageList = []
    //   this.page = 1
    //   // 重新加载数据
    //   this.getPackageList()
    // },
    getPackageList() {
      ajax
        .get(PackageApis.packageListUrl, {
          params: {
            platforms: this.platforms,
            q: this.q,
            page: this.page,
            perPage: this.perPage,
          },
        })
        .then(({ data: { package_list, meta } }) => {
          this.packageList = this.packageList.concat(package_list);
          this.meta = meta;
          this.page += 1;
        });
    },
  },
  mounted() {
    this.loadData();
  },
  updated() {
    this.loadData();
  },
};
</script>