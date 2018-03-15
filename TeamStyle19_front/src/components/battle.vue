<template>
  <div>
    <p>Submit Your Code and Start Combating Today!</p>
    <upload v-bind:isProfile="isProfile" v-bind:icon="icon" v-bind:acceptedFormat="acceptedFormat"></upload>
    <div v-if="compileError" id="ErrorInfo">
        <h1>Compile Error</h1>
        <p> {{ ErrorDetail }}</p>
    </div>
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
    <p>View your submit</p>
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
export default {
  name: 'battle',
  components: {
      upload
  },
  created(){
    teamSrv.getMyteamindex(this,this.jump)
    teamSrv.showAll(this,this.requireAI)
    fileSrv.getAI(this)
  },
  data(){
      return {
          isProfile: false,
          icon: "el-icon-upload",
          acceptedFormat: [],
          team: [],
          //teamid: [],
          compileError: true,
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
          context.$router.push({name: 'submit', params: { battleid:battleid }})
      },
      handleBattle(index,row){
          const data = {
              team1: this.$store.state.teamindex,
              team2: row.teamid
          }
          if(this.$store.state.teamindex!=null){
              console.log('start battle')
              teamSrv.startBattle(this,data,this.jumpwithParam)
          } else {
              alert('获取队伍信息失败')
          }
      }
  }
}
</script>

<style lang="scss" scoped>
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
/*span {
    font-family: inherit;
    font-size: inherit;
}*/
</style>
