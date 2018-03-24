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
                <el-button type="primary" @click="onSubmit" :disabled="disabled">确定</el-button>
            </el-form-item>
            <el-form-item>
                <router-link to="/ShowAllTeams"><a>查看所有队伍</a></router-link>
            </el-form-item>
        </el-form>
        <!--el-button @click="testLeader">testLeader</el-button!-->
        <foot></foot>
    </div>
</template>

<script>
import teamSrv from '@/api/team.js'
import foot from './foot'
export default {
  name: 'team',
  components: {
      foot
  },
  data(){
      var teamnamecheck = (rule,value,callback) => {
          if(value.match(/ /)||value.match(/\//)){
              callback(new Error("队名不能包含空格或\/"))
          } else {
              callback()
          }
      }
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
                    trigger: 'blur,change'
                },
                {
                    validator: teamnamecheck,
                }

              ],
              invitecode: [
                  {
                    required: true,
                    message: '请输入邀请码',
                    trigger: 'blur,change'
                  }
              ]
          }
      }
  },
  computed: {
      disabled(){
          return (this.form.isteamleader&&this.form.teamname === '')||this.form.invitecode === ''||this.form.teamname.match(/ |\//)
      }
  },
  created() {
      this.form.isteamleader = this.$store.state.isLeader
  },
  methods: {
        jump(context) {
            context.$router.push('/ShowAllTeams')
        },
	    onSubmit() {
            if(this.form.isteamleader) {
                console.log('start create')
                teamSrv
                    .createTeam(this,this.jump)
            } else {
                teamSrv
                    .checkCode(this,this.jump)
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
  margin: 60px auto;
}
form {
    width: 35%;
    max-width: 400px;
    margin: 0 auto 90px;
}
button {
  width: 100%;
}
a,a:hover,a:visited, a:active,a:link {
    text-decoration: none;
    font-size: 12px;
}
@media screen and (max-width:720px){
    form{
        margin-top: 20%;
        margin-bottom: 20%;
        width: 90%;
    }
}
</style>
