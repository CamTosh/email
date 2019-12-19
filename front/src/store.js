import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);
const API = "http://localhost:6969";

export default new Vuex.Store({
  state: {
    api: API,
    loginPending: false, 
    status: "",
    token: localStorage.getItem("token") || "",
    user: JSON.parse(localStorage.getItem("user")) || null,
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, {token, user}) {
      state.status = "success";
      state.token = token;
      state.user = user;
    },
    pending_login(state) {
      state.loginPending = !state.loginPending;
    },
    auth_error(state) {
      state.status = "error";
    },
    alert_error(state) {
      state.info_error = "error";
    },
    logout(state) {
      state.status = "";
      state.user = null;
      state.token = "";
    }
  },
  actions: {
    login({ commit }, user) {
      commit("pending_login");
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({
          url: API + "/login",
          data: user,
          method: "POST"
        })
          .then((resp) => {
            const token = `Bearer ${resp.data.bearer}`;
            localStorage.setItem("token", token);
            localStorage.setItem("user", JSON.stringify(resp.data.user));
            commit("auth_success", {token, user: resp.data.user});
            commit("pending_login");
            resolve(resp);
          })
          .catch((err) => {
            commit("auth_error");
            localStorage.removeItem("token");
            commit("pending_login");
            reject(err);
          });
      });
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        axios({ url: API + "/user", data: user, method: "POST" })
          .then((resp) => {
            const token = `Bearer ${resp.data.bearer}`;

            axios.defaults.headers.common["Authorization"] = token;
            
            localStorage.setItem("token", token);
            localStorage.setItem("user", JSON.stringify(resp.data.user));

            commit("auth_success", {token, user: resp.data.user});
            resolve(resp);
          })
          .catch((err) => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit("logout");
        localStorage.removeItem("token");
        localStorage.removeItem("user");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    },
    createCampaign({ commit }, campaign) {
      return new Promise((resolve, reject) => {
        axios.defaults.headers.common["Authorization"] = this.state.token;
        axios({
          url: API + "/campaign",
          data: campaign,
          method: "POST"
        })
          .then((resp) => {
            const data = JSON.parse(resp.data);
            if (data.error) {
              throw new Error(data.error);
            }
          })
          .catch((err) => {
            console.log(err);
            commit("alert_error", err);
          });
      });
    },
  },
  getters: {
    user: state => state.user,
    api: state => state.api,
    token: state => state.token,
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    loginPending: state => state.loginPending
  }
});
