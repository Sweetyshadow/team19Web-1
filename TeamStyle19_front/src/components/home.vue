<template>
<div>
  <div id="particles">
    <vue-particles 
        color="#999999"
        :particleOpacity="0.7"
        :particlesNumber="100"
        shapeType="circle"
        :particleSize="3"
        linesColor="#aaaaaa"
        :linesWidth="1"
        :lineLinked="true"
        :lineOpacity="0.4"
        :linesDistance="200"
        :moveSpeed="5"
        :hoverEffect="true"
        hoverMode="grab"
        :clickEffect="true"
        clickMode="push"
    >
    </vue-particles>
    <h1> Teamstyle19</h1>
  </div>
  <foot></foot>
</div>
</template>

<script>
import foot from './foot'
export default {
  name: 'Home',
  components: {
    foot
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
  a,a:hover,a:visited,a:link,a:active{
    text-decoration: none;
    color: inherit;
  }
  #logo{
    width: 100%;
  }
  .footer {
    position: absolute;
    top: 100vh;
  }
</style>
