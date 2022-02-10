<template>
  <div>
    <!-- Authors Table Card -->
    <a-card
      :bordered="false"
      class="header-solid h-full card-package-table"
      :bodyStyle="{ padding: 0 }"
    >
      <template #title>
        <a-row type="flex" align="middle">
          <a-col :span="24" :md="24">
            <h5 class="font-semibold m-0">版本信息</h5>
          </a-col>
        </a-row>
      </template>
      <a-table :columns="columns" :data-source="data" :pagination="true">
        <template #version="{ text: version }">
          <div class="package-version-info">
            <a :href="version.href"
              ><h6>{{ version.value }}</h6></a
            >
          </div>
        </template>

        <template #vulnerabilities="{ text: vulnerabilities }">
          <div class="package-vulnerabilities-info" >
            <a-tag color="error" v-if="vulnerabilities.value">
              <a :href="vulnerabilities.href">{{ vulnerabilities.value }}</a>
            </a-tag>
          </div>
        </template>

        <template #usages="{ text: usages }">
          <a :href="usages.href">{{ usages.value }}</a>
          <a-progress
            :stroke-color="{
              from: '#6CA8AF',
              to: '#C3D94E',
            }"
            :percent="usages.value"
			:show-info="false"
            status="active"
          />
        </template>
      </a-table>
    </a-card>
    <!-- / Authors Table Card -->
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
      default: () => [],
    },
    columns: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      // Active button for the "Authors" table's card header radio button group.
      authorsHeaderBtns: "all",
    };
  },
};
</script>