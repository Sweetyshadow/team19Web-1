<template>
  <div id="particles">
    <vue-particles 
        color="#999999"
        :particleOpacity="0.7"
        :particlesNumber="150"
        shapeType="circle"
        :particleSize="2"
        linesColor="#aaaaaa"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="150"
        :moveSpeed="3"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
    >
    </vue-particles>
    <h1> Teamstyle19</h1>
    <el-footer>
      <div class="column">
        <div class="left">
          <p>联系我们</p>
        </div>
        <div class="right">
          <p><a>EESAST</a></p>
          <p><a href="https://github.com/eesast/TeamStyle19-BUG-Report/issues/new">BUG反馈</a></p>
        </div>
      </div>
      <div class="column">
        <div class="left">
          <p>技术支持</p>
        </div>
        <div class="right">
          <el-tag><a href="https://www.djangoproject.com/">Django</a></el-tag>
          <el-tag><a href="https://www.docker.com/">Docker</a></el-tag>
          <el-tag><a href="https://cn.vuejs.org/">Vue</a></el-tag>
          <el-tag><a href="element.eleme.io/">ElementUI</a></el-tag>
          <el-tag><a href="https://github.com/">GitHub</a></el-tag>
        </div>
      </div>
      <div class="column">
        <img id="logo" src="../../static/img/logo.jpg">
      </div>
    </el-footer>
  </div>
</template>

<script src="particles.js"></script>
<script>
import DishMenu from './menu'
import Login from './login'
export default {
  name: 'Home',
  data () {
    return {
      //message: 'Welcome to my first vue app'
    }
  },
  components: {
    //DishMenu,
    //Login
  }
}
</script>
<style scoped>
  #particles{
    height: calc(100% - 60px);
    position:absolute;
    width: 100%;
  }
  #particles-js {
    height: 100%;
  }
  h1{ 
    position: absolute;
    margin: 0;
    top: 20%;
    left: calc(50% - 180.54px);
    text-align: center;
    font-family: 'Megrim', cursive;
    font-size: 64px;
    cursor: default;
  }
  .column{
    display: inline-block;
    width: 33%;
    vertical-align: middle;
  }
  .column .left{
    display:inline-block;
    width: 35%;
    vertical-align: top;
  }
  .column .right{
    display: inline-block;
    width: 60%;
    color:gray;
    font-size: 80%;
  }
  a,a:hover,a:visited,a:link,a:active{
    text-decoration: none;
    color: inherit;
  }
  #logo{
    width: 100%;
  }
</style>
