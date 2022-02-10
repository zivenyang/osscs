<template>
  <div class="page-result">
    <a-row type="flex" :gutter="24">
      <!-- Package List Column -->
      <a-col :span="24" :md="16" class="mb-24">
        <!-- Package List Card -->
        <CardPackageList />
        <!-- / Package List Card -->
      </a-col>
      <!-- / Package List Column -->
    </a-row>
  </div>
</template>
<script>
import CardPackageList from "@/components/cards/CardPackageList.vue";
export default {
  components: {
    CardPackageList,
  },
};
</script>