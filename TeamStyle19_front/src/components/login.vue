<template>
  <form>
    <div class='title'>
      <span v-on:click="fade1" id="log-but" v-bind:class="{fonts:faded1}">登陆</span>
      <span v-on:click="fade2" id="reg-but" v-bind:class="{fonts:faded2}">注册</span>
    </div>
    <div class='log-form' v-bind:class="{hide: faded1}">
      <div class='input-line'>
        <i class="fa fa-user-circle-o fa-lg"></i>
        <input v-model="username" type="text" placeholder="用户名">
      </div>
      <div class='input-line'>
        <i class="fa fa-key fa-lg"></i>
        <input v-model="password" type="password" placeholder="密码">
      </div>
      <button v-on:click="login" class="submit">提交</button>
    </div>
    <div class='reg-form' v-bind:class="{hide: faded2}">
      <div class='input-line'>
        <i class="fa fa-user-circle-o fa-lg"></i>
        <input v-model="username" type="text" placeholder="用户名">
      </div>
      <div class='input-line'>
        <i class="fa fa-key fa-lg"></i>
        <input v-model="password" type="password" placeholder="密码">
      </div>
      <div class='input-line'>
        <i class="fa fa-envelope fa-lg"></i>
        <input type="email" placeholder="邮箱地址">
      </div>
      <button v-on:click="register">注册</button>
    </div>
    <!--p>Count: {{ count }}</p-->
  </form>
</template>

<script>
import authSrv from '@/api/auth.js'
export default {
  name: 'Login',
  data() {
    return{
      faded1: false,
      faded2: true
    }
  },
  components: {},
  computed: {
    count () {
      return this.$store.state.count
    }
  },
  methods: {
    login () {
      // this.$store.commit('increment')
      const {username, password, $router} = this
      const data = {
        name: username,
        pwd: password
      }
      // console.log(this)
      authSrv
         .login(this, data)
    },
    register () {
      const {username, password, email} = this
      const data = {
        name: username,
        pwd: password,
        email: email
      }
      authSrv
        .register (this, data)
      console.log("trigger register")
    },
    fade1(){
      this.faded1 = false;
      this.faded2 = true;
    },
    fade2(){
      this.faded1 = true;
      this.faded2 = false;
    }
  }
}

</script>

<style lang="scss" scoped>
  form{
    width:60%;
    margin: 0 auto;
    padding-bottom: 20px;
    border: {
      width: 1px;
      style: dashed;
      color: black;
    }
  }
  .title{
    margin: 0 auto;
    padding-top: 15px;
  }
  span{
    margin: {
      left: 10%;
      right: 10%;
    }
    font-size: 1.5em;
    cursor: pointer;
  }
  input {
    margin: 0 auto;
    padding: 0;
    width:calc(100% - 30px);
    box-sizing: border-box;
    outline: none;
    border: none;
    border-bottom: {
      color: black;
      width: 2px;
      style: solid;
    }
  }
  .input-line{
    margin: 15px auto;
    width: 50%;
    height: 2em;
  }
  button{
    display: block;
    margin: 0 auto;
    padding: 0;
    width: 50%;
    height: 2em;
    border:none;
    outline: none;
    cursor: pointer;
  }
  .hide{
    display:none;
  }
  .non-hide{
    display: block;
  }
  .fonts{
    font-size: 1.25em;
  }
</style>
