<template>
  <div id="app">
    <div class="bg-gray-100 h-auto min-h-screen">
      <div style="max-width: 1080px; margin: 0 auto;">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  created: function() {
    this.$http.interceptors.response.use(undefined, function(err) {
      return new Promise(function(resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(logout);
        }
        throw err;
      });
    });
  }
};
</script>
