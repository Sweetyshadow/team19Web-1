<template>
<div>
    <el-container>
        <el-aside width="100px">
            <el-menu router mode="vertical" default-active="1">
                <el-menu-item index="1" route="/MyTeam/profile">profile</el-menu-item>
                <el-menu-item index="2" route="/MyTeam/pulse">pulse</el-menu-item>
                <!--el-menu-item index="3" route="/MyTeam/upload">上传头像</el-menu-item!-->
            </el-menu>
        </el-aside>
        <el-main>
            <router-view></router-view>
        </el-main>
    </el-container>
    
</div>
</template>


<script>
/*import teamSrv from '@/api/team.js'
export default {
  name: 'MyTeam',
  data() {
      return {
          team: [],
          //memberid: [],
          isleader: true,
          teamname: null
      }
  },
  created(){
      //if(this.$store.state.isLeader!=null){
      //    this.isleader = this.$store.state.isLeader
      //} else {
          teamSrv.isLeader(this)
      //}
      teamSrv.showMyteam(this)
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
  }
}*/
</script>


<style lang="scss" scoped>
section {
    height: calc(100vh - 61px);
    width: 100%;
}
aside ul {
    height: 100%;
}
</style>
