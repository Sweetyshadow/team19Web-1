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
    <div class="footer">
      <div class="col left">
        <h4> 联系我们</h4>
        <p><a> EESAST</a><p>
        <p><a href="https://github.com/eesast/TeamStyle19-BUG-Report/issues/new">问题反馈</a></p>
      </div>
      
      <div class="col mid">
        <img src="/static/img/logo_main_metal.png"/>
      </div>
            
      <div class="col right">
        <h4>技术支持</h4>
        <a href="https://www.djangoproject.com/">
          <img src="/static/img/django.svg" />
        </a>
        <a href="https://www.docker.com/">
          <img src="/static/img/docker.svg"/>
        </a>
        <a href="https://cn.vuejs.org/">
          <img src="static/img/vue.png"/>
        </a>
        <a href="element.eleme.io/">
          <img src="/static/img/elementui.svg"/>
        </a>
        <a href="https://github.com/">
          <img src="/static/img/github.svg"/>
        </a>
      </div>
    </div>
    <!--el-footer>
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
    </el-footer-->
    <foot></foot>
  </div>
</template>

<script src="particles.js"></script>
<script>
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
<style lang="scss" scoped>
  #particles{
    height: 100vh;
    position:absolute;
    top: 0;
    width: 100%;
    //border-bottom: solid #f1f1f1 2px;
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
  .footer{
    width: 100%;
    height: 150px;
    display: flex;
    flex-direction: row;
  }
  .col{
    margin: 0;
    vertical-align: middle;
    box-sizing: content-box;

  }
  .left{
    order: 1;
    width: 25%;
    padding: 0 70px;
    vertical-align: middle;
    text-align: center;
    align-items: flex-start;
    p {
      margin: 10px;
    }
    a {
      font-size: 14px;
    }
    h4 {
      margin-bottom: 10px;
      padding-bottom: 10px;
      border-bottom: solid #f0f0f0 1px;
    }
  }
  .mid{
    order: 2;
    width: 30%;
    vertical-align: middle;
    display: flex;
    img {
      margin: auto;
      width: 100%;
      align-items: center;
    }
  }
  .right {
    order: 3;
    width: 25%;
    padding: 0 70px;
    text-align: center;
    align-items: flex-start;
    img {
      width: 30px;
      height: 30px;
    }
    h4 {
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: solid #f0f0f0 1px;
    }
  }

  
  a,a:hover,a:visited,a:link,a:active{
    text-decoration: none;
    color: inherit;
  }
  #logo{
    width: 100%;
  }
</style>
