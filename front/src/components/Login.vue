<template>
<div class="container mx-auto">
    <div class="flex justify-center px-6 my-12">
        <!-- Row -->
        <div class="w-full flex justify-center ">
            <!-- Col -->
            <div class="w-full lg:w-1/2 bg-white p-5 rounded-lg lg:rounded-l-none">
                <h3 class="pt-4 text-2xl text-center">Bon retour !</h3>
                <form class="px-8 pt-6 pb-8 mb-4 bg-white rounded">
                    <div class="mb-4">
                        <label class="block mb-2 text-sm font-bold text-gray-700" for="mail">
                            Email
                        </label>
                        <input v-model="mail" class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="mail" type="text" placeholder="email" />
                    </div>
                    <div class="mb-4">
                        <label class="block mb-2 text-sm font-bold text-gray-700" for="password">
                            Mot de passe
                        </label>
                        <input v-model="password" class="w-full px-3 py-2 mb-3 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline" id="password" type="password" placeholder="******************" />
                    </div>
                    <div class="mb-6 text-center">
                        <button @click='login()' class="w-full px-4 py-2 font-bold text-white bg-blue-500 rounded-full hover:bg-blue-700 focus:outline-none focus:shadow-outline" type="button">
                            Se connecter
                        </button>
                    </div>
                    <hr class="mb-6 border-t" />
                    <div class="text-center">
                        <a class="inline-block text-sm text-blue-500 align-baseline hover:text-blue-800" href="/register">
                            Créer un compte !
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
