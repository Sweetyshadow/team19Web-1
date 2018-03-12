<template>
  <div>
    <p>Submit Your Code and Start Combating Today!</p>
    <upload v-bind:isProfile="isProfile" v-bind:icon="icon" v-bind:acceptedFormat="acceptedFormat"></upload>
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
    <textarea v-model="code" cols="100" rows="30"></textarea>
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
    teamSrv.showAll(this)
    fileSrv.getAI(this)
  },
  data(){
      return {
          isProfile: false,
          icon: "el-icon-upload",
          acceptedFormat: ['*/*'],
          team: [],
          teamid: [],
          code: "No sumbit available!"
      }
  },
  methods: {
      jump (context) {
          context.$router.push('/ShowAllTeams')
      },
      handleBattle(index,row){
          const data = {
              team1: this.$store.state.teamindex,
              team2: this.teamid[index]
          }
          if(this.$store.state.teamindex!=null){
              console.log('start battle')
              teamSrv.startBattle(this,data)
          }
      }
  }
}
</script>

<style lang="scss" scoped>
.el-table{
    width: 640px;
    margin: 20px auto;
    border: 1px solid rgb(235,238,245);
    border-bottom: none;
}
</style>
