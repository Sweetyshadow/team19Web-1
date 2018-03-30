<template>
  <div id="app">
    <!--<img src="./assets/logo.png">!-->
    <nav-bar></nav-bar>
    <router-view/>
    <foot></foot>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import foot from './components/foot'
export default {
  name: 'app',
  components: {
    NavBar,
    foot
  }
}
</script>

<style>
#app {
  min-height: 100vh;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.footer {
  position: absolute;
  bottom: 0;
}
</style>
