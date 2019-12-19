<template>
<div class="container mx-auto">
    <div class="flex justify-center">
        <!-- Row -->
        <div class="w-full flex justify-center ">
            <!-- Col -->
            <div class="w-full lg:w-1/2 p-5 rounded-lg lg:rounded-l-none">
                <h3 class="pt-4 text-2xl text-center">Welcome Back!</h3>
                <form class="px-8 pt-6 pb-8 mb-4 rounded">
                    <div class="mb-4">
                        <label class="block mb-2 text-sm font-bold text-gray-700" for="mail">
                            Email
                        </label>
                        <input v-model="mail" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="mail" type="text" placeholder="email" />
                    </div>
                    <div class="mb-4">
                        <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                            Password
                        </label>
                        <input v-model="password" class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" />
                    </div>
                    <div class="mb-4 text-center">
                        <div class="mb-4 text-center w-full inline-flex flex-col items-center">
                            <div class="hover:bg-gray-800 bg-gray-700 text-white w-3/4 text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none" @click='login()'>
                              Login
                            </div>
                        </div>
                    </div>
                    <hr class="mb-4 border-t" />
                    <div class="text-center">
                        <a class="inline-block text-sm text-gray-500 align-baseline hover:text-gray-800" href="/register">
                            Register
                        </a>
                    </div>
                </form>
            </div>
        </div>
    </div>

</div>
</template>

<script>
export default {
    data() {
      return {
        mail: "cam@tosh.fr",
        password: "toast"
      }
    },
    methods: {
      login: function () {
        const mail = this.mail
        const password = this.password
        this.$store.dispatch('login', { mail, password })
        .then(() => this.$router.push('/dashboard'))
        .catch(err => console.log(err))
      }
    }
}
</script>
