// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import store from './vuex'
import VueParticles from 'vue-particles'
// 后端接口抽象成Resource
import VueResource from 'vue-resource'
import hljs from 'highlight.js'
import VueCookies from 'vue-cookies'
import VueClip from 'vue-clip'
import VueHighlightJS from 'vue-highlightjs'

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(ElementUI)
Vue.use(VueCookies)
Vue.use(VueClip)
Vue.use(VueHighlightJS, ['cpp'])
Vue.use(VueParticles)
Vue.http.options.emulateJSON = true
Vue.http.options.headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  store,
  router,
  template: '<App/>',
  components: { App }
})

router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requireAuth)) {
    if(!localStorage.getItem('teamstyle_id')){
      //console.log('catch1')
      alert("Please login first")
      next({
        path: '/login',
      })
    } else{
      //console.log('catch2')
      next()
    }
  } else {
    //console.log('catch3')
    next()
  }
})

// 取 cookie 
function getCookie(name) {
  let arr,
      reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)")
  console.log(document.cookie)
  if(arr=window.document.cookie.match(reg)) {
    return decodeURIComponent(arr[2])
  }
}

// 设置 POST 请求时 的 data 格式
Vue.http.options.emulateJSON = true

// 设置 X-CSRFToken
Vue.http.interceptors.push(function(request, next) {
  if(request.url == '/backend/test'){
    //console.log(request)
    //request.META["CSRF_COOKIE_USED"] = 'True'
    //request.headers.set('X-CSRFToken', 'qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwer')
  }
  next()
})

Vue.directive('highlightjs', {
  deep: true,
  bind: function (el, binding) {
    // on first bind, highlight all targets
    let targets = el.querySelectorAll('code')
    targets.forEach((target) => {
      // if a value is directly assigned to the directive, use this
      // instead of the element content.
      if (binding.value) {
        target.textContent = binding.value
      }
      hljs.highlightBlock(target)
    })
  },
  componentUpdated: function (el, binding) {
    // after an update, re-fill the content and then highlight
    let targets = el.querySelectorAll('code')
    targets.forEach((target) => {
      if (binding.value) {
        target.textContent = binding.value
        hljs.highlightBlock(target)
      }
    })
  }
})