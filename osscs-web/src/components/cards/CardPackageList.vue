<template>
  <!-- Package List Card -->
  <a-card
    :bordered="false"
    class="header-solid h-full"
    :bodyStyle="{ paddingTop: 0, paddingBottom: '16px' }"
  >
    <template #title>
      <h6 :key="this.query">
        在 “{{ this.ossType }}” 中关于 “{{ this.query }}” 的搜索结果
      </h6>
    </template>

    <a-list
      :grid="{ gutter: [24, 24], column: 1 }"
      :data-source="packageList"
      item-layout="vertical"
      size="large"
      :pagination="paginations"
    >
      <template #renderItem="{ item, index }">
        <a-list-item :key="index">
          <router-link :to="{ name: 'Detail', params: { id: index } }">
            <a-card hoverable :bordered="false" class="card-package-list">
              <div class="col-info">
                <a-descriptions :title="item.title" :column="1">
                  <a-descriptions-item label="description">
                    {{ item.description }}
                  </a-descriptions-item>
                  <a-descriptions-item label="avatar">
                    {{ item.avatar }}
                  </a-descriptions-item>
                </a-descriptions>
              </div>
              <div class="col-action">
                <a-button type="link" size="small">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      class="fill-danger"
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M9 2C8.62123 2 8.27497 2.214 8.10557 2.55279L7.38197 4H4C3.44772 4 3 4.44772 3 5C3 5.55228 3.44772 6 4 6L4 16C4 17.1046 4.89543 18 6 18H14C15.1046 18 16 17.1046 16 16V6C16.5523 6 17 5.55228 17 5C17 4.44772 16.5523 4 16 4H12.618L11.8944 2.55279C11.725 2.214 11.3788 2 11 2H9ZM7 8C7 7.44772 7.44772 7 8 7C8.55228 7 9 7.44772 9 8V14C9 14.5523 8.55228 15 8 15C7.44772 15 7 14.5523 7 14V8ZM12 7C11.4477 7 11 7.44772 11 8V14C11 14.5523 11.4477 15 12 15C12.5523 15 13 14.5523 13 14V8C13 7.44772 12.5523 7 12 7Z"
                      fill="#111827"
                    />
                  </svg>
                  <span class="text-danger">DELETE</span>
                </a-button>
                <a-button type="link" size="small">
                  <svg
                    width="16"
                    height="16"
                    viewBox="0 0 20 20"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      class="fill-muted"
                      d="M13.5858 3.58579C14.3668 2.80474 15.6332 2.80474 16.4142 3.58579C17.1953 4.36683 17.1953 5.63316 16.4142 6.41421L15.6213 7.20711L12.7929 4.37868L13.5858 3.58579Z"
                      fill="#111827"
                    />
                    <path
                      class="fill-muted"
                      d="M11.3787 5.79289L3 14.1716V17H5.82842L14.2071 8.62132L11.3787 5.79289Z"
                      fill="#111827"
                    />
                  </svg>
                  <span class="text-dark">EDIT</span>
                </a-button>
              </div>
            </a-card>
          </router-link>
        </a-list-item>
      </template>
    </a-list>
    <!-- / Billing Information Card -->
  </a-card>

  <!-- <div class="content">
    <a-layout-content class="result_content">
      <h2 :key="this.query">
        在 “{{ this.ossType }}” 中关于 “{{ this.query }}” 的搜索结果
      </h2>
      <div class="result_list">
        <a-list
          item-layout="vertical"
          size="large"
          :pagination="paginations"
          :data-source="resultList"
          style="padding-bottom: 10px"
        >
          <template #renderItem="{ item }">
            <a-list-item key="item.title">
              <a-list-item-meta :description="item.description">
                <template #avatar>
                  <a-avatar
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                  />
                </template>
                <template #title>
                  <a :href="item.href">{{ item.title }}</a>
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </div>
    </a-layout-content>
  </div> -->
</template>

<script>
const dataList = [];
const pagination = {
  onChange: (page) => {
    console.log(page);
  },
  pageSize: 5,
};

for (let i = 0; i < 23; i++) {
  dataList.push({
    href: "/",
    title: `ant design vue part ${i}`,
    avatar: "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
    description:
      "Ant Design, a design language for background applications, is refined by Ant UED Team.",
  });
}

export default {
  components: {},
  data() {
    return {
      ossType: "",
      query: "",
      packageList: dataList,
      paginations: pagination,
    };
  },

  methods: {
    // 页面数据初始化，从GET请求中获取参数
    loadData() {
      this.ossType = this.$route.query.ossType;
      this.query = this.$route.query.query;
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
<style lang="less">
// .content {
//   min-height: calc(100vh - 134px);
//   .result_content {
//     background: #fafafa;
//     align-items: center;
//     display: flex;
//     flex-direction: column;
//     min-height: calc(100vh - 134px);
//     min-width: fit-content;
//     position: relative;
//     z-index: 1;
//     .result_list {
//       text-align: left;
//       width: 50%;
//     }
//   }
// }
</style>