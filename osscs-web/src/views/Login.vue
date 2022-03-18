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
          name="loginForm"
          ref="loginFormRef"
          id="components-form-demo-normal-login"
          :model="loginForm"
          :rules="rules"
          class="login-form"
          :hideRequiredMark="true"
        >
          <a-form-item class="mb-10" label="用户名" :colon="false" name="username">
            <a-input v-model:value="loginForm.username" placeholder="请输入用户名" />
          </a-form-item>
          <a-form-item class="mb-5" label="密码" :colon="false" name="password">
            <a-input-password
              v-model:value="loginForm.password"
              type="password"
              placeholder="请输入密码"
            />
          </a-form-item>
          <a-form-item class="mb-10" name="rememberMe">
            <!-- TODO: 实现rememberMe -->
            <a-switch v-model:checked="loginForm.rememberMe" /> 记住我
          </a-form-item>
          <a-form-item>
            <a-button
              type="primary"
              block
              html-type="submit"
              class="login-form-button"
              @click.prevent="onSubmit"
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
import LOGIN from "../graphql/accounts/mutations/Login.graphql";

export default {
  data() {
    return {
      // Binded model property for "Sign In Form" switch button for "Remember Me" .
      loginForm: {
        username: "",
        password: "",
        rememberMe: true,
      },
      rules: {
        username: [{ required: true, message: "Please input your username!" }],
        password: [{ required: true, message: "Please input your password!" }],
      },
    };
  },
  methods: {
    // Handles input validation after submission.
    handleLogin() {
      // 保存用户输入以防止错误
      const loginForm = this.loginForm;
      // 将其清除以尽早更新用户页面
      this.loginForm = {};
      // 调用 graphql 变更
      this.$apollo
        .mutate({
          // 查询语句
          mutation: LOGIN,
          // 参数
          variables: {
            ...loginForm,
          },
        })
        .then(({ data }) => {
          // 结果
          console.log("Register data:", data);
          localStorage.setItem("apollo-token", data.tokenAuth.token);
          this.$router.push({
            name: "Profile",
          });
        })
        .catch((error) => {
          this.loginForm = loginForm;
          throw error;
        });
    },
    // Handles input validation after submission.
    onSubmit() {
      // 验证整个表单项
      this.$refs.loginFormRef
        .validate()
        .then(() => {
          this.handleLogin();
        })
        .catch((error) => {
          console.error("请正确输入表单项", error);
        });
    },
  },
};
</script>

<style lang="less">
body {
  background-color: #ffffff;
}
</style>
