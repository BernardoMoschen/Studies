<template>
  <div id="app">
    <NavBar/>
    <router-view />
  </div>
</template>

<script>

import NavBar from "@/components/Navbar/NavBar.vue"

  export default {
    components: {
      NavBar
    }
  }
</script>

<style>

</style>