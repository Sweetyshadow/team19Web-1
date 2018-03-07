<template>
  <ul>
    <el-card v-for="item in files" :key="item.id">
      <h2> {{item.title}} </h2>
      <!--p> {{item.intro}} </p!-->
      <el-button type="primary"><a :href="item.address">download</a></el-button>
   </el-card>
  </ul>
</template>
<script>
import fileSrv from '@/api/file.js'
export default {
  name: 'File',
  data () {
    return{
      files: []
    } 
  },
  created () {
    fileSrv
      .loadFile(this)
  },
  components: {

  },
  methods: {

  }
}
</script>
<style lang="scss" scoped>
a,a:hover,a:link,a:active,a:visited {
  text-decoration: none;
  color: white;
}
</style>