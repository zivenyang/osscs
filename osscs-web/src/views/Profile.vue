<!-- 
	This is the user profile page, it uses the dashboard layout in: 
	"./layouts/Dashboard.vue" .
 -->

<template>
  <div>
    <!-- User Profile Card -->
    <a-card
      :bordered="false"
      class="card-profile-head"
      :bodyStyle="{ padding: 0 }"
    >
      <template #title>
        <a-row type="flex" align="middle">
          <a-col :span="24" :md="12" class="col-info">
            <a-avatar :size="74" shape="square" src="/static/images/face-1.jpg" />
            <div class="avatar-info">
              <h4 class="font-semibold m-0">{{ username }}</h4>
              <p>CEO / Co-Founder</p>
            </div>
          </a-col>
          <a-col
            :span="24"
            :md="12"
            style="
              display: flex;
              align-items: center;
              justify-content: flex-end;
            "
          >
            <a-radio-group v-model="profileHeaderBtns" size="small">
              <a-radio-button value="overview">OVERVIEW</a-radio-button>
              <a-radio-button value="teams">TEAMS</a-radio-button>
              <a-radio-button value="projects">PROJECTS</a-radio-button>
            </a-radio-group>
          </a-col>
        </a-row>
      </template>
    </a-card>
    <!-- User Profile Card -->

    <a-row type="flex" :gutter="24">
      <!-- Platform Settings Column -->
      <a-col :span="24" :md="8" class="mb-24">
        <!-- Platform Settings Card -->
        <!-- <CardPlatformSettings></CardPlatformSettings> -->
        <!-- / Platform Settings Card -->
      </a-col>
      <!-- / Platform Settings Column -->
    </a-row>
  </div>
</template>

<script>
// import CardPlatformSettings from "../components/Cards/CardPlatformSettings";

export default {
  components: {
    // CardPlatformSettings,
  },
  data() {
    return {
      // Active button for the "User Profile" card's radio button group.
      profileHeaderBtns: "overview",
      username: this.$route.params.username,
    };
  },
};
</script>

<style lang="scss">
</style>