<template>
<div id="wrap">
    <el-button icon="el-icon-plus" type="primary" size="medium" @click="handleCreate">创建队伍</el-button>
  <el-table :data='team' stripe>
      <el-table-column type="index" align="center" header-align="center">
      </el-table-column>
      <el-table-column prop="teamname" label="队伍名称" align="center" header-align="center">
      </el-table-column>
      <el-table-column prop="teamleader" label="队长" align="center" header-align="center">
      </el-table-column>
      <el-table-column prop="teammember" label="成员" align="center" header-align="center">
      <template slot-scope="scope">
          <span style="margin:2px" v-for="item in scope.row.teammember" :key="item">{{item}}</span>
      </template>
      </el-table-column>
      <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleJoin(scope.$index, scope.row)">加入</el-button>
      </template>
    </el-table-column>
  </el-table>
  <foot></foot>
  <!--div :model="test">
      <input v-model="test.id1">
      <input v-model="test.id2">
      <input v-model="test.id3">
  </div>
  <el-button @click="handleClear">delete</el-button!-->
</div>
</template>

<script>
import teamSrv from '@/api/team.js'
import foot from './foot'
export default {
  name:'ShowAllTeams',
  components: {
      foot
  },
  data(){
      return{
          team: [],
          requireAI: false
          //teamid: [],
          /*test: {
              id1: null,
              id2: null,
              id3: null
          }*/
      }
  },
  created () {
      teamSrv.showAll(this,this.requireAI)
  },
  methods:{
      handleJoin (index,row) {
          console.log(row)
          //this.$store.commit('setTeamindex',this.teamid[index])
          this.$store.commit('setTeamindex',row.teamid)
          this.$store.commit('setisLeader',false)
          this.$router.push('/team')
      },
      handleCreate () {
          this.$store.commit('setisLeader',true)
          this.$router.push('/team')
      },
      /*handleClear(){
          teamSrv.removeMember(this)
      }*/
  }
}
</script>

<style lang="scss" scoped>
#wrap {
    max-width: 600px;
    min-width: 480px;
    margin: 40px auto;
}
.footer {
    position: absolute;
    margin-top: 60px;
    left: 0;
}
@media screen and (max-width: 720px){
#wrap {
    width: 80%;
    margin: 20% 5% 0;

}
.leader .member{
    display: none;
}
}
</style>
