<template>
  <div class="w-3/4 xs:w-full sm:w-full m:w-3/4 lg:w-3/4 xl:w-3/4 shadow bg-white rounded h-12 px-4 py-3 mt-8 inline-flex text-gray-600">
    <div class="w-full text-left left-0 inline-flex">
      <div class="mr-4 cursor-pointer" v-for='item in menu'> 
        <span @click='select(item)' v-if='item.name === selected' class="text-gray-900">{{ item.name }}</span>
        <span @click='select(item)' v-else>{{ item.name }}</span>
      </div>
    </div>
    <div @click='logout()' class="cursor-pointer text-right">Logout</div>
  </div>
</template>

<script>  
 export default {
    name: 'Header',
    props: {
      selected: String
    },
    data() {
      return {
        menu: [
    			{
  					name: 'Dashboard',
  					path: '/dashboard',
          },
          {
  					name: 'Account',
  					path: '/account',
          },
        ],
      }
    },
    methods: {
    	select(item) {
    		this.$router.push(item.path)
    	},
	    logout: function () {
	      this.$store.dispatch('logout')
	        .then(() => {
	          this.$router.push('/login')
	        })
		    }
    }
  };
</script>
