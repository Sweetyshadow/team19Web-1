<template>
    <div id="wrap">
        <el-form :model="form" :rules="rules" ref="form" label-position="left">
            <h3>组队</h3>
            <!--el-form-item label="是否为队长">
                <el-switch 
                    v-model="form.isteamleader" 
                    disabled
                    active-color="#13ce66"
                    inactive-color="#ff4949"
                    active-text="是"
                    inactive-text="否">
                </el-switch-->
            <!--/el-form-item-->
            <el-form-item v-if="form.isteamleader" prop="teamname">
                <el-input v-model="form.teamname" placeholder="队伍名称"></el-input>
            </el-form-item>
            <el-form-item v-if="!form.isteamleader" prop="invitecode">
                <el-input v-model="form.invitecode" placeholder="邀请码"></el-input>
            </el-form-item>
            <el-form-item v-else prop="invitecode">
                <el-input v-model="form.invitecode" placeholder="设置邀请码"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">确定</el-button>
            </el-form-item>
        </el-form>
        <!--el-button @click="testLeader">testLeader</el-button!-->
        <router-link to="/ShowAllTeams"><a>查看所有队伍</a></router-link>
    </div>
</template>

<script>
import teamSrv from '@/api/team.js'
export default {
  name: 'team',
  data(){
      return{
          form: {
              isteamleader: false,
              teamname:'',
              invitecode:''
          },
          rules: {
              teamname: [
                  {
                    required: true, 
                    message: '请输入队伍名称',
                    trigger: 'blur'
                    }
              ],
              invitecode: [
                  {
                    required: true,
                    message: '请输入邀请码',
                    trigger: 'blur'
                  }
              ]
          }
      }
  },
  created() {
      this.form.isteamleader = this.$store.state.isLeader
  },
  methods: {
	    onSubmit() {
            if(this.form.isteamleader) {
                console.log('start create')
                teamSrv
                    .createTeam(this)
            } else {
                teamSrv
                    .checkCode(this)
            }
        },
        testLeader() {
            teamSrv.isLeader(this)
        }
    }
  
}
</script>

<style lang="scss" scoped>
template {
    width: 100%;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
h1{
    line-height: 1;
    text-align:center;
}
#wrap {
  width: 50%;
  margin: 40px auto;
  max-width: 400px;
}
button {
  width: 100%;
}
a {
    font-size: 12px;
}
</style>
