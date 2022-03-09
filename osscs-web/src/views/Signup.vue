<!-- 
	This is the sign up page, it uses the dashboard layout in: 
	"./layouts/Default.vue" .
 -->

<template>
  <div class="page-signup">
    <a-row type="flex" :gutter="[24, 24]" justify="center" align="middle">
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
        <div class="content">
          <h2 class="mb-5">用户注册</h2>
        </div>
        <h5 class="font-semibold text-center">通过其他平台注册</h5>
        <div class="sign-up-gateways text-center">
          <a-button
            href="#"
            target="_blank"
            type="primary"
            shape="circle"
            rel="noopener noreferrer"
            style="text-align: center; line-height: 44px; margin: 5px;"
          >
            <template #icon
              ><GithubOutlined :style="{ fontSize: '20px' }"
            /></template>
          </a-button>
          <a-button
            href="#"
            target="_blank"
            type="primary"
            shape="circle"
            rel="noopener noreferrer"
            style="text-align: center; line-height: 44px; margin: 5px;"
          >
            <template #icon
              ><GoogleOutlined :style="{ fontSize: '20px' }"
            /></template>
          </a-button>
        </div>
        <p class="text-center my-25 font-semibold text-muted">或者</p>
        <a-form
          id="components-form-demo-normal-login"
          :model="formState"
          class="login-form"
          @submit="handleSubmit"
        >
          <a-form-item class="mb-10">
            <a-input
              v-model:value="formState.username"
              placeholder="请输入用户名"
            >
            </a-input>
          </a-form-item>
          <a-form-item class="mb-10">
            <a-input v-model:value="formState.email" placeholder="请输入邮箱">
            </a-input>
          </a-form-item>
          <a-form-item class="mb-5">
            <a-input
              v-model:value="formState.password"
              type="password"
              placeholder="请输入密码"
            >
            </a-input>
          </a-form-item>
          <a-form-item class="mb-5">
            <a-input
              v-model:value="formState.checkpassword"
              type="password"
              placeholder="请确认密码"
            >
            </a-input>
          </a-form-item>
          <a-form-item class="mb-10">
            <a-checkbox v-model:checked="formState.agreement">
              我同意
              <a href="#" class="font-bold text-dark">条款和条件</a>
            </a-checkbox>
          </a-form-item>
          <a-form-item>
            <a-button
              type="primary"
              block
              html-type="submit"
              class="login-form-button"
            >
              注册
            </a-button>
          </a-form-item>
        </a-form>
        <p class="font-semibold text-muted text-center">
          已有账户？
          <router-link to="/login" class="font-bold text-dark"
            >登录</router-link
          >
        </p>
        <!-- / Sign Up Form -->
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { GithubOutlined, GoogleOutlined } from "@ant-design/icons-vue";
const formState = {
  username: "",
  email: "",
  password: "",
  checkpassword: "",
  agreement: false,
};
const rules = {
  username: [{ required: true, message: "Please input your username!" }],
  email: [{ required: true, message: "Please input your email!" }],
  password: [{ required: true, message: "Please input your password!" }],
  checkpassword: [
    { required: true, message: "Please input your password again!" },
  ],
};

export default {
  components: {
    GithubOutlined,
    GoogleOutlined,
  },
  data() {
    return {
      formState,
      rules,
    };
  },
  methods: {
    // Handles input validation after submission.
    handleSubmit() {
      // e.preventDefault();
      // this.form.validateFields((err, values) => {
      // 	if ( !err ) {
      // 		console.log('Received values of form: ', values) ;
      // 	}
      // });
      console.log("Received values of form: ", formState);
    },
  },
};
</script>

<style lang="scss">
</style>