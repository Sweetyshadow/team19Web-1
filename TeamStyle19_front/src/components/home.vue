<template>
  <div>
    <h1> {{message}} </h1>
    <login-reg></login-reg>
    <dish-menu></dish-menu>
  </div>
</template>

<script>
import DishMenu from './menu'
import Login from './login'
export default {
  name: 'Home',
  data () {
    return {
      message: 'Welcome to my first vue app'
    }
  },
  components: {
    DishMenu,
    Login
  }
}
</script>
<style scoped>
  h1{
    font-size: 24px;
    font-family: 'Times New Roman',serif;
  }
</style>
