<template>
<div>
  <ul>
    <el-card v-for="item in files" :key="item.id">
      <h4> {{item.title}} </h4>
      <!--p> {{item.intro}} </p!-->
      <el-button type="primary"><a :href="item.address">download</a></el-button>
   </el-card>
  </ul>
  <foot></foot>
</div>
</template>
<script>
import fileSrv from '@/api/file.js'
import foot from './foot'
export default {
  name: 'File',
  components:{foot},
  data () {
    return{
      files: []
    } 
  },
  created () {
    fileSrv
      .loadFile(this)
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
ul {
  margin-top: 10%;
  padding: 30px 0;
}

.el-card {
  width: 60%;
  margin: 0 auto;
  h4 {
    margin-top: 0;
  }
}
.footer {
  margin-top: 60px;
}
@media screen and(max-width: 720px){
  .el-card {
    width: 85%;
  }

}
</style>