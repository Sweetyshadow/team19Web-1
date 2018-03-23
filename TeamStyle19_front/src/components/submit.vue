<template>
  <div>
      <div v-if="isWait" class="waiting">
        <img src="/static/img/kotori.gif"/>
        <p><a>对战进行中...</a></p>
      </div>
      <div v-else class="result">
        <p>{{resultDetail}}</p>         
      </div>        
  </div>
</template>
<script>
import battleSrv from '@/api/battle.js'
export default {
  name: 'submit',
  data(){
    return {
      poll: null,
      isWait: true,
      resultDetail: null
    }
  },
  created(){
    var battleid = this.$route.params.battleid
    this.getDetail(battleid)
  },
  methods: {
    getDetail(id){
      var that = this
      return new Promise((resolve,reject)=>{
        that.pollDetail(id)
        resolve()
      }).then(()=>{

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
            this.resultDetail = response.body
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
    }
  }
}
</script>

<style lang="scss" scoped>
.waiting {
  margin-top:10%;
  width: 100%;
  text-align: center;
}
img {
  margin: 0 auto;
  display: block;
}
a{
  font-size: 24px;
}
</style>
