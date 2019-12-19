<template>
<div class="container mx-auto">
    <div class="flex justify-center">
        <!-- Row -->
        <div class="w-full flex justify-center ">
            <!-- Col -->
            <div class="w-full lg:w-1/2 p-5 rounded-lg lg:rounded-l-none">
                <h3 class="pt-4 text-2xl text-center">Register</h3>
                <form class="w-full px-8 pt-6 pb-8  rounded inline-flex flex-row">
                    <div class="w-1/2 pr-4">
                        <div class="mb-4">
                            <label class="block mb-2 text-sm font-bold text-gray-700" for="mail">
                                Email
                            </label>
                            <input required v-model="mail" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="mail" type="email" placeholder="email" />
                        </div>
                        <div class="mb-4">
                            <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                                Password
                            </label>
                            <input required v-model="password" class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" />
                        </div>
                    </div>

                    <div class="w-1/2 pl-4 border-l">
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
                <div class="mb-4 text-center w-full inline-flex flex-col items-center">
                    <div v-if='mail && password && lastName && firstName' class="hover:bg-gray-800 bg-gray-700 text-white w-3/4 text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" @click='register()'>
                      Create account
                    </div>
                    <div v-else class="hover:bg-gray-800 bg-gray-700 text-white w-3/4 text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-not-allowed outline-none">
                      Create account
                    </div>
                </div>
                <hr class="mb-4 border-t" />
                <div class="text-center">
                    <a class="inline-block text-sm text-gray-500 align-baseline cursor-pointer hover:text-gray-800" href="/login">
                        Login!
                    </a>
                </div>
            </div>
        </div>
    </div>

</div>
</template>

<script>
export default {
    data() {
      return {
        mail: "",
        password: "",
        firstName: "",
        lastName: ""
      }
    },
    methods: {
      register: function () {
        if (this.mail && this.password && this.lastName && this.firstName) {
            this.$store.dispatch('register', {
                mail: this.mail,
                password: this.password,
                lastName: this.lastName,
                firstName: this.firstName
            })
            .then(() => this.$router.push('/dashboard/campaign/new'))
            .catch(err => console.log(err))
        }
      }
    }
}
</script>
