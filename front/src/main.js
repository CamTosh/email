import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Axios from "axios";

import TrendChart from "vue-trend-chart";
import JsonCSV from 'vue-json-csv'
import VueGoodTablePlugin from 'vue-good-table';
import VCalendar from "v-calendar";

import "@/assets/tailwind.css";
import 'vue-good-table/dist/vue-good-table.css'

Vue.component('downloadCsv', JsonCSV)
Vue.use(TrendChart);
Vue.use(VueGoodTablePlugin);

Vue.use(VCalendar, {
  locale: "fr"
});

Vue.config.productionTip = false;
Vue.prototype.$http = Axios;

const accessToken = localStorage.getItem("access_token");
if (accessToken) {
  Vue.prototype.$http.defaults.headers.common["Authorization"] = accessToken;
}

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount("#app");
