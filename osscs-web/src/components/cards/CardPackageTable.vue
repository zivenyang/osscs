<template>
  <div>
    <!-- Authors Table Card -->
    <a-card
      :bordered="false"
      class="header-solid h-full card-package-table"
      :bodyStyle="{ padding: 0 }"
      :loading="loading"
    >
      <template #title>
        <a-row type="flex" align="middle">
          <a-col :span="24" :md="24">
            <h5 class="font-semibold m-0">版本信息</h5>
          </a-col>
        </a-row>
      </template>
      <a-table :columns="columns" :data-source="data" :pagination="true">
        <template #vulnerabilities="{ text: vulnerabilities }">
          <div class="package-vulnerabilities-info">
            <a-tag color="error" v-if="vulnerabilities">
              {{ vulnerabilities }}
            </a-tag>
          </div>
        </template>

        <template #usages="{ text: usages }">
          {{ usages }}
          <a-progress
            :stroke-color="{
              from: '#6CA8AF',
              to: '#C3D94E',
            }"
            :percent="usages"
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
    loading: {
      type: Boolean,
      default: true,
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