<template>
  <div id="wrap">
      <div class="column right">
        <h1>{{teamname}}</h1>
        <p v-if="isleader"> 邀请码： {{invitecode}}</p>
      </div>
      <div class="column left">
        <upload message="上传头像" v-bind:isProfile="isProfile" v-bind:icon="icon" v-bind:acceptedFormat="acceptedFormat" style="width: 100px; height: 100px; line-height: 100px"></upload>
      </div>      
        <el-table :data="team" :span-method="arraySpanMethod" stripe border>
            <el-table-column prop="leader" label="队长" align="center">
            </el-table-column>
            <el-table-column prop="member" label="队员" align="center">
            </el-table-column>
            <el-table-column label="操作" v-if="isleader" align="center">
                <template slot-scope="scope">
                    <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <div>
            <h1>Battle History</h1>
            <el-table :data="history">
                <el-table-column type="index">
                </el-table-column>
                <el-table-column prop="time" label="对战时间" align="center">
                </el-table-column>
                <el-table-column label="回放文件">
                    <template slot-scope="rpy">
                        <el-button size="mini" type="primary" @click="handleDownload(rpy.$index, rpy.row)">下载</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
  </div>
</template>

<script>
import upload from './upload'
import teamSrv from '@/api/team.js'
export default {
  name: 'teamProfile',
  components: {
      upload
  },
  data() {
      return {
          team: [],
          history: [],
          //memberid: [],
          isleader: true,
          teamname: null,
          invitecode: null,
          isProfile: true,
          icon: "el-icon-plus",
          acceptedFormat: ['image/*']
      }
  },
  created(){
      //if(this.$store.state.isLeader!=null){
      //    this.isleader = this.$store.state.isLeader
      //} else {
          teamSrv.isLeader(this)
      //}
      teamSrv.showMyteam(this)
      this.renderBattleHistory(localStorage.getItem('teamstyle_id'))
  },
  methods: {
      handleDelete(index, row){          
        teamSrv.removeMember(this,this.team[index].member,teamSrv.showMyteam)          
      },
      arraySpanMethod({ row, column, rowIndex, columnIndex }) {
        if ( columnIndex == 0 ){
            if( rowIndex == 0){
                console.log(row)
                return [this.team.length,1]
            } else if( rowIndex >0){
                return [0,0]
            }
        }
      },
      renderBattleHistory(userid){
          if(!this.$store.state.teamindex){
              teamSrv.getMyteamindex(this,this.jump)
          }
          teamSrv.getBattleHistory(this,this.$store.state.teamindex).then(response => {
              console.log(response)
              if(response.body.success){
                  //bind data
              } else {
                  alert(response.body.message)
              }
          }, response => {
              alert('fail to get battle history')
          })
      }
  }
}
</script>

<style lang="scss" scoped>
div#wrap{
    max-width: 600px;
    min-width: 480px;
    margin: 40px auto;
    float:d
}
div.column{
    display: inline-block;
    vertical-align: top;
}
div.left{
    width: 30%;
}
div.right{
    width: 60%;
}
h1{
    text-align: left;
    font-size: 24px;
}
</style>
