<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header selected="Dashboard" />

    <div
      v-if="user.plan.id == 'free'"
      class="w-3/4 flex items-center mt-4 justify-center"
    >
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br />
              The <b>{{ user.plan.id }} version</b> is limited to
              <b>{{ user.plan.campaigns }} campaigns</b> and
              <b>{{ user.plan.emailsPerCampaign }} emails</b><br /><br />
              Go to your
              <router-link class="underline text-gray-800" to="/account"
                >account</router-link
              >
              to activate your subscription 😎
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      v-if="$store.getters.loginPending == false"
      class="w-3/4 flex items-center mt-8 justify-center"
    >
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div
            class="w-full inline-flex justify-between px-3 font-medium text-gray-600"
          >
            <div class=" text-gray-700">Campaign</div>
            <router-link
              class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer outline-none"
              to="/dashboard/campaign/new"
            >
              + New
            </router-link>
          </div>
        </div>
        <router-link
          class="w-full py-3 flex flex-col hover:bg-gray-100 cursor-pointer"
          v-for="campaign in campaigns.slice().reverse()"
          :to="'dashboard/campaign/' + campaign.id"
        >
          <div class="w-full inline-flex justify-between h-12 px-8 m-2 py-3">
            <div class="text-left">
              {{ campaign.site }}
            </div>
            <div class="text-right">
              <span class="font-l mr-2">{{ campaign.emails }}</span>
              <span class="text-gray-600">Emails</span>
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import axios from "axios";

export default {
  components: {
    Header
  },
  data() {
    return {
      user: { plan: { id: "" } },
      api: null,
      token: null,
      campaigns: []
    };
  },
  mounted() {
    this.user = this.$store.getters.user;
    this.api = this.$store.getters.api;
    this.token = this.$store.getters.token;
    this.getCampaigns();
  },
  methods: {
    getCampaigns: async function() {
      axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign`,
        method: "GET"
      });
      const data = response.data.campaigns;

      if (data.error) {
        throw new Error(data.error);
      }
      this.campaigns = data;
      this.$store.dispatch("add_campaigns", this.campaigns);
    }
  }
};
</script>
