<template>
  <!-- Package List Card -->
  <a-card
    :bordered="false"
    class="header-solid h-full"
    :bodyStyle="{ paddingTop: 0, paddingBottom: '16px' }"
    :loading="loading"
  >
    <template #title>
      <h6 :key="this.q">
        在 “{{ this.platforms }}” 中关于 “{{ this.q }}” 的搜索结果
      </h6>
    </template>

    <a-list
      :grid="{ gutter: [24, 24], column: 1 }"
      :data-source="packageList"
      item-layout="vertical"
      size="large"
    >
      <template #renderItem="{ item, index }">
        <a-list-item :key="index">
          <a-card hoverable :bordered="false" class="card-package-list">
            <div class="col-info">
              <a-descriptions
                :column="{ xxl: 4, xl: 3, lg: 3, md: 2, sm: 2, xs: 1 }"
              >
                <template #title>
                  <router-link
                    :to="{
                      name: 'Detail',
                      params: {
                        platform: this.platforms,
                        packageName: item.name,
                      },
                    }"
                  >
                    {{ item.name }}
                  </router-link>
                </template>
                <a-descriptions-item :span="4">
                  {{ item.description }}
                </a-descriptions-item>
                <a-descriptions-item
                  :span="4"
                  label="keywords"
                  v-if="item.keywords.length > 0"
                  class="package-keywords"
                >
                  <a-tag
                    v-for="(keyword, keywordIndex) in item.keywords"
                    :key="keywordIndex"
                  >
                    {{ keyword }}</a-tag
                  >
                </a-descriptions-item>
                <a-descriptions-item label="license">
                  <a-tag :color="setLicenseColor(item.licenses)">
                    {{ item.licenses }}
                  </a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="latest release version">
                  {{ item.latestReleaseNumber }}
                </a-descriptions-item>
                <a-descriptions-item label="latest stable version">
                  {{ item.latestStableReleaseNumber }}
                </a-descriptions-item>
                <a-descriptions-item label="stars">
                  {{ item.stars }}
                </a-descriptions-item>
                <a-descriptions-item label="use by">
                  {{ item.dependentReposCount }}
                </a-descriptions-item>
                <a-descriptions-item label="status" v-if="item.status != null">
                  <a-tag :color="setStatusColor(item.status)">{{
                    item.status
                  }}</a-tag>
                </a-descriptions-item>
              </a-descriptions>
            </div>
          </a-card>
        </a-list-item>
      </template>
      <template #loadMore>
        <div
          :style="{
            textAlign: 'center',
            marginTop: '12px',
            height: '32px',
            lineHeight: '32px',
          }"
        >
          <!-- <a-spin v-if="meta.has_next_page" /> -->
          <a-button v-if="hasNextPage" @click="fetchMore"
            >Loading more</a-button
          >
          <p v-else>No more</p>
        </div>
      </template>
    </a-list>
    <!-- / Billing Information Card -->
  </a-card>
</template>

<script>
export default {
  props: [
    "packageList",
    "platforms",
    "q",
    "hasNextPage",
    "fetchMore",
    "loading",
  ],
  computed: {
    setLicenseColor() {
      return function (License) {
        if (License.indexOf("GPL") != -1) {
          return "red";
        } else if (License == "UNKNOWN") {
          return "orange";
        } else {
          return "green";
        }
      };
    },
    setStatusColor() {
      return function (license) {
        if (license == "Deprecated") {
          return "red";
        } else {
          return "green";
        }
      };
    },
  },
};
</script>
<style lang="less">
</style>