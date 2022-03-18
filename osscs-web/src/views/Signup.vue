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
            style="text-align: center; line-height: 44px; margin: 5px"
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
            style="text-align: center; line-height: 44px; margin: 5px"
          >
            <template #icon
              ><GoogleOutlined :style="{ fontSize: '20px' }"
            /></template>
          </a-button>
        </div>
        <p class="text-center my-25 font-semibold text-muted">或者</p>
        <a-form
          name="regsiterForm"
          id="components-form-demo-normal-login"
          ref="registerFormRef"
          :model="registerForm"
          :rules="rules"
          class="login-form"
        >
          <a-form-item has-feedback class="mb-10" name="username">
            <a-input
              v-model:value="registerForm.username"
              placeholder="请输入用户名"
            >
            </a-input>
          </a-form-item>
          <a-form-item has-feedback class="mb-5" name="password">
            <a-input-password
              v-model:value="registerForm.password"
              placeholder="请输入密码"
            />
          </a-form-item>
          <a-form-item has-feedback class="mb-5" name="checkPassword">
            <a-input-password
              v-model:value="registerForm.checkPassword"
              placeholder="请确认密码"
            />
          </a-form-item>
          <a-form-item has-feedback class="mb-10" name="email">
            <a-input
              v-model:value="registerForm.email"
              placeholder="请输入邮箱"
            >
            </a-input>
          </a-form-item>
          <a-input-group compact>
            <a-form-item
              has-feedback
              class="mb-10"
              name="smsCode"
              style="width: 70%"
            >
              <a-input
                v-model:value="registerForm.smsCode"
                placeholder="请输入验证码"
              >
              </a-input>
            </a-form-item>
            <a-button
              type="primary"
              block
              html-type="submit"
              class="send-smscode-button"
              @click.prevent="sendSmsCode"
              style="width: 30%"
              >发送验证码
            </a-button>
          </a-input-group>
          <a-form-item has-feedback class="mb-10" name="agreement">
            <a-checkbox v-model:checked="registerForm.agreement">
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
              @click.prevent="onSubmit"
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
import { message } from "ant-design-vue";
import SIGNUP from "../graphql/accounts/mutations/Signup.graphql";

export default {
  components: {
    GithubOutlined,
    GoogleOutlined,
  },
  data() {
    return {
      registerForm: {
        username: "",
        password: "",
        checkPassword: "",
        email: "",
        smsCode: "",
        agreement: false,
      },
      rules: {
        username: [
          { required: true, message: "用户名不能为空", trigger: "change" },
          {
            pattern: /^[a-z0-9_-]{6,16}$/,
            message:
              "用户名输入不正确，只能包含小写字母、数字、中划线和下划线，长度为6-16个字符",
            trigger: "change",
          },
        ],
        password: [
          { required: true, message: "密码不能为空", trigger: "change" },
          {
            pattern:
              /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9~!@#$%^&*]{8,16}$/,
            message:
              "密码格式不正确，必须包含大小写字母和数字的组合，可以使用特殊字符(~!@#$\\%^&*)，长度在8-16之间",
            trigger: "change",
          },
        ],
        checkPassword: [
          { required: true, message: "请确认密码", trigger: "change" },
          {
            validator: () =>
              this.registerForm.password === this.registerForm.checkPassword
                ? Promise.resolve()
                : Promise.reject("两次密码输入不一致"),
            trigger: "change",
          },
        ],
        email: [
          { required: true, message: "邮箱不能为空", trigger: "change" },
          {
            pattern: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
            message: "邮箱格式不正确",
            trigger: "change",
          },
        ],
        smsCode: [
          { required: true, message: "验证码不能为空", trigger: "change" },
          {
            pattern: /^[0-9]{6}$/,
            message: "验证码为6位数字",
            trigger: "change",
          },
        ],
        agreement: [
          {
            required: true,
            validator: () =>
              this.registerForm.agreement === true
                ? Promise.resolve()
                : Promise.reject("请勾选同意"),
            trigger: "change",
          },
        ],
      },
    };
  },
  methods: {
    sendSmsCode() {
      console.log("发送验证码");
    },
    handleRegister() {
      // 保存用户输入以防止错误
      const registerForm = this.registerForm;
      // 将其清除以尽早更新用户页面
      this.registerForm = {};
      // 调用 graphql 变更
      this.$apollo
        .mutate({
          // 查询语句
          mutation: SIGNUP,
          // 参数
          variables: {
            ...registerForm,
          },
        })
        .then(({ data }) => {
          if (data.register.errors.length !== 0) {
            // TODO: 定义优雅的错误类型
            message.error(data.register.errors[0].messages);
            this.registerForm = registerForm;
          } else {
            // 结果
            console.log("Register data:", data);
            localStorage.setItem("apollo-token", data.register.token);
            this.$router.push({
              name: "Profile",
            });
          }
        })
        .catch((error) => {
          this.registerForm = registerForm;
          throw error;
        });
    },
    // Handles input validation after submission.
    onSubmit() {
      // 验证整个表单项
      this.$refs.registerFormRef
        .validate()
        .then(() => {
          this.handleRegister();
        })
        .catch((error) => {
          console.error("请正确输入表单项", error);
        });
    },
  },
};
</script>

<style lang="scss"></style>
