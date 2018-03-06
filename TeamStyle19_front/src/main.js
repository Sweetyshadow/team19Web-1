// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './vuex'

// 后端接口抽象成Resource
import VueResource from 'vue-resource'

Vue.config.productionTip = false
Vue.use(VueResource)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: { App }
})

router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requireAuth)) {
    if(!localStorage.length || 
      !localStorage.getItem('teamstyle_name') || 
      !localStorage.getItem('teamstyle_pwd')){
      next({
        path: '/login',
      })
    } else{
      next()
    }
  } else {
    next()
  }
})