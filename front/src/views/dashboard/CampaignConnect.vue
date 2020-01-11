<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header />

    <div v-if="needUpgrade" class="w-3/4 flex items-center mt-4 justify-center">
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br />
              The <b>{{ user.plan.id }} version</b>
              <span class="text-white bg-red-400 px-1 py-1 rounded">
                doesn't provide API!
              </span>
              <br /><br />
              Go to your
              <router-link class="underline text-gray-800" to="/account"
                >account</router-link
              >
              to upgrade your subscription 😎
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 font-medium text-gray-600">
            <div class=" text-gray-700">API & WebHook</div>
            <div class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 -mt-1 cursor-pointer">
              + Create
            </div>
          </div>
        </div>
        
        <div class="w-full py-3 text-center px-8">
          First you must be create an API Key
        </div>
        <!-- Create, Renew, view + copy -->
      </div>
    </div>

    <!-- Embed -->
    <div class="w-3/4 mt-8 inline-flex flex-col cursor-pointer items-center justify-center">
      <div class="rounded bg-white w-full p-4 fill-current text-green-700 inline-flex shadow mb-4">
        
        <svg  class="w-6 h-6 align-middle" width="24" height="24" fill="#333333" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><g><path d="M134.961,466h242.078c27.57,0,50-22.43,50-50V166.104c0-2.746-1.129-5.371-3.123-7.26L307.683,48.74   c-1.857-1.76-4.318-2.74-6.877-2.74H134.961c-27.57,0-50,22.43-50,50v320C84.961,443.57,107.391,466,134.961,466z M312.363,80.722   l78.919,74.758h-68.919c-5.514,0-10-4.486-10-10V80.722z M104.961,96c0-16.542,13.458-30,30-30h157.402v79.48   c0,16.542,13.458,30,30,30h84.676V416c0,16.542-13.458,30-30,30H134.961c-16.542,0-30-13.458-30-30V96z"></path><path d="M293.586,358.799c1.873,1.572,4.154,2.34,6.423,2.34c2.854,0,5.688-1.215,7.665-3.572l31.195-37.177   c3.12-3.718,3.12-9.138,0-12.856l-31.195-37.177c-3.55-4.231-9.858-4.782-14.088-1.232c-4.23,3.55-4.783,9.857-1.232,14.088   l25.802,30.749l-25.802,30.749C288.803,348.942,289.355,355.249,293.586,358.799z"></path><path d="M204.326,357.567c1.978,2.357,4.812,3.573,7.665,3.572c2.269,0,4.55-0.768,6.423-2.34c4.23-3.55,4.783-9.857,1.232-14.088   l-25.802-30.749l25.802-30.749c3.551-4.231,2.998-10.538-1.232-14.088c-4.23-3.55-10.539-2.998-14.088,1.232l-31.195,37.177   c-3.12,3.718-3.12,9.138,0,12.856L204.326,357.567z"></path><path d="M245.099,385.81c0.509,0.077,1.014,0.115,1.513,0.115c4.859,0,9.123-3.55,9.874-8.501L275.288,253.5   c0.829-5.46-2.926-10.558-8.387-11.387c-5.46-0.83-10.559,2.926-11.387,8.386l-18.803,123.924   C235.883,379.884,239.638,384.982,245.099,385.81z"></path></g></svg>
        <div class="text-gray-900 ml-4">Code to embed on your website</div>
      </div>
      <div class="w-full">
        <Embed :campaignId="campaign.id" />
      </div>
    </div>


    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 font-medium text-gray-600 mb-2">
            <div class="text-gray-700">Integration</div>
          </div>
        </div>
        
        <div class="w-full py-3 inline-flex flex-row flex-wrap justify-center p-8 listPlugin">
          
          <div class="w-full lg:w-auto border-l-2 m-2 rounded shadow bg-gray-100 border-blue-600 px-3 py-2">  
            <div class="w-full inline-flex justify-between mt-2 plugin">
              <div class="text-gray-900 text-lg font-medium">Wordpress</div>
              <div class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer">
                + Install
              </div>
            </div>
          </div>
          
          <div class="w-full lg:w-auto border-l-2 m-2 rounded shadow bg-gray-100 border-orange-600 px-3 py-2">  
            <div class="w-full inline-flex justify-between mt-2 plugin">
              <div class="text-gray-900 text-lg font-medium">Zapier</div>
              <div class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer">
                + Install
              </div>
            </div>
          </div>

          <div class="w-full lg:w-auto border-l-2 m-2 rounded shadow bg-gray-100 border-blue-400 px-3 py-2">  
            <div class="w-full inline-flex justify-between mt-2 plugin">
              <div class="text-gray-900 text-lg font-medium">Mailchimp</div>
              <div class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer">
                + Install
              </div>
            </div>
          </div>
          
          <div class="w-full lg:w-auto border-l-2 m-2 rounded shadow bg-gray-100 border-yellow-500 px-3 py-2">  
            <div class="w-full inline-flex justify-between mt-2 plugin">
              <div class="text-gray-900 text-lg font-medium">MailJet</div>
              <div class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer">
                + Install
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>


  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Embed from "@/components/Embed.vue";
import axios from "axios";


export default {
  components: {
    Header,
    Embed
  },
  data() {
    return {
      api: null,
      token: null,
      campaign: {},
      needUpgrade: false,
    };
  },
  mounted() {
    console.log(this.$route.params.id)
    this.user = this.$store.getters.user;
    this.api = this.$store.getters.api;
    this.token = this.$store.getters.token;

    if (this.user.plan.id === 'free') {
      this.needUpgrade = true;
    }
  },
  methods: {
    async apiCall() {
      axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign/`,
        method: "GET"
      });
      const data = response.data;
      if (data.error) {
        throw new Error(data.error);
      }
    }
  }
};
</script>
<style type="text/css">
  .plugin {
    min-width: 18rem;
  }
  @media screen and (max-width: 960px) {
    .plugin {
      min-width: auto;
    }   
  }
</style>