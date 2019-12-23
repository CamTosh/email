<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header />
    
    <div v-if="needUpgrade" class="w-3/4 flex items-center mt-4 justify-center">
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br>
              The <b>{{ user.plan.id }} version</b> is limited to <b>{{ user.plan.emailsPerCampaign }} emails</b> and you are reach the limit
              <span class="text-white bg-red-400 px-1 py-1 rounded">{{ campaign.total }}/{{ user.plan.emailsPerCampaign }}</span>
              <br><br>
              Go to your <router-link class='underline text-gray-800' to='/account'>account</router-link> to upgrade your subscription 😎
            </div>
         </div>
       </div>
     </div>
    </div>

    <!-- Info -->
    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
            <div class=" text-gray-700">Info</div>
          </div>
        </div>

        <div class="w-full py-3 inline-flex justify-around flex-col md:flex-row lg:flex-row px-8">
          
          <div class="md:w-3/5 lg:w-3/5 border border-gray-200 m-1 rounded h-24 bg-gray-100 mt-2 py-2 px-3">
            <div class="text-gray-800">
              Campaign Id: {{ campaign.id }}
            </div>
            <div class="text-gray-800">
              Emails: {{ campaign.total }}              
            </div>
          </div>
          <div class="md:w-3/5 lg:w-3/5 border border-gray-200 m-1 rounded h-24 bg-gray-100 mt-2 py-2 px-3">
            <div class="text-gray-800">
              Emails: {{ campaign.total }}
            </div>
            <div class="text-gray-800">
              Users: {{ campaign.total }}
            </div>
          </div>
          
        </div>
      </div>
    </div>
  

    <!-- Chart -->
    <div v-if='campaign' class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
       <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 font-bold text-gray-600">
            <div class="px-2 mb-2">{{ campaign.site }}</div>
            <div class="hover:bg-red-600 bg-red-500 text-white text-sm py-1 px-2 border border-red-500 rounded mb-2 cursor-pointer outline-none" @click='deleteCampaign'>
              Delete
            </div>
          </div>
          <div class="w-full py-3 px-3 flex flex-col">
            <TrendChart
              :interactive="true" 
              :datasets="[
                {
                  data: [10, 50, 20, 100, 40, 60, 80],
                  smooth: true,
                  fill: true
                }
              ]"
              :grid="{
                 verticalLines: true,
                 horizontalLines: true
              }"
              :labels='{
                 xLabels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                 yLabels: 5
              }'
              :min="0">
            </TrendChart>
          </div>
        </div>
      </div>
    </div>

    <!-- Emails -->
    <div v-if='campaign.emails' class="w-3/4 flex items-center my-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 font-bold text-gray-600 mb-2">
            <div class="">Emails</div>
            <download-csv
              class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none"
              :data="campaign.emails"
            >
              + Export
            </download-csv>
          </div>
        </div>
        <!-- Filtering -->
        <!-- <div class="w-full inline-flex items-center px-10 py-3 border-b border-gray-200 h-8 cursor-pointer">
          <div class="w-1/5">Id</div>
          <div class="w-2/5 ">Email</div>
          <div class="w-2/5">Created at</div>
        </div> -->
        <div class="w-full py-3 flex flex-col hover:bg-gray-100" v-for='(email, k) in campaign.emails' :key='email.email'>
          <div class="w-full inline-flex h-12 px-8 m-2 py-3">
            <div class="w-1/5">{{ k }}</div>
            <div class="w-2/5">{{ email.email }}</div>
            <div class="w-2/5">{{ email.created_at }}</div>
          </div>
        </div>
      </div>
    </div>


    <!-- Embed -->
    <div v-if='campaign.id' class="w-3/4 inline-flex flex-col cursor-pointer items-center justify-center" @click='openEmbed = !openEmbed'>
      <div class="rounded bg-white w-full p-4 fill-current text-green-700 inline-flex shadow mb-4">
        <svg class="w-6 h-6 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        <div class="text-gray-900 ml-4">Code to embed on your website</div>
      </div>
      <div class="w-full" v-if='openEmbed'>
        <Embed :campaignId='campaign.id' />
      </div>
    </div>

  </div>
</template>


<script>
import Header from '@/components/Header.vue';
import Embed from '@/components/Embed.vue';
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
      openEmbed: false,
      needUpgrade: false,
    }
  },
  mounted() {
    this.user = this.$store.getters.user
  	this.api = this.$store.getters.api
  	this.token = this.$store.getters.token
  	this.getCampaign()
  }, 
  methods: {
    getCampaign: async function() {
    	axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign/${this.$route.params.id}`,
        method: "GET"
      });
      const data = response.data
      if (data.error) {
        throw new Error(data.error);
      }
      this.campaign = data
      if (this.campaign.total > this.campaign.emails.length) {
        this.needUpgrade = true;
      }
    },
    deleteCampaign: async function() {
      axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign/${this.$route.params.id}`,
        method: "DELETE"
      });
      this.$router.push('/dashboard')
    }
  }
}
</script>