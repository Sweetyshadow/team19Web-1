<template>
  <div class="echart">
      <IEcharts
      :option="line"
      :loading="loading"
      @ready="onReady"
      @click="onClick"
      resizable
    />
  </div>
</template>

<script>
import IEcharts from 'vue-echarts-v3/src/lite.js'
import 'echarts/lib/chart/line'
import 'echarts/lib/component/legend'
import 'echarts/lib/component/tooltip'
import 'echarts/lib/component/title'
import teamSrv from '@/api/team.js'
export default {
    name: 'teamPulse',
    components: {
        IEcharts
    },
    created(){
        //load data
        teamSrv.getTeamPulse(this)
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
    width: 100%;
    height: 300px;
}
</style>