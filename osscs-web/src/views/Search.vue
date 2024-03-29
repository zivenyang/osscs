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
          :hasNextPage="hasNextPage"
          :fetchMore="fetchMore"
          :loading="$apollo.queries.packagesData.loading"
        ></CardPackageList>
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
  </div>
</template>
<script>
import CardPackageList from "@/components/cards/CardPackageList.vue";
import gql from "graphql-tag";
import { message } from "ant-design-vue";

const QueryPackagesGql = gql`
  query QueryPackages(
    $platforms: String!
    $q: String!
    $page: Int
    $perPage: Int
  ) {
    packages(platforms: $platforms, q: $q, page: $page, perPage: $perPage) {
      hasNextPage
      packages {
        name
        description
        keywords
        licenses
        latestReleaseNumber
        latestStableReleaseNumber
        stars
        dependentReposCount
        status
      }
    }
  }
`;

export default {
  components: {
    CardPackageList,
  },
  data() {
    return {
      platforms: this.$route.query.platforms,
      q: this.$route.query.q,
      packageList: [],
      hasNextPage: false,
      page: 1,
      perPage: 20,
      packagesData: {},
    };
  },
  methods: {
    fetchMore() {
      this.page++;

      this.$apollo.queries.packagesData.fetchMore({
        // 新的变量
        variables: {
          platforms: this.platforms,
          q: this.q,
          page: this.page,
          perPage: this.perPage,
        },
        // 用新数据转换之前的结果
        updateQuery: (previousResult, { fetchMoreResult }) => {
          // No new feed posts
          if (!fetchMoreResult) return previousResult;
          this.packageList = this.packageList.concat(
            fetchMoreResult.packages.packages
          );
          this.hasNextPage = fetchMoreResult.packages.hasNextPage;

          return {
            packages: {
              __typename: previousResult.packages.__typename,
              packages: [
                ...previousResult.packages.packages,
                ...fetchMoreResult.packages.packages,
              ],
              hasNextPage: fetchMoreResult.packages.hasNextPage,
            },
          };
        },
      });
    },
    refreshData() {
      (this.platforms = this.$route.query.platforms),
        (this.q = this.$route.query.q),
        (this.packageList = []),
        (this.hasNextPage = false),
        (this.page = 1),
        (this.perPage = 20),
        (this.packagesData = {}),
        this.$apollo.queries.packagesData.refresh();
    },
  },
  apollo: {
    packagesData: {
      query: QueryPackagesGql,
      // 响应式参数
      variables() {
        // 在这里使用 vue 的响应式属性
        return {
          platforms: this.platforms,
          q: this.q,
          page: this.page,
          perPage: this.perPage,
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
        this.packageList = this.packageList.concat(data.packages.packages);
        this.hasNextPage = data.packages.hasNextPage;
      },
      // 错误处理
      error(error) {
        message.error(error.message);
      },
    },
  },
  updated() {
    this.refreshData();
  },
};
</script>