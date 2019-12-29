import Vue from "vue";
import Router from "vue-router";
import store from "./store.js";
import Home from "./views/Home.vue";

import Login from "./components/Login.vue";
import Register from "./components/Register.vue";

import Dashboard from "./views/Dashboard.vue";
import Detail from "./views/dashboard/CampaignDetail.vue";
import Create from "./views/dashboard/CampaignCreate.vue";

import Account from "./views/dashboard/Account.vue";

Vue.use(Router);

let router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/login",
      name: "login",
      component: Login
    },
    {
      path: "/register",
      name: "register",
      component: Register
    },
    {
      path: "/register/:email",
      name: "registerWithEmail",
      component: Register
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: Dashboard,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/dashboard/campaign/new",
      name: "CreateCampaign",
      component: Create,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/dashboard/campaign/:id",
      name: "InfoCampaign",
      component: Detail,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/account",
      name: "Account",
      component: Account,
      meta: {
        requiresAuth: true
      }
    },
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn && store.getters.user) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
