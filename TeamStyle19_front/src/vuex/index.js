import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    count: 1,
    userInfo: {
      name: localStorage.getItem('teamstyle_name'),
      pwd: localStorage.getItem('teamstyle_pwd')
    }
  },
  getters: {

  },
  mutations: {
    // an example
    increment (state) {
      state.count ++
      console.log(state.count)
    },
    updateUserInfo (state, payload) {
      state.userInfo = payload
      console.log(state.userInfo)
    },
    clearUserInfo (state) {
      state.userInfo = null
      console.log('User Logout')
    }
  }
})
