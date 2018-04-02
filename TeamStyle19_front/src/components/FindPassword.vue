<template>
<div id="wrap">
  <el-form :model="form" ref="form">
      <el-form-item prop="email">
          <el-input v-model="form.email" placeholder="注册邮箱"></el-input>
      </el-form-item>
      <el-button @click="onSubmit" type="primary" :disabled="disabled">提交</el-button>
  </el-form>
  <foot></foot>
</div>
</template>
<script>
import authSrv from '@/api/auth.js'
import foot from './foot'
export default {
  name: 'findPassword',
  components:{foot},
  data(){
      return {
          form: {
              email: ''
          },
          rules: {
            email: [
              {required: true, message: '请输入您的注册邮箱'}
            ]
          }
      }
  },
  computed: {
    disabled(){
      return this.form.email === ''
    }
  },
  methods: {
      onSubmit(){
          authSrv.findPassword(this)
      }
  }
}
</script>
<style lang="scss" scoped>
template {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
#wrap {
  width: 50%;
  margin: 40px auto;
  max-width: 400px;
}
button {
  width: 100%;
}
p {
  font-size: 12px;
}
@media screen and (max-width: 720px) {
  #wrap{
    margin: 40% auto;
    width: 100%;
  }
  form{
    margin: 0 10%;
  }
}
</style>