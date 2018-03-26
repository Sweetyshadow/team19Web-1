const FILE_URL = 'backend/download/'
export default {
  name: 'fileSrv',
  loadFile (context) {
    console.log('loading')
    return context.$http({
      url: FILE_URL+'allfiles',
      method: 'get'
    }).then(response => {
      //alert('success')
      console.log(response.body["index"])
      context.files = []
      for (var i=0;i<response.body["index"].length;i++){
        var onefile = response.body["index"][i]
        context.files.push({
          id: i,
          title: onefile,
          address: FILE_URL +'file/'+ onefile,
        })
      }
    }, response => {
      console.log('gg')
      context.title = 'faketitle'
      context.intro = 'fakeintro'
      context.address = 'fakeaddr.xx'
      context.files = [
        {
          id: 0,
          title: 'faketitle0',
          intro: 'fakeintro0',
          address: 'fakeaddr0.xx'
        },
        {
          id: 1,
          title: 'faketitle1',
          intro: 'fakeintro1',
          address: 'fakeaddr1.xx'
        }
      ]
    })
  },
  getAI (context) {
    const data = {
      userid: localStorage.getItem('teamstyle_id')
      //userid: 1
    }
    context.$http({
      url: FILE_URL+'code/',
      method: 'post',
      body: data
    }).then(response=>{
      //console.log(response)
      if(response.body.success){
        context.code = response.body
      }
    }, response => {
      alert('gg')
    })
  }
}