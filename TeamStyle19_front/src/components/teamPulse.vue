<template>
<div>
  <div class="echart">
      <IEcharts
      :option="line"
      :loading="loading"
      @ready="onReady"
      @click="onClick"
      resizable
    />
  </div>
  <foot></foot>
</div>
</template>

<script>
import IEcharts from 'vue-echarts-v3/src/lite.js'
import 'echarts/lib/chart/line'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'
import foot from './foot'
import teamSrv from '@/api/team.js'
export default {
    name: 'teamPulse',
    components: {
        IEcharts,
        foot
    },
    created(){
        //load data
        teamSrv.getTeamPulse(this,{userid: localStorage.getItem('teamstyle_id')}).then(response => {
            //context.line.xAxis.data = response.body.score.map(function (item) {
            // return item[0];
            //})
            //context.line.series[0].data = response.body.score.map(function (item) {
                //return item[1];
            //})
            console.log(response)
            var scores = response.body.score
            scores.forEach(element => {
                this.line.xAxis.data.push(element.time)
                this.line.series[0].data.push(parseFloat(element.score))
            })
        }, response => {
            context.line.xAxis.data = ['N/A','N/A','N/A','N/A','N/A']
            context.line.series[0].data = [0,0,0,0,0]
            alert('网络状态不佳')
        })
        teamSrv.get
    },
    data () {
        return {
            loading: true,
            line: {
                title: {
                    text: 'Team Scores'
                },
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    name: '对战历史',
                    data: []
                },
                yAxis: {
                    name: 'score',
                },
                series: [{
                    name: 'Score',
                    type: 'line',
                    data: [],
                    smooth: true
                }]
            }
        }
    },
    methods: {
        onReady(instance, ECharts) {
        //console.log(instance, ECharts);
        this.loading = false
      },
        onClick(event, instance, ECharts) {
        //console.log(arguments);
      }
    }
}
</script>

<style lang="scss" scoped>
.echart {
    margin: 0 auto;
    width: 80%;
    height: 300px;
    margin-top: 10%;
}
.footer {
    position: absolute;
    left: 0;
    bottom: 0;
}
</style>