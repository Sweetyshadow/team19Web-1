<template>
  <div>
    <upload v-bind:isProfile="isProfile" v-bind:icon="icon" v-bind:acceptedFormat="acceptedFormat"></upload>
    <el-table :data='team' stripe>
        <el-table-column type="index"></el-table-column>
        <el-table-column prop="teamname" label="队伍名称"></el-table-column>
        <el-table-column prop="teamleader" label="队长"></el-table-column>
        <el-table-column prop="teammember" label="队员">
            <template slot-scope="scope">
                <span style="margin:2px" v-for="item in scope.row.teammember" :key="item">{{item}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="teamscore" label="得分"></el-table-column>
        <el-table-column label="操作">
            <template slot-scope="scope">
                <el-button
                size="mini"
                @click="handleBattle(scope.$index, scope.row)">对战</el-button>
            </template>
        </el-table-column>
    </el-table>
  </div>
</template>
<script>
import upload from './upload'
import teamSrv from '@/api/team.js'
export default {
  name: 'battle',
  components: {
      upload
  },
  created(){
    teamSrv.getMyteamindex(this,this.jump)
    teamSrv.showAll(this)
  },
  data(){
      return {
          isProfile: false,
          icon: "el-icon-upload",
          acceptedFormat: ['text/*'],
          team: [],
          teamid: []
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
