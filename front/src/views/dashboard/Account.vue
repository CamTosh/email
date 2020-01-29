<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header selected='Account' />
    <Error v-if='error && infoError' :message='error' />

    <div class="w-3/4 flex items-center mt-8 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-medium text-gray-600">
            <div class=" text-gray-700">Presonal Information</div>
          </div>
        </div>

        <div class="w-full py-3 px-5 inline-flex items-center md:justify-around lg:justify-around flex-col px-8">
          <div class="w-full md:px-8 lg:px-8 pt-6 rounded inline-flex flex-col md:flex-row lg:flex-row">
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
          </div>
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
    <div class="w-3/4 flex flex-col items-center mt-8 justify-center">
    
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-medium text-gray-600">
            <div class=" text-gray-700">Billing</div>
          </div>
        </div>

        <div class="w-full inline-flex text-center justify-center">
          <div class="w-1/2 inline-flex items-center bg-white text-gray-800 rounded-full p-2 m-2 shadow text-sm">
            <span class="inline-flex bg-green-600 text-white rounded-full h-6 px-3 justify-center items-center">Need More?</span>
            <span class="inline-flex px-2">
              Contact us: 
               <span class="ml-2 font-bold select-all">contact@email-landing.page</span>
           </span>
          </div>
        </div>

      
        <div class="w-full inline-flex text-center justify-center">
          <div class="w-1/2 mt-2 text-center">
            <div class="inline-flex p-2 w-full px-3 py-2 text-sm border rounded shadow items-center text-gray-700 rounded-lg w-full justify-around p-2">
              <div
                :class='{"bg-gray-800": selectedPeriod === "monthly"}'
                @click='selectedPeriod = "monthly"'
                class="inline-flex cursor-pointer bg-gray-700 text-white rounded-full h-6 px-3 py-4 justify-center items-center"
              >
                Monthly
              </div>
              <div
                :class='{"bg-gray-800": selectedPeriod === "annualy"}'
                @click='selectedPeriod = "annualy"'
                class="inline-flex cursor-pointer bg-gray-700 text-white rounded-full h-6 px-3 py-4 justify-center items-center"
              >
                Annualy (save 20%)
              </div>
            </div>
          </div>
        </div>

        <div class="w-full py-3 inline-flex md:justify-center items-center lg:justify-around flex-col md:flex-row lg:flex-row px-2">
          <div
            class="w-4/5 md:w-2/5 lg:w-2/5 mt-2 rounded-lg shadow p-6 inline-block"
            style="height: 400px;"
            v-for='plan in plans.filter((p) => p.period === selectedPeriod)'
            :class='{"shadow-xl": selectedPlan == plan.id}'
          >
            <div class="w-full" style="height: 90%">
              <div class="w-full inline-flex items-center justify-center lg:justify-around flex-col md:flex-row lg:flex-row">
                <div class="w-full text-center mt-2 lg:mt-0 lg:text-left lg:left-0">
                  <span class="bg-gray-600 text-gray-100 rounded-full h-6 px-3 py-1 capitalize">{{ plan.id }}</span>
                </div>
                <div
                  class="w-full text-center mt-2 lg:mt-0 lg:right-0 lg:text-right"
                  v-if='storePlan == plan.id && plan.period == period'
                >
                  <span class="bg-gray-800 text-white rounded-full h-6 px-3 py-1">Current Plan</span> 
                </div>
                <div
                  class="w-full text-center mt-2 lg:mt-0 lg:right-0 lg:text-right"
                  v-else-if='selectedPlan == plan.id'
                >
                  
                  <span class="bg-gray-800 text-white rounded-full h-6 px-3 py-1">Selected Plan</span> 
                </div>
              </div>
              <h2 class="text-4xl text-gray-900">
                {{ plan.price }} € 
                <span v-if='plan.period === "monthly"' class="text-lg text-gray-600">/month</span>
                <span v-else class="text-lg text-gray-600">/year</span>
              </h2>
              <div class="text-gray-600">{{ plan.description }}</div>
              <div class="inline-flex flex-col mt-2">
                <div class="my-1 inline-flex flex-row" v-for='(feature, key) in plan.features'>
                   <div v-if='plan.id=="startup" && key == 0' class="font-bold pt-1 mr-2 text-blue-600">
                    <svg height='18' width='18' fill="none" stroke="currentColor" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.1" x="0px" y="0px" viewBox="0 0 100 100"><g transform="translate(0,-952.36218)"><path style="opacity:1;fill:#3182ce;fill-opacity:1;stroke-width:3;" d="m 36.821482,955.37477 c -0.235991,0.0109 -0.469963,0.0641 -0.6875,0.15625 l -35,16 c -1.12509524,0.51218 -1.39272561,2.15004 -0.68749995,3.125 L 11.321482,987.37477 0.44648205,1000.0623 c -0.6544461,0.9192 -0.43759529,2.6128 0.68749995,3.125 l 10.84375,4.9688 0,23.2187 c 0.0058,0.7633 0.490041,1.5024 1.1875,1.8125 l 35.96875,16 c 0.509699,0.2266 1.115301,0.2266 1.625,0 l 36.03125,-16 c 0.697459,-0.3101 1.181707,-1.0492 1.1875,-1.8125 l 0,-23.2187 10.84375,-4.9688 c 1.125095,-0.5122 1.493758,-2.1879 0.6875,-3.125 l -10.875,-12.68753 10.875,-12.71875 c 0.806258,-0.93708 0.437595,-2.61282 -0.6875,-3.125 l -35,-16 c -0.312709,-0.13621 -0.660646,-0.19057 -1,-0.15625 -0.494621,0.0359 -0.97284,0.26365 -1.3125,0.625 l -11.53125,12.40625 -11.53125,-12.40625 c -0.410745,-0.43796 -1.026638,-0.67484 -1.625,-0.625 z m -0.3125,4.40625 10.09375,10.875 -32.0625,14.28125 -9.3125,-10.84375 z m 26.9375,0 31.28125,14.3125 -9.3125,10.84375 -32.0625,-14.28125 z m -13.46875,13.78125 31.0625,13.8125 -31.0625,13.78133 -31.0625,-13.78133 z m -35.4375,16.21875 32.0625,14.28128 -10.09375,10.875 -31.28125,-14.3125 z m 70.875,0 9.3125,10.84378 -31.28125,14.3125 -10.09375,-10.875 z m -37.4375,18.68758 0,35.8124 -32,-14.2187 0,-20.0937 20.15625,9.2187 c 0.764319,0.3513 1.745297,0.1525 2.3125,-0.4687 z m 4,0 9.53125,10.25 c 0.567203,0.6212 1.548181,0.82 2.3125,0.4687 l 20.15625,-9.2187 0,20.0937 -32,14.1875 z"></path></g></svg>
                  </div>
                  <div v-else class="font-bold pt-1 mr-2 text-green-600">
                    <svg class="w-4 h-4 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                  </div>
                  <span v-if='plan.id=="startup" && key == 0' class="font-semibold">{{ feature }}</span>
                  <span v-else>{{ feature }}</span>
                </div>
              </div>
            </div>
            <div class="w-full justify-center">
              <div v-if='storePlan == plan.id && plan.period == period' class="bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-not-allowed outline-none">
                Current Plan
              </div>
              <div v-else  @click='selectPlan(plan)' class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none">
                Get started
              </div>
            </div>
          </div>
         
        </div>


        <div class="w-full py-3 inline-flex items-center justify-center flex-col md:flex-row lg:flex-row">
          <card class='w-full shadow md:w-2/4 lg:w-2/4'
            :class='{ complete }'
            stripe='pk_test_RWLO2o36Z9Jc9BWJRpH12b8000RU1kHkUS'
            :options='stripeOptions'
            @change='complete = $event.complete'
          />

          <div class="mt-4 md:mt-0 lg:mt-0 md:ml-4 lg:ml-4">
            <div class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" @click='pay' :class="{'cursor-not-allowed': pending}">
              Pay with credit card
            </div>
          </div>

        </div>

      </div>
    </div>

    <div class="w-3/4 flex items-center mt-8 justify-center mb-8">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div class="w-full inline-flex justify-between px-3 mb-2 font-medium text-gray-600">
            <div class=" text-gray-700">Invoices</div>
          </div>
        </div>
        <div class="w-full py-4 inline-flex items-center md:justify-around lg:justify-around flex-col px-6">
          <div class="w-full inline-flex justify-around border-l-2 border-gray-800 px-4 py-3 00 bg-gray-100 rounded h-24 mt-2" v-for='invoice in invoices'>
            <div class="w-full inline-flex justify-around mr-4">
              <div class="w-1/2 h-full">
                <div class="text-gray-900 font-medium text-lg my-2">
                  Plan: <span class="text-gray-800 font-normal capitalize"> {{ invoice.plan }} ({{ invoice.period }})</span>
                </div>
                <div class="text-gray-900 font-medium text-lg my-2">
                  Start: <span class="text-gray-800 font-normal"> {{ parseDate(invoice.start) }}</span> 
                </div>
              </div>
              <div class="w-1/2 h-full">
                <div class="text-gray-900 font-medium text-lg my-2">
                  Price: <span class="text-gray-800 font-normal"> {{ Math.round(invoice.price) / 100 }} €</span>
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
      period: null,
      selectedPlan: null,
      storePlan: null,
      selectedPeriod: 'monthly',
      complete: false,
      pending: false,
      stripeOptions: {
        // see https://stripe.com/docs/stripe.js#element-options for details
      },
      plans: [
        {
          id: 'indie',
          price: '5',
          description: 'Great for personal project',
          period: 'monthly',
          features: [
            '5 Campaigns',
            '1 000 Emails Per Campaign',
            'Statistics',
            'Email validation',
            'Export'
          ]
        },
        {
          id: 'startup',
          price: '10',
          description: 'Great for biggest project',
          period: 'monthly',
          features: [
            'Indie features',
            '10 Campaigns',
            '10 000 Emails Per Campaign',
            'Several Call To Action per campaign',
            'Browser analytics',
          ]
        },
        {
          id: 'indie',
          price: '50',
          description: 'Great for personal project',
          period: 'annualy',
          features: [
            '5 Campaigns',
            '1 000 Emails Per Campaign',
            'Statistics',
            'Email validation',
            'Export'
          ]
        },
        {
          id: 'startup',
          price: '100',
          description: 'Great for biggest project',
          period: 'annualy',
          features: [
            'Indie features',
            '10 Campaigns',
            '10 000 Emails Per Campaign',
            'Several Call To Action per campaign',
            'Browser analytics',
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
    this.invoices = this.$store.getters.user.invoice.slice().reverse()
    this.period = this.$store.getters.user.plan.period
    this.selectedPeriod = this.period ? this.period : this.selectedPeriod;

    this.storePlan = this.$store.getters.user.plan.id
    this.selectedPlan = this.storePlan === 'free' ? null : this.storePlan

    this.api = this.$store.getters.api
    this.token = this.$store.getters.token
  },
  methods: {
    parseDate(date) {
      return moment.unix(date).format('DD MMMM YYYY')
    },
    isCurrentPlan(invoice) {
      const now = moment(new Date()).format('X');
      return now >= invoice.start && now <= invoice.end;
    },
    async pay() {
      if (this.selectedPlan && this.selectedPlan !== this.storePlan && this.selectedPeriod && !this.pending) {
        this.pending = true;
        this.billingError = false
        const { token } = await createToken();

        axios.defaults.headers.common["Authorization"] = this.token;
        const response = await axios({
          url: `${this.api}/purchase`,
          method: "POST",
          data: {
            stripeToken: token.id,
            plan: this.selectedPlan,
            period: this.selectedPeriod
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
          this.invoices = data
        }
      } else {
        this.error = 'Please select a billing plan';
        this.billingError = true
      }
      this.pending = false;
    },
    async updateAccount() {
      const response = await axios({
          url: `${this.api}/user`,
          method: "PUT",
          data: {
            mail: this.email,
            password: this.password,
            firstName: this.firstName,
            lastName: this.lastName,
          }
        });
        const data = response.data
        if (data) {
          this.info = 'Account Updated!'
        } else {
          this.error = 'Error on account update'
        }
    },
    selectPlan(plan) {
      this.selectedPlan = plan.id;
      this.selectedPeriod = plan.period;
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