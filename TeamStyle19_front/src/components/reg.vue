<template>
  <div id="wrap">
  <el-form :model="form" :rules="rules" ref="form" label-width="80px" label-position="left">
    <el-form-item prop="email" label="邮箱">
      <el-input v-model="form.email" placeholder="邮箱"></el-input>
    </el-form-item>
    <el-form-item prop="studentID" label="学号">
      <el-input v-model="form.studentID" placeholder="学号"></el-input>
    </el-form-item>
    <el-form-item prop="realname" label="真实姓名">
      <el-input v-model="form.realname" placeholder="真实姓名"></el-input>
    </el-form-item>
    <el-form-item prop="username" label="用户名">
      <el-input v-model="form.username" placeholder="用户名"></el-input>
    </el-form-item>
    <el-form-item prop="password" label="密码">
      <el-input v-model="form.password" type="password" placeholder="密码"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="register" size="medium" :disabled="disabled">注册</el-button>
      <router-link to="/login"><p>已有账号？点击登录</p></router-link>
    </el-form-item>
  </el-form>
  <foot></foot>
</div>
</template>

<script>
import authSrv from '@/api/auth.js'
import foot from './foot'
export default {
  name: 'Reg',
  components: { foot },
  data(){
    var mailcheck = (rule, value, callback) => {
      if (value.match(/@mails.tsinghua.edu.cn$/)) {
        callback();
      } else {
        callback(new Error("请输入清华邮箱"));
      }
    }
    var studentIDcheck = (rule, value, callback) => {
      if(value.length === 10) {
        callback();
      } else {
        callback(new Error("请输入10位学号"));
      }
    }
    var usernamecheck = (rule, value, callback) => {
      if(value.match(/ /)||value.match(/\//)) {
        callback(new Error("用户名不能包含空格或 \/"))
      } else {
        callback()
      }
    }
    return{
      form: {
        email:'',
        username:'',
        realname: '',
        password:'',
        studentID:''
      },
      rules:{
        email: [
          //{required: true, message: '请输入邮箱', trigger:'blur'},
          //{ type: 'email', message: '请输入正确的邮箱地址', trigger: 'blur,change' }
          {required: true, validator: mailcheck, trigger: 'blur,change'}
        ],
        studentID: [
          {required: true, validator: studentIDcheck, trigger: 'blur,change'}
        ],
        realname: [
          {required: true, trigger: 'blur,change'}
        ],
        username: [
          {required: true, message: '请输入用户名'},
          {max: 16, message:'用户名长度不能超过16位'},
          {validator: usernamecheck}
        ],
        password: [
          {required: true, min: 8, max: 20, message: '请输入8-20位密码', trigger:'blur,change'}
        ]
      }
    }
  },
  computed: {
    disabled(){
      return this.form.email===''||!this.form.email.match(/@mails.tsinghua.edu.cn$/)||this.form.realname===''||
             this.form.username===''||this.form.username.match(/ |\//)||this.form.password===''||this.form.studentID.length!=10
    }
  },
  methods: {
    register () {
      console.log('reg')
      authSrv
        .register(this,this.jump)
    },
    jump (context) {
      context.$router.push('/login')
    }
  }
}
</script>

<style lang="scss" scoped>
template {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
#wrap{
  padding-top: 40px;
}
.el-form {
  width: 35%;
  min-width: 400px;
  margin: 0 auto 10%;
  padding-top: 40px;
  box-sizing: border-box;
  border: solid #f4f4f4 1px;
  border-radius: 2px;
  box-shadow: 2px 2px 10px 2px rgba(211, 211, 211, 0.829);
}
.el-form-item {
  margin: 16px auto;
  margin-left: 60px;
  width: 70%;
}
button {
  width: 100%;
}
p {
  font-size: 12px;
}
@media screen and (max-width: 720px) {
  #wrap{
    margin: 30% auto;
    width: 100%;
  }
  .el-form{
    width: 95%;
    margin: 0 auto 8%;
    min-width: 0;
  }
  .el-form-item{
    margin-left: 40px;
  }
}
</style>
