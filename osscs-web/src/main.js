import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.less';
import DefaultLayout from './layouts/Default.vue'
import './less/app.less'
import './utils/nprogress'
import apolloProvider from './utils/apollo'


const app = createApp(App);
app.config.productionTip = false;

app.use(Antd).use(store).use(router).use(apolloProvider).mount('#app');

// Adding template layouts to the vue components.
app.component("layout-default", DefaultLayout);