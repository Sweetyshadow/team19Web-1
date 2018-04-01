<template>
<div id="wrap">
  <div id="particles">
    <vue-particles 
        color="#999999"
        :particleOpacity="0.7"
        :particlesNumber="50"
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
</div>
</template>

<script>
export default {
  name: 'Home',
}
</script>
<script src="particles.js"></script>

<style lang="scss" scoped>
#wrap {
  height: 100%;
  width: 100%;
}
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
    font-size: 64px;
    margin: 0;
    top: 20%;
    left: calc(50% - 180.54px);
    text-align: center;
    font-family: 'Megrim', cursive;
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
  @media screen and (max-width:720px) {
    h1 {
      font-size: 56px;
      top: 30%;
      left: calc(50% - 157.97px);
    }
  }
</style>
