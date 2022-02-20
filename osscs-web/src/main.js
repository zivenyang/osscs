import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.less';
import DefaultLayout from './layouts/Default.vue'
import './less/app.less'
import './utils/nprogress'


const app = createApp(App);
app.config.productionTip = false;

app.use(Antd).use(store).use(router).mount('#app');

// Adding template layouts to the vue components.
app.component("layout-default", DefaultLayout);