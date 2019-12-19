import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Axios from "axios";
import TrendChart from "vue-trend-chart";
import JsonCSV from 'vue-json-csv'

Vue.component('downloadCsv', JsonCSV)
Vue.use(TrendChart);

import "@/assets/tailwind.css";

Vue.config.productionTip = false;
Vue.prototype.$http = Axios;

const accessToken = localStorage.getItem("access_token");
if (accessToken) {
  Vue.prototype.$http.defaults.headers.common["Authorization"] = accessToken;
}
import VCalendar from "v-calendar";

Vue.use(VCalendar, {
  locale: "fr"
});

new Vue({
  router,
  store,
  render: (h) => h(App)
}).$mount("#app");
