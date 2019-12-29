<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header selected='Account' />
    <Error v-if='error && infoError' :message='error' />

    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
            <div class=" text-gray-700">Presonal Information</div>
          </div>
        </div>

        <div class="w-full py-3 px-5 inline-flex items-center md:justify-around lg:justify-around flex-col px-8">
          <form class="w-full md:px-8 lg:px-8 pt-6 rounded inline-flex flex-col md:flex-row lg:flex-row">
            <div class="w-full md:w-1/2 lg:w-1/2 md:pr-4 lg:pr-4">
                <div class="mb-4">
                    <label class="block mb-2 text-sm font-bold text-gray-700">
                        Email
                    </label>
                    <input required v-model="email" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" type="email" placeholder="email" />
                </div>
                <div class="mb-4">
                    <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                        Password
                    </label>
                    <input required v-model="password" class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" />
                </div>
            </div>

            <div class="w-full md:w-1/2 lg:w-1/2 md:pl-4 lg:pl-4 md:border-l lg:border-l">
                <div class="mb-4">
                    <label class="block mb-2 text-sm font-bold text-gray-700">
                        First Name
                    </label>
                    <input required v-model="firstName" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" type="text" />
                </div>
                <div class="mb-4">
                    <label class="block mb-2 text-sm font-bold text-gray-700">
                        Last Name
                    </label>
                    <input required v-model="lastName" class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" />
                </div>
            </div>
          </form>
          <div class="w-4/5 md:w-1/5 lg:w-1/5 my-2">
            <div class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" @click='updateAccount()'>
              Update account
            </div>
          </div>
        </div>
      </div>
    </div>

    <Error class='mt-4' v-if='error && billingError' :message='error' />
    <Info v-if='upgrade && info' :message='info' />
    <!-- Pricing -->
    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
            <div class=" text-gray-700">Billing</div>
          </div>
        </div>

        <div class="w-full py-3 inline-flex md:justify-center items-center lg:justify-around flex-col md:flex-row lg:flex-row px-2">

          <div class="w-4/5 md:w-2/5 lg:w-2/5 mt-2 rounded-lg shadow-md p-6" v-for='plan in plans' :class='{"shadow-2xl": selectedPlan == plan.id}'>
            <div class="w-full inline-flex">
              <div class="w-1/2 left-0">
                <span class="bg-gray-600 text-gray-100 rounded-full h-6 px-3 py-1 capitalize">{{ plan.id }}</span>
              </div>
              <div v-if='storePlan == plan.id' class="w-1/2 right-0 text-right">
                <span class="bg-gray-800 text-white rounded-full h-6 px-3 py-1">Current Plan</span> 
              </div>
            </div>
            <h2 class="text-4xl text-gray-900">
              {{ plan.price }} € <span class="text-lg text-gray-600">/month</span>
            </h2>
            <div class="text-gray-600">{{ plan.description }}</div>
            <div class="inline-flex flex-col mt-2">
              <div class="my-1 inline-flex flex-row" v-for='feature in plan.features'>
                 <div class="font-bold pt-1 mr-2 text-green-600">
                  <svg class="w-4 h-4 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                </div>
                {{ feature }}
              </div>
            </div>
            <div class="w-full mt-2 justify-center">
              <div @click='selectedPlan = plan.id' class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" :class='{"bg-gray-800": selectedPlan == plan.id}'>
                Get started
              </div>
            </div>
          </div>
         
        </div>

        <div class="w-full py-3 inline-flex items-center justify-center flex-col md:flex-row lg:flex-row px-8">
          <card class='w-full shadow md:w-2/4 lg:w-2/4'
            :class='{ complete }'
            stripe='pk_test_RWLO2o36Z9Jc9BWJRpH12b8000RU1kHkUS'
            :options='stripeOptions'
            @change='complete = $event.complete'
          />

          <div class="mt-4 md:mt-0 lg:mt-0 md:ml-4 lg:ml-4">
            <div class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" @click='pay' :disabled='!complete'>
              Pay with credit card
            </div>
          </div>

        </div>
      </div>
    </div>

    <div class="w-3/4 flex items-center mt-8 justify-center mb-8">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
            <div class=" text-gray-700">Invoices</div>
          </div>
        </div>
        <div class="w-full py-4 inline-flex items-center md:justify-around lg:justify-around flex-col px-6">
          <div class="w-full inline-flex justify-around border-l-2 border-gray-800 px-4 py-3 00 bg-gray-100 rouded h-24 mt-2" v-for='invoice in invoices'>
            <div class="w-full inline-flex justify-around mr-4">
              <div class="w-1/2 h-full">
                <div class="text-gray-900 font-medium text-lg my-2">
                  Plan: <span class="text-gray-800 font-normal capitalize"> {{ invoice.plan }}</span>
                </div>
                <div class="text-gray-900 font-medium text-lg my-2">
                  Start: <span class="text-gray-800 font-normal"> {{ parseDate(invoice.start) }}</span> 
                </div>
              </div>
              <div class="w-1/2 h-full">
                <div class="text-gray-900 font-medium text-lg my-2">
                  Price: <span class="text-gray-800 font-normal"> {{ Math.round(invoice.price) / 100 }} {{ invoice.currency }}</span>
                </div>
                <div class="text-gray-900 font-medium text-lg my-2">
                  End: <span class="text-gray-800 font-normal"> {{ parseDate(invoice.end) }}</span> 
                </div>
              </div>
            </div>
            <div v-if='isCurrentPlan(invoice)' class="font-bold pt-1 pl-1 text-green-600">
              <svg class="w-6 h-6 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
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
import axios from "axios";
import moment from "moment";

import { Card, createToken } from 'vue-stripe-elements-plus'
 
// pk_test_RWLO2o36Z9Jc9BWJRpH12b8000RU1kHkUS
export default {
  components: {
    Header,
    Info,
    Error,
    Card
  },
  data () {
    return {
      infoError: null,
      billingError: null,
      error: null,
      email: '',
      info: null,
      upgrade: null,
      password: '',
      firstName: '',
      lastName: '',
      invoices: [],
      selectedPlan: null,
      storePlan: null,
      complete: false,
      stripeOptions: {
        // see https://stripe.com/docs/stripe.js#element-options for details
      },
      plans: [
        {
          id: 'indie',
          price: '5',
          description: 'Great for building personal project',
          features: [
            '5 Campaigns',
            '1 000 Emails Per Campaign',
            'Statistics',
            'Export'
          ]
        },
        {
          id: 'startup',
          price: '10',
          description: 'Great for building biggest project',
          features: [
            '10 Campaigns',
            '10 000 Emails Per Campaign',
            'Statistics',
            'Export'
          ]
        },
      ]
    }
  },
  mounted() {
    this.$store.dispatch('getUser')
    this.email = this.$store.getters.user.mail
    this.firstName = this.$store.getters.user.firstName
    this.lastName = this.$store.getters.user.lastName
    this.invoices = this.$store.getters.user.invoice
    
    this.storePlan = this.$store.getters.user.plan.id
    this.selectedPlan = this.storePlan === 'free' ? null : this.storePlan

    this.api = this.$store.getters.api
    this.token = this.$store.getters.token
  },
  methods: {
    parseDate(date) {
      return moment.unix(date).format('DD MMM YYYY')
    },
    isCurrentPlan(invoice) {
      const now = moment(new Date()).format('X');
      return now >= invoice.start && now <= invoice.end;
    },
    async pay () {
      if (this.selectedPlan && this.selectedPlan !== this.storePlan) {
        this.billingError = false
        const { token } = await createToken();

        axios.defaults.headers.common["Authorization"] = this.token;
        const response = await axios({
          url: `${this.api}/purchase`,
          method: "POST",
          data: {
            stripeToken: token.id,
            plan: this.selectedPlan
          }
        });
        const data = response.data
        this.upgrade = data
        if (data.error) {
          this.error = data.error;
          this.billingError = true
        } 
        if (data) {
          this.info = 'Account Upgrade!'
        }
      } else {
        this.error = 'Please select a billing plan';
        this.billingError = true
      }
    }
  }
};
</script>

<style type="text/css">
.StripeElement {
  box-sizing: border-box;
  height: 40px;
  padding: 10px 12px;
  border: 1px solid transparent;
  border-radius: 4px;
  background-color: white;
  box-shadow: 0 1px 3px 0 #e6ebf1;
  -webkit-transition: box-shadow 150ms ease;
  transition: box-shadow 150ms ease;
}

.StripeElement--focus {
  box-shadow: 0 1px 3px 0 #cfd7df;
}

.StripeElement--invalid {
  border-color: #fa755a;
}

.StripeElement--webkit-autofill {
  background-color: #fefde5 !important;
}
.stripe-card {
}
.stripe-card.complete {
  border-color: green;
}
</style> 