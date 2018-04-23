<template>
  <div id="wrap">
    <h3>修改密码</h3>
    <el-form :model="form" :rules="rules" ref="form">
      <!--el-form-item label="原密码" prop="opwd">
          <el-input type="password" v-model="form.opwd"></el-input>
      </el-form-item!-->
      <el-form-item prop="pwd">
        <el-input type="password" v-model="form.pwd" placeholder="新密码" clearable></el-input>
      </el-form-item>
      <el-form-item prop="apwd">
        <el-input type="password" v-model="form.apwd" placeholder="请再次输入新密码" clearable></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="modify" :disabled="disable"> 确定 </el-button>
      </el-form-item>
    </el-form>
    <foot></foot>
  </div>
</template>
<script>
  import authSrv from '@/api/auth.js'
  import foot from './foot'
  export default {
    name: 'PwdChange',
    components: {
      foot
    },
    data() {
      var pwdcheck = (rule, value, callback) => {
        if (value === '') {
          callback(new Error("请输入密码"));
        } else {
          callback();
        }
      }
      var pwdcheck1 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.form.pwd) {
          callback(new Error('两次输入密码不一致'))
        } else {
          callback();
        }
      }
      return {
        form: {
          pwd: '',
          apwd: ''
        },
        rules: {
          pwd: [{
            validator: pwdcheck,
            trigger: 'blur'
          }],
          apwd: [{
            validator: pwdcheck1,
            trigger: 'blur'
          }]
        }
      };
    },
    computed: {
      disable() {
        return (this.form.pwd === '') || (this.form.pwd != this.form.apwd)
      }
    },
    methods: {
      jump(context) {
        context.$router.push('./login')
      },
      modify() {
        authSrv.modify(this, this.jump)
      }
    }
  }

</script>
<style lang="scss" scoped>
  #wrap {
    min-width: 400px;
    max-width: 480px;
    margin: 0 auto;
  }

  button {
    width: 100%;
  }

  h3 {
    text-align: center;
  }

  @media screen and (max-width:720px) {
    #wrap {
      max-width: 480px;
      min-width: 240px;
      margin: 0 20%;
      margin-top: 30%;
    }
  }

</style>
