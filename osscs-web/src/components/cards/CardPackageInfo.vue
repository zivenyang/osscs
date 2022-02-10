<template>
  <div>
    <!-- User Profile Card -->
    <a-card
      :bordered="false"
      class="card-package-info"
      :bodyStyle="{ padding: 0 }"
    >
      <a-card-meta>
        <template #avatar>
          <a-avatar
            :size="74"
            shape="square"
            src="/static/packageIcon/android.webp"
          />
        </template>
        <template #title>
          <a
            href="https://mvnrepository.com/artifact/com.google.android/android"
            ><h4 class="font-semibold m-0">Google Android Library</h4></a
          >
        </template>
        <template #description>
          <a-row type="flex" align="middle">
            <a-col :span="24" :md="24" class="col-info">
              <p>
                A library jar that provides APIs for Applications written for
                the Google Android Platform.
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
              <a-descriptions :column="{ xxl: 4, xl: 3, lg: 3, md: 3, sm: 2, xs: 1 }">
                <a-descriptions-item label="license">
                  <a-tag color="green">Apache 2.0</a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="categories">
                  <a-tag color="red">Android Platform</a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="tags"
                  ><a-tag color="pink">google</a-tag>
                  <a-tag color="red">android</a-tag>
                  <a-tag color="red">platform</a-tag>
                </a-descriptions-item>
                <a-descriptions-item label="usedBy">
                  <a
                    href="https://mvnrepository.com/artifact/com.google.android/android/usages"
                  >
                    1,342 artifacts</a>
                </a-descriptions-item>
              </a-descriptions>
            </a-col>
          </a-row>
        </template>
      </a-card-meta>
    </a-card>
    <!-- User Profile Card -->
  </div>
</template>
<script>
export default {
  data() {
    return {
      // Active button for the "User Profile" card's radio button group.
      profileHeaderBtns: "overview",
    };
  },
};
</script>