<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header />
    
    <Info v-if='campaignId' message='Campaign are created' />
    <Error v-if='error' :message='error' />

    <div v-if="user.plan.id == 'free'" class="w-3/4 flex items-center mt-4 justify-center">
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br>
              The <b>{{ user.plan.id }} version</b> is limited to <b>{{ user.plan.campaigns }} campaigns</b> and  <b>{{ user.plan.emailsPerCampaign }} emails</b><br><br>
              Go to your <router-link class='underline text-gray-800' to='/account'>account</router-link> to activate your subscription 😎
            </div>
         </div>
       </div>
      </div>
    </div>

    <div v-if="user.campaigns && user.plan.campaigns == user.campaigns.length" class="w-3/4 flex items-center mt-4 justify-center">
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br>
              The <b>{{ user.plan.id }} version</b> is limited to <b>{{ user.plan.campaigns }} campaigns</b> and you are reach the limit
              <span class="text-white bg-red-400 px-1 py-1 rounded">{{ user.campaigns.length }}/{{ user.plan.campaigns }}</span>
              <br><br>
              Go to your <router-link class='underline text-gray-800' to='/account'>account</router-link> to upgrade your subscription 😎
            </div>
         </div>
       </div>
      </div>
    </div>

    <!-- Detail -->
    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
            <div class=" text-gray-700">New Campaign</div>
          </div>
        </div>
        
          <div class="w-full py-3 px-5 inline-flex px-8">
            <div class="w-1/2">
              <div class="mb-1">Campaign Name : </div>
              <input placeholder="New product" type="text" v-model='name' class="py-2 px-3 shadow bg-gray-100 rounded outline-none w-3/4">
            </div>
            <div class="w-1/2">
              <div class="mb-1">Website : </div>
              <input placeholder="https://landingpage.com" type="text" v-model='site' class="py-2 px-3 shadow bg-gray-100 rounded outline-none w-3/4">
            </div>
          </div>
          <div class="w-full py-3 inline-flex items-center px-8" v-if='!campaignId'>
            <div v-if='name && site && user.plan.campaigns > user.campaigns.length' class="hover:bg-gray-800 bg-gray-700 text-white right-0 py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer outline-none" @click='create()'>
              + Create
            </div>
            <div v-else class="hover:bg-gray-800 bg-gray-700 text-white right-0 py-1 px-2 border border-gray-700 rounded mb-2 cursor-not-allowed outline-none">
              + Create
            </div>
          </div>
          
          <div class="w-full py-3 px-5 inline-flex px-8">
                        
            <div class="w-full">
              
              <div v-if='campaignId' class="rounded bg-gray-100 w-full p-4 fill-current text-green-700 inline-flex shadow">
                <svg class="w-6 h-6 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                <div class="text-gray-900 ml-4">Code to embed on your website</div>
              </div>
              
              <div v-else class="rounded bg-gray-100 w-full p-4 fill-current text-red-700 inline-flex shadow">
                <svg class="w-6 h-6 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                <div class="text-gray-900 ml-4">Code to embed on your website</div>
              </div>
              <div v-if='campaignId' class="w-full">
                <Embed :campaignId='campaignId' />
              </div>
              <div class="w-full py-3 inline-flex items-center" v-if='campaignId'>
                <router-link to='/dashboard' class="hover:bg-gray-800 bg-gray-700 text-white right-0 py-1 px-2 border border-gray-700 rounded mb-2 cursor-pointer outline-none">
                  Go to dashboard
                </router-link>
              </div>     
            </div>
          </div>  
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import Header from '@/components/Header.vue';
  import Info from '@/components/Info.vue';
  import Error from '@/components/Error.vue';
  import Embed from '@/components/Embed.vue';
  import axios from "axios";
  
  export default {
    components: {
      Header,
      Embed,
      Info,
      Error
    },
    data() {
      return {
        api: null,
        token: null,
        site: null,
        name: null,
        campaignId: null,
        error: null,
        user: {plan: {id: ''}},
      }
    },
    mounted() {
      this.user = this.$store.getters.user
      this.api = this.$store.getters.api
      this.token = this.$store.getters.token
    },
    methods: {
      create: async function() {
        if (this.site && this.name) {
          axios.defaults.headers.common["Authorization"] = this.token;
          const response = await axios({
            url: `${this.api}/campaign`,
            method: "POST",
            data: {
              site: this.site,
              name: this.name,
            }
          });
          const data = response.data
          if (data.error) {
            this.error = data.error;
          }
          if (data.id) {
            this.campaignId = data.id;
          }
        }
      }
    }
  }
  </script>