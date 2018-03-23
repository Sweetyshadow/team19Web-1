<template>
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
        <a href="https://element.eleme.io/">
          <img src="/static/img/elementui.svg"/>
        </a>
        <a href="https://github.com/">
          <img src="/static/img/github.svg"/>
        </a>
      </div>
    </div>
</template>

<script>
export default {
  name: 'foot'
}
</script>

<style lang="scss" scoped>
a,a:active,a:link,a:hover,a:visited{
    text-decoration: none;
    color: black;
}  
  .footer{
    width: 100vw;
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
@media screen and(max-width:720px) {
  .footer{
    flex-direction: column;
    height:auto;
  }
  .col {
    width: 100vw;
    box-sizing: border-box;
  }
  .left {
    margin-top: 50px;
  }
  .mid{
    height: 100px;
    img {
      height: 100%;
      width: auto;
    }
  }
  .right{
    margin-bottom: 30px;
  }
}
</style>
