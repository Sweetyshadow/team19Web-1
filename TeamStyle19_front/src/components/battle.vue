<template>
  <div class="battle">
    <div class="version">
        <p>当前平台版本：{{ version }}</p>
    </div>
    <div class="title1">
        <h4>提交代码</h4>
    </div>
    <div class="upload">
        <upload v-bind:isProfile="isProfile" v-bind:acceptedFormat="acceptedFormat"
            style="width: 150px; height: 100px; line-height: 100px;" message="上传代码"></upload>    
        <div><i class="el-icon-info">点击或拖拽上传</i></div>
        <div><i class="el-icon-warning">Note: 系统仅保留最新上传文件</i></div>
    </div>
    <div v-if="compileError" id="ErrorInfo">
        <h1>Compile Error</h1>
        <p> {{ ErrorDetail }}</p>
    </div>
    <h4> 进行对战 </h4>
    <el-table :data='team' :default-sort="{prop: 'teamscore', order: 'descending'}" stripe>
        <el-table-column type="index" align="center"></el-table-column>
        <el-table-column prop="teamname" label="队伍名称" align="center" sortable></el-table-column>
        <el-table-column prop="teamleader" label="队长" align="center" sortable></el-table-column>
        <el-table-column prop="teamscore" label="得分" align="center" sortable></el-table-column>
        <el-table-column label="操作" align="center">
            <template slot-scope="scope">
                <el-button
                size="mini"
                @click="handleBattle(scope.$index, scope.row)">对战</el-button>
            </template>
        </el-table-column>
    </el-table>
    <h4>查看代码</h4>
    <template v-if="code">
        <pre v-highlightjs><code class="cpp">{{ code }}</code></pre>
    </template>
    <template v-else>
        <p>No submit available</p>
    </template>
  </div>
</template>
<script>
import upload from './upload'
import teamSrv from '@/api/team.js'
import fileSrv from '@/api/file.js'
import battleSrv from '@/api/battle.js'
export default {
  name: 'battle',
  components: {
      upload,
  },
  created(){
    teamSrv.getMyteamindex(this,this.jump)
    teamSrv.showAll(this,this.requireAI)
    fileSrv.getAI(this)
    /*battleSrv.getPlatformVersion(this).then(response => {
        if(response.body.success) {
            this.version = response.body.version
        }
    }, response => {
        this.version = '暂无数据'
    })*/
  },
  data(){
      return {
          version: 'latest',
          isProfile: false,
          icon: "el-icon-upload",
          acceptedFormat: [],
          team: [],
          //teamid: [],
          compileError: false,
          ErrorDetail: null,
          code: null,
          requireAI: true
      }
  },
  methods: {
      jump (context) {
          context.$router.push('/ShowAllTeams')
          //context.$router.push(path)
      },
      jumpwithParam (context, battleid) {
          context.$store.commit('setBattleid',battleid)
          context.$router.push({name: 'submit', params: { battleid:battleid }})
      },
      handleBattle(index,row){
          const data = {
              team1: this.$store.state.teamindex,
              team2: row.teamid
          }
          if(this.$store.state.teamindex!=null){
              if(data.team1===data.team2){
                  //alert('您不能和自己的队伍对战')
                  this.$notify({
                      message: '您不能和自己的队伍对战',
                      type: 'warning'
                  })
                  return
              }
              console.log('start battle')
              teamSrv.startBattle(this,data,this.jumpwithParam)
          } else {
              //alert('获取队伍信息失败')
              this.$notify.error({
                  message: '获取队伍信息失败'
              })
          }
      }
  }
}
</script>

<style lang="scss" scoped>
.battle {
    width: 80%;
    margin: 0 auto;
}
.version {
    p {
        font-size: 12px;
        margin-top: 10px;
    }
}
#ErrorInfo{
    background: #ffc;
}
.el-table{
    width: 640px;
    margin: 20px auto;
    border: 1px solid rgb(235,238,245);
    border-bottom: none;
}
code {
    font-family: '5efe7697695c42a99b24705c46f7ca0c','Source Code Pro';
    font-size: 14px;
    margin: 0 auto;
    min-width: 640px;
    max-width: 1200px;
}
    h4{
        margin-top: 24px;
        margin-bottom: 6px;
    }
.title1,.version{
    display: inline-block;
}
.version {
    float: right;
    margin-right: 12px;
}
.footer {
    position: absolute;
    margin-top: 60px;
    left: 0;
}
.upload {
    margin: 0;
    div {
        margin: 6px 0;
    }
}
i {
    font-size: 14px;
}
</style>
