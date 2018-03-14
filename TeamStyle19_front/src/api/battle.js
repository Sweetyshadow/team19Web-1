const CODEFILE_URL = 'api/code'
import io from 'socket.io-client'
export default {
  name: 'battleSrv',
  uploadFile (context, file) {
    context.$http({
      url: CODEFILE_URL,
      method: 'post',
      params: file,
      progress: pe => {
        // render in the context
        context.data.progressbar = pe.loaded/pe.total
        return pe.loaded/pe.total
      }
    }).then(response => {
      alert('文件上传成功')
    }, response => {
      // fail call back
      alert(response.msg)
    })
  },
  /*battle (context, enemy) {
    var socket = io.connect('')
    var send_data = {
      p1: context.$store.state.userInfo,
      p2: enemy
    }
    socket.emit('startBattle', send_data)
    socket.on('progressBattle', response => {
      // render progress in context
      console.log(response)
    })
  }*/
  getBattleDetail(context,battleid){
    return context.$http({
      url: ''+battleid,
      method: 'get'
    })
  }
}