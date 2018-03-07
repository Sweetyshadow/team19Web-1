<template>
  <div id="particles">
    <vue-particles 
        color="#999999"
        :particleOpacity="0.7"
        :particlesNumber="200"
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
    ></vue-particles>
    
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
      message: 'Welcome to my first vue app'
    }
  },
  components: {
    DishMenu,
    Login
  }
}
</script>
<style scoped>
  #particles{
    height: calc(100% - 70px);
  }
  #particles-js {
    height: 100%;
  }
  h1{ 
    position: absolute;
    left: 50%;
    top: 50;
  }
</style>
