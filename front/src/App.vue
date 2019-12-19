<template>
  <div id="app">
    <div class="bg-gray-100 h-auto min-h-screen">
      <router-view />
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(logout)
        }
        throw err;
      });
    });
  }
}

</script>