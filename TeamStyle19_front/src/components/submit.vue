<template>
  <div>
      <div v-if="isWait" class="waiting">
        <img src="/static/img/kotori.gif"/>
        <p><a>对战进行中...</a></p>
      </div>
      <div v-else class="result">
        <!--p>{{resultDetail}}</p!-->
        <el-table :data="resultDetail">
          <el-table-column prop="result" label="结果"></el-table-column>
          <el-table-column prop="time" label="对战时间"></el-table-column>
          <el-table-column prop="round" label="回合数"></el-table-column>
        </el-table>         
      </div>  
      <foot></foot>      
  </div>
</template>
<script>
import battleSrv from '@/api/battle.js'
import foot from './foot'
export default {
  name: 'submit',
  components: { foot },
  data(){
    return {
      poll: null,
      isWait: true,
      resultDetail: null
    }
  },
  created(){
    var battleid = this.$store.state.battleid
    if(battleid!=null)  this.getDetail(battleid)
    else this.isWait = false
  },
  methods: {
    getDetail(id){
      var that = this
      return new Promise((resolve,reject)=>{
        that.pollDetail(id)
        resolve()
      }).then(()=>{
        that.$store.commit('setBattleid',null)
      }).catch(error=>{
        reject(error)
      })  
    },
    pollDetail(id) {
      const duration = 3600 * 1000
      const endTime = Number(new Date()) + duration
      this.poll = setInterval(() => {
        battleSrv.getBattleDetail(this,id).then(response => {
          if(response.body.success) {
            //bind data
            this.isWait = false
            var detail = response.body
            console.log(detail)
            this.resultDetail = [{
              result: this.mapResult(detail.result),
              time: detail.battle_time,
              round: detail.total_round
            }]
            clearInterval(this.poll)
            
          }
          else if (Number(new Date()) > endTime) {
            clearInterval(this.poll)
            console.log('time out')
          }
        }).catch(error => {
          clearInterval(this.poll)
        })
      }, 1000)
    },
    mapResult(result){
      switch(result){
        case "0": return "You are victorious!"
        case "1": return "You lose."
        case "2": return "Draw!"
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.waiting {
  width: 100%;
  text-align: center;
}
img {
  margin: 2% auto;
  display: block;
}
a{
  font-size: 24px;
}
</style>
