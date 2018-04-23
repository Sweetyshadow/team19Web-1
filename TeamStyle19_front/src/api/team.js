const TEAM_URL = '/backend/teams/'
const USER_URL = '/backend/students/' // 后可再加子域名
//import io from 'socket.io-client'
export default {
  name: 'teamSrv',
  notLogin () {
    return !localStorage.getItem('teamstyle_id')
  },
  showAll (context,requireAI) {
    console.log('loading')
    context.$http({
      url: TEAM_URL+'allteam',
      method: 'get',
    }).then(response => {
      context.team = []
      context.teamid = []
      for(var i in response.body){
        if(!requireAI || (requireAI&&response.body[i].hasAI)){
          context.team.push({
            teamname: response.body[i].teamname,
            teamleader: response.body[i].leader,
            teamid: response.body[i].teamid,
            teamscore: parseFloat(response.body[i].score),
            teammember: []
          })
          for(var j=1;j<response.body[i].scale;j++){
            if(response.body[i]["member"+j]) context.team[context.team.length-1].teammember.push(response.body[i]["member"+j])
          }
        }
        //context.teamid.push(response.body[i].teamid)
      }
      //console.log(context.teamid)
      //console.log(context.team)
      //console.log(response.body)
    }, response => {
      console.log('网络状态不佳')
      context.team = [{
        teamname: 'efsdgrfuioahfioasufhasui',
        teamleader: '张狗蛋',
        teammember: ['fake1','fake2','fake3']
    },
    {
        teamname: '阿斯顿v哈稍等v阿达VS的VS v的',
        teamleader: 'sdv33659d6fgdgf',
        teammember: []
    }]
    })
  },

  getMyteamindex (context,cb) {
    const data = {
      userid: localStorage.getItem('teamstyle_id')
    }
    context.$http({
      url: TEAM_URL+'oneteam/',
      method: 'POST',
      body: data // userid
    }).then(response => {
      if(response.body.success){
        context.$store.commit('setTeamindex',response.body.teamid)
      } else {
        //alert(response.body.message)
        context.$notify.error({
          message: response.body.message
        })
        if (typeof cb === 'function'){
          cb(context)
        }
      }
    }, response => {
      //alert('网络状态不佳')
      context.$notify.error({
        message: '网络状态不佳'
      })
    })
  },

  queryteamindex (context, userid) {
    return context.$http({
      url: TEAM_URL+'oneteam/',
      method: 'POST',
      body: {userid: userid} // userid 
    })
  },

  showMyteam (context) {
    const data = {
      userid: localStorage.getItem('teamstyle_id')
    }
    context.$http({
      url: TEAM_URL+'oneteam/',
      method: 'POST',
      body: data // userid
    }).then(response => {
      //console.log(response.body)
      if(response.body.success == true){
        context.teamname = response.body.teamname
        context.invitecode = response.body.invitecode
        context.team = []
        for(var i = 1;i<response.body.scale;i++){
          if(response.body["member"+i]!=null) 
            context.team.push({member:response.body["member"+i]})
        }
          context.team[0].leader = response.body.leader
      } else{
        //alert(response.body.message)
        context.$notify.error({
          message: response.body.message
        })
      }
      console.log(context.team)
    }, response => {
      console.log(response.status)
      context.team = [{member:'fake1'},{member:'fake2'},{member:'fake3'}]
    })
  },

  getTeamPulse (context,data) {
    return context.$http({
      url: TEAM_URL+'score/',
      method: 'post',
      body: data
    })
  },

  isLeader (context) {
    if(!localStorage.getItem('teamstyle_id')){
      //alert('请先登录再进行操作')
      context.$router.push('/login')
    } else {
      context.$http({
        url: USER_URL+'leader/',
        method: 'POST',
        body: {
          userid: localStorage.getItem('teamstyle_id')
        }
      }).then(response => {
        //console.log(response.body)
        context.isleader = response.body.isleader
        context.$store.commit('setisLeader',response.body.isleader)
      }, response => {
        //console.log(response.status)
      })
    }
  },

  createTeam (context,cb) {
    if(!localStorage.getItem('teamstyle_id')){
      //alert('登录状态丢失，请先登录')
      context.$notify({
        message: '登录状态丢失，请先登录',
        type: 'warning'
      })
      context.$router.push('/login')
    } else{
      const data = {
        userid: localStorage.getItem('teamstyle_id'), // 用户id
        teamname: context.form.teamname,
        invitecode: context.form.invitecode
      }
      context.$http({
        url: TEAM_URL+'add/',
        method: 'post',
        body: data,
        //timeout: 1000
      }).then(response => {
        if(response.body.success == true){
          //alert('success')
          context.$notify({
            message: 'success',
            type: 'success'
          })
        } else {
          //alert(response.body.message)
          context.$notify.error({
            message: response.body.message
          })
        }
        //jump to my team
        if(typeof cb==='function'){
          cb(context)
        }
      }, response => {
        //alert('网络状态不佳')
        context.$notify.error({
          message: '网络状态不佳'
        })
      })
    }
  },
  
  checkCode (context, cb) {
    if(!localStorage.getItem('teamstyle_id')){
      //alert('请先登录再进行操作')
      context.$notify({
        message: '请先登录再进行操作',
        type: 'warning'
      })
      context.$router.push('/login')
    } else{
      const data = {
        userid: localStorage.getItem('teamstyle_id'), // 用户id
        teamid: context.$store.state.teamindex,
        invitecode: context.form.invitecode
      }
      console.log(data)
      context.$http({
        url: TEAM_URL+'join/', // 校验验证码
        method: 'post',
        body: data,
        timeout: 1000
      }).then(response => {
        if(response.body.success == true){
          //alert('success')
          context.$notify({
            message: 'success',
            type: 'success'
          })
        } else{
          //alert(response.body.message)
          context.$notify.error({
            message: response.body.success
          })
        }
        //jump to my team
        if(typeof cb==='function'){
          cb(context)
        }
      }, response => {
        console.log(response)
        // 校验失败
        //alert('fail')
        context.$notify.error({
          message: '网络状态不佳'
        })
      })
    }
  },

  removeMember (context, data, cb) {
    //var membersid = []
    //if(context.test.id1!=null) membersid.push(context.test.id1)
    //if(context.test.id2!=null) membersid.push(context.test.id2)
    //if(context.test.id3!=null) membersid.push(context.test.id3)
    //console.log(data)
    context.$http({
      url: TEAM_URL+'exit/',
      method: 'post',
      body: {name:data}
    }).then(response => {
      //console.log(response)
      //alert('success')
      context.$notify({
        message: 'success',
        type: 'success'
      })
      if(typeof cb == 'function'){
        cb(context)
      }
    }, response => {
      //alert('网络状态不佳')
      context.$notify.error({
        message: '网络状态不佳',
      })
    })
  },
  resetCode (context,data){
    context.$http({
      url: TEAM_URL,
      method: 'post',
      params: data
    }).then(response => {
      //change context
      //console.log('reset code success')
    }, response => {
      //console.log('gg')
    })
  },
  startBattle (context, data, cb){
    context.$http({
      url: TEAM_URL+'battle/',
      method: 'post',
      body: data
    }).then(response => {
      //console.log(response)
      if(response.body.success){
        if(typeof cb==='function'){
          //console.log(response.body.battleid)
          cb(context,response.body.battleid)
        }
      } else {
        //alert(response.body.message)
        context.$notify.error({
          message: response.body.message,
        })
      }
    }, response => {
      //alert('网络状态不佳')
      context.$notify.error({
        message: '网络状态不佳'
      })
    })
  },
  getBattleHistory(context,userID){
    return context.$http({
      url: TEAM_URL+'history/',
      method: 'post',
      body: {user:userID}
    })
  },
  getRpy(context,battleid) {
    return context.$http({
      url: TEAM_URL+'record/',
      method: 'post',
      body: {battleid: battleid}
    })
  },
  getChallengeTimes(context,teamid) {
    return context.$http({
      url: TEAM_URL+'battletime/',
      method: 'post',
      body: {teamid: teamid}
    })
  }
}