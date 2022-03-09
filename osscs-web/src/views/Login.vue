<!-- 
	This is the sign in page, it uses the dashboard layout in: 
	"./layouts/Default.vue" .
 -->

<template>
  <div class="page-login">
    <a-row type="flex" :gutter="[24, 24]" justify="center" align="middle">
      <!-- Sign In Form Column -->
      <a-col
        :span="24"
        :md="12"
        :lg="{ span: 12, offset: 0 }"
        :xl="{ span: 6, offset: 2 }"
        class="col-form"
        style="
          margin: 0px;
          margin-top: 50px;
          margin-left: 0px;
          margin-left: 0px;
        "
      >
        <h2 class="mb-15">用户登录</h2>

        <!-- Sign In Form -->
        <a-form
          id="components-form-demo-normal-login"
          :model="formState"
          :rules="rules"
          class="login-form"
          @submit="handleSubmit"
          :hideRequiredMark="true"
        >
          <a-form-item class="mb-10" label="邮箱" :colon="false">
            <a-input v-model:value="formState.email" placeholder="请输入邮箱" />
          </a-form-item>
          <a-form-item class="mb-5" label="密码" :colon="false">
            <a-input
              v-model:value="formState.password"
              type="password"
              placeholder="请输入密码"
            />
          </a-form-item>
          <a-form-item class="mb-10">
            <a-switch v-model:checked="formState.rememberMe" /> 记住我
          </a-form-item>
          <a-form-item>
            <a-button
              type="primary"
              block
              html-type="submit"
              class="login-form-button"
            >
              登录
            </a-button>
          </a-form-item>
        </a-form>
        <!-- / Sign In Form -->

        <p class="font-semibold text-muted">
          没有账户？
          <router-link to="/signup" class="font-bold text-dark"
            >注册</router-link
          >
        </p>
      </a-col>
      <!-- / Sign In Form Column -->

      <!-- Sign In Image Column -->
      <!-- <a-col :span="24" :md="12" :lg="12" :xl="12" class="col-img">
        <img src="images/img-signin.jpg" alt="" />
        <p>Sign in</p>
      </a-col> -->
      <!-- Sign In Image Column -->
    </a-row>
  </div>
</template>

<script>
const formState = {
  email: "",
  password: "",
  rememberMe: true,
};
const rules = {
  email: [{ required: true, message: "Please input your email!" }],
  password: [{ required: true, message: "Please input your password!" }],
};
export default {
  data() {
    return {
      // Binded model property for "Sign In Form" switch button for "Remember Me" .
      formState,
      rules,
    };
  },
  methods: {
    // Handles input validation after submission.
    handleSubmit() {
      //   e.preventDefault();
      //   this.form.validateFields((err, values) => {
      //     if (!err) {
      //       console.log("Received values of form: ", values);
      //     }
      //   });
      this.$router.push({
        name: "Profile",
        params: { username: this.formState.email },
      });
      console.log("Received values of form: ", this.formState);
    },
  },
};
</script>

<style lang="less">
body {
  background-color: #ffffff;
}
</style>