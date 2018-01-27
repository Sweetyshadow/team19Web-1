<template>
  <div>
    <p>用户名</p>
    <input v-model="username" type="text">
    <p>密码</p>
    <input v-model="password" type="password">
    <button v-on:click="login" class="submit">提交</button>
  </div>
</template>

<script>
import authSrv from '@/api/auth.js'
export default {
  name: 'Login',
  data () {
    return {

    }
  },
  components: {

  },
  methods: {
    login () {
      const {username, password, $router} = this
      const data = {
        name: username,
        pwd: password
      }
      console.log(username)
      authSrv
        .query(this, data)
        .then(rep => {
          // success call back
          if (!rep.code) {
            $router.go({
              name: 'home'
            })
          } else {
            alert(rep.code)
          }
        }, rep => {
          // error call back
          alert(rep.code)
        })
    }
  }
}
</script>

<style scoped>
  .submit{
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>
