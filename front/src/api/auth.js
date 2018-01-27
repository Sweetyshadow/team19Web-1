const API_URL = 'api/auth'

export default {
  name: 'authSrv',
  register (context, data) {
    return context.$http({
      url: API_URL,
      method: 'post',
      data: data
    })
  },
  query (context, data) {
    return context.$http({
      url: API_URL,
      params: data
    })
  }
}
