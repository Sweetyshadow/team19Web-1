<template>
<div id="wrap">
  <el-form :model="form" :rules="rules" ref="form">
    <el-form-item prop="username">
      <el-input v-model="form.username" placeholder="用户名"></el-input>
    </el-form-item>
    <el-form-item  prop="password">
      <el-input v-model="form.password" type="password" placeholder="密码"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="login" size="medium">登录</el-button>
      <div class="foot">
      <router-link to="/reg"><p>没有账号？点击注册</p></router-link>
      <router-link to="/find_password"><p>忘记密码？</p></router-link>
      </div>
    </el-form-item>
  </el-form>
  <foot></foot>
</div>
</template>

<script>
import authSrv from '@/api/auth.js'
import foot from './foot'
export default {
  name: 'Login',
  data() {
    return{
      form:{
        username:'',
        password:''
      },
      rules: {
        username: [
          {required: true, message: '请输入用户名'}
        ],
        password: [
          {required: true, message: '请输入密码'}
        ]
    }
    }
  },
  components: {foot},
  computed: {
    count () {
      return this.$store.state.count
    }
  },
  methods: {
    jump (context) {
      context.$router.push('/')
    },
    login () {
      console.log('lg')
      authSrv
         .login(this,this.jump)
      
    }
  }
}
</script>

<style lang="scss" scoped>
template {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
#wrap {
  margin: 60px auto;
}
.el-form {
  width: 60%;
  margin: 0 auto 7%;
  padding-top: 40px;
  box-sizing: border-box;
  border: solid #f4f4f4 1px;
  border-radius: 2px;
  box-shadow: 2px 2px 10px 2px rgba(211, 211, 211, 0.829);
}
.el-form-item {
  margin: 16px auto;
  width: 70%;
}
button {
  width: 100%;
}
p {
  font-size: 12px;
}
div.foot{
  font-size: 0;
}
div.foot p{
  display:inline-block;
  width: 50%;
}
div.foot a:first-child p{
  text-align: left;
}
div.foot a:last-child p{
  text-align: right;
}
@media screen and (max-width: 720px) {
  #wrap{
    margin: 40% auto;
    width: 100%;
  }
  .el-form{
    width: 95%;
    margin: 0 auto;
    margin-bottom: 40%;
  }
}
</style>
