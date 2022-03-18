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
            <a-avatar
              :size="74"
              shape="square"
              src="/static/images/face-1.jpg"
            />
            <div class="avatar-info">
              <h4 class="font-semibold m-0">{{ me.username }}</h4>
              <p>email: {{ me.email }}</p>
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
import QUERY_ME from "@/graphql/accounts/queries/QueryMe.graphql";
import { message } from "ant-design-vue";

export default {
  components: {
    // CardPlatformSettings,
  },
  data() {
    return {
      // Active button for the "User Profile" card's radio button group.
      profileHeaderBtns: "overview",
      me: {},
    };
  },
  apollo: {
    me: {
      query: QUERY_ME,
      // 错误处理
      error(error) {
        localStorage.removeItem("apollo-token");
        this.$router.push({
          name: "Login",
        });
        message.error(error.message);
      },
    },
  },
};
</script>

<style lang="scss"></style>
