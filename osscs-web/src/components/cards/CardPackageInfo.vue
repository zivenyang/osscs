<template>
  <div>
    <!-- Package Info Card -->
    <a-card
      :bordered="false"
      class="card-package-info"
      :bodyStyle="{ padding: 0 }"
      :loading="loading"
    >
      <a-card-meta>
        <template #title>
          <a :href="packageDetail.homepage"
            ><h4 class="font-semibold m-0">{{ this.packageDetail.name }}</h4></a
          >
        </template>
        <template #description>
          <a-row type="flex" align="middle">
            <a-col :span="24" :md="24" class="col-info">
              <p>
                {{ this.packageDetail.description }}
              </p>
            </a-col>
            <a-col
              :span="24"
              :md="24"
              style="
                display: flex;
                align-items: center;
                justify-content: flex-end;
              "
            >
              <a-descriptions :column="{ xxl: 4, xl: 3, lg: 3, md: 2, sm: 2, xs: 1 }">
                <a-descriptions-item label="keywords" :span="4"
                  ><a-tag
                    v-for="(keyword, keywordIndex) in this.packageDetail
                      .keywords"
                    :key="keywordIndex"
                    color="pink"
                    >{{ keyword }}</a-tag
                  >
                </a-descriptions-item>
                <a-descriptions-item label="license">
                  <a-tag color="green">{{ this.packageDetail.licenses }}</a-tag>
                </a-descriptions-item>

                <a-descriptions-item label="used by">
                  {{ this.packageDetail.dependent_repos_count }} repositories
                </a-descriptions-item>
              </a-descriptions>
            </a-col>
          </a-row>
        </template>
      </a-card-meta>
    </a-card>
    <!-- Package Info Card -->
  </div>
</template>
<script>
export default {
  props: ["packageDetail", "loading"],
  data() {
    return {};
  },
};
</script>