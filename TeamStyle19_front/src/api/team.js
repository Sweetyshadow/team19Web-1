const TEAM_URL = 'api/team'
const USER_URL = 'api/user' // 后可再加子域名

export default {
  name: 'teamSrv',
  createTeam (context, data) {
    context.$http({
      url: TEAM_URL,
      method: 'post',
      params: data,
      timeout: 1000
    }).then(response => {
      context.$http({
        url: USER_URL,
        method: 'post',
        params: context.$store.state.userInfo,
        timeout: 1000
      }).then(response2 => {
        context.$store.commit('beLeader')
      }, response2 => {
        alert(response2.msg)
      }) 
    }, response => {
      alert(response.msg)
    })
  },
  
  checkCode (context, data) {
    context.$http({
      url: TEAM_URL, // 校验验证码
      method: 'get',
      params: data,
      timeout: 1000
    }).then(response => {
      context.$http({
        url: TEAM_URL, // 更新队员
        method: 'post',
        params: context.$store.state.userInfo,
        timeout: 1000
      }).then(response2 => {
        // 页面显示成功加入队伍
        alert('成功入队') 
      }, response2 => {
        // 入队失败
        alert(response2.msg)
      })
    }, response => {
      // 校验失败
      alert(response.msg)
    })
  },

}