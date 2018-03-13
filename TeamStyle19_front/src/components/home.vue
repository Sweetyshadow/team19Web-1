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
    height: calc(100% - 70px);
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
</style>
