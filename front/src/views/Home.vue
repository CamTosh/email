<template>
  <div id="app">
    <router-view/>
  </div>
</template>
<script>
  export default {
    mounted() {
      if(this.$store.getters.isLoggedIn) {
        this.$router.push('/dashboard')
      } else {
        this.$router.push('/login')
      }
    },
  }
</script>
