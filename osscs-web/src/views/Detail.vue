<template>
  <div class="page-detail">
    <a-back-top />

    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->
        <CardPackageInfo
          :packageDetail="packageDetail"
          :loading="$apollo.queries.packageData.loading"
        />
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
    <a-row type="flex" :gutter="24">
      <a-col :span="24" :md="16" class="mb-24">
        <CardPackageTable
          :data="packageVersionTableData"
          :columns="packageVersionTableColumns"
          :loading="$apollo.queries.packageData.loading"
        />
      </a-col>
    </a-row>
  </div>
</template>
<script>
import CardPackageInfo from "@/components/cards/CardPackageInfo.vue";
import CardPackageTable from "@/components/cards/CardPackageTable.vue";
import gql from "graphql-tag";
import { message } from 'ant-design-vue';

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
    dataIndex: "publishedAt",
    class: "date",
  },
];

const QueryPackageDetailGql = gql`
  query QueryPackageDetail($name: String!, $platform: String!) {
    package(name: $name, platform: $platform) {
      keywords
      licenses
      dependentReposCount
      description
      name
      versions {
        number
        publishedAt
        usages
        vulnerabilities
      }
    }
  }
`;

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
      packageData: {},
    };
  },
  methods: {
    // 页面数据初始化，从GET请求中获取参数
    loadData() {
      this.platform = this.$route.params.platform;
      this.packageName = this.$route.params.packageName;
      this.packageDetail = {};
      this.packageVersionTableData = [];
      this.getPackageDetail();
    },
    getPackageDetail() {
      this.$apollo.addSmartQuery("packageData", {
        query: QueryPackageDetailGql,
        // 响应式参数
        variables() {
          // 在这里使用 vue 的响应式属性
          return {
            name: this.packageName,
            platform: this.platform,
          };
        },
        // 我们使用自定义的 update 回调函数，因为字段名称不匹配
        // 默认情况下，将使用 'data' 结果对象上的 'pingMessage' 属性
        // 考虑到 apollo 服务端的工作方式，我们知道结果是在 'ping' 属性中
        update(data) {
          // 返回的值将更新 vue 属性 'pingMessage'
          return data;
        },
        // 可选结果钩子
        result({ data }) {
          this.packageDetail = data.package;
          this.packageVersionTableData = data.package.versions;
        },
        // 错误处理
        error(error) {
          message.error(error.message);
          console.error("We've got an error!", error);
        },
      });
    },
  },

  updated() {
    this.loadData();
  },
  created() {
    this.loadData();
  },
};
</script>