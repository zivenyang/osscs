<template>
  <div class="page-detail">
    <a-back-top />

    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->
        <CardPackageInfo :packageDetail="packageDetail" :loading="loading" />
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
    <a-row type="flex" :gutter="24">
      <a-col :span="24" :md="16" class="mb-24">
        <CardPackageTable
          :data="packageVersionTableData"
          :columns="packageVersionTableColumns"
          :loading="loading"
        />
      </a-col>
    </a-row>
  </div>
</template>
<script>
import CardPackageInfo from "@/components/cards/CardPackageInfo.vue";
import CardPackageTable from "@/components/cards/CardPackageTable.vue";
import { ajax } from "@/utils/ajax";
import { PackageApis } from "@/utils/apis";

// "Authors" table list of columns and their properties.
const packageVersionTableColumns = [
  {
    title: "Version",
    dataIndex: "number",
  },
  {
    title: "Vulnerabilities",
    dataIndex: "vulnerabilities",
    slots: { customRender: "vulnerabilities" },
  },
  {
    title: "Usages",
    dataIndex: "usages",
    slots: { customRender: "usages" },
  },
  {
    title: "Date",
    dataIndex: "published_at",
    class: "date",
  },
];

export default {
  components: {
    CardPackageInfo,
    CardPackageTable,
  },

  data() {
    return {
      // Associating "Authors" table data with its corresponding property.
      packageVersionTableData: [],

      // Associating "Authors" table columns with its corresponding property.
      packageVersionTableColumns: packageVersionTableColumns,

      platform: "",
      packageName: "",
      packageDetail: {},
      loading: true,
    };
  },
  methods: {
    // 页面数据初始化，从GET请求中获取参数
    loadData() {
      this.platform = this.$route.params.platform;
      this.packageName = this.$route.params.packageName;
      this.packageDetail = {};
      this.packageVersionTableData = [];
      this.loading = true;
      this.getPackageDetail();
    },
    getPackageDetail() {
      const url = PackageApis.packageDetailUrl
        .replace(":platform", this.platform)
        .replace(":name", this.packageName);
      ajax.get(url).then(({ data }) => {
        this.packageDetail = data;
        this.packageVersionTableData = data.versions;
        this.loading = false;
      });
    },
  },

  updated() {
    this.loadData();
  },
  mounted() {
    this.loadData();
  },
};
</script>