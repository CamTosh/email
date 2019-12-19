<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header selected='Account' />

		<div class="w-3/4 flex items-center mt-8 justify-center">
			<div class="w-full bg-white pt-4 rounded shadow">
				<div class="w-full border-b border-gray-200">
					<div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
						<div class=" text-gray-700">Billing</div>
					</div>
				</div>

        <div class="w-full py-3 px-5 inline-flex md:justify-around lg:justify-around flex-col md:flex-row lg:flex-row px-8">
          
          <div class="w-full md:w-1/3 lg:w-1/3 border border-gray-200 rounded h-64 bg-gray-100 mt-2">
            
          </div>
          <div class="w-full md:w-1/3 lg:w-1/3 border border-gray-200 rounded h-64 bg-gray-100 mt-2">
            
          </div>

        </div>

				<div class="w-full py-3 px-5 inline-flex items-center justify-center flex-col md:flex-row lg:flex-row px-8">
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
	</div>
</template>
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
</style>
<style>
.stripe-card {
}
.stripe-card.complete {
  border-color: green;
}
</style> 

<script>
import Header from '@/components/Header.vue';
import Info from '@/components/Info.vue';
import Error from '@/components/Error.vue';
import axios from "axios";

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
      complete: false,
      stripeOptions: {
        // see https://stripe.com/docs/stripe.js#element-options for details
      }
    }
  },
  methods: {
    pay () {
      // createToken returns a Promise which resolves in a result object with
      // either a token or an error key.
      // See https://stripe.com/docs/api#tokens for the token object.
      // See https://stripe.com/docs/api#errors for the error object.
      // More general https://stripe.com/docs/stripe.js#stripe-create-token.
      createToken().then(data => console.log(data.token))
    }
  }
};
</script>