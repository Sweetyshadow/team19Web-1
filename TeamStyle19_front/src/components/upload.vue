<template>
<div>
	<vue-clip  :options="options" :on-sending="sending" :on-complete="complete">
    <template slot="clip-uploader-action">
				<el-button type="primary" >{{message}}</el-button>
				<i :class="icon" class="dz-message"></i>
    </template>

    <!--template slot="clip-uploader-body" slot-scope="props">
			<div v-if="props.files.length>0">
				<p>最后一次上传</p>
				{{ props.files[props.files.length-1].name }} {{props.files[props.files.length - 1].status}} {{props.files[props.files.length - 1].errorMessage}}
				<p>上传历史</p>
      	<div v-for="file in props.files" :key="file.name">
        	{{ file.name }} {{file.status}} {{ file.errorMessage}}
      	</div>
			</div>
			<div v-else>
				暂无上传记录
			</div>
			
    </template!-->

	</vue-clip>
	<!--el-button><a href="/backend/download/code">getfile</a></el-button!-->
	<!--el-button @click="gethead">gethead</el-button!-->
	
</div>
</template>

<script>
	import authSrv from '@/api/auth.js'
	import fileSrv from '@/api/file.js'
  export default {
		name: 'upload',
		props: ['isProfile','icon','acceptedFormat', 'message'],
    data () {
			var sizeLimit = this.isProfile?{limit:0.8,message:'Your file size is greater than the max file size'}:{}
      return {
				options: {
          url: '/backend/upload/file/',
					paramName: 'file',
					maxFilesize: sizeLimit,
					acceptedFiles: {
						extensions: this.acceptedFormat,
						message: 'You are uploading an invalid file'
					},
					accept: function (file, done) {
    				if (file.name.match(/ |\//)) {
      				done('文件名不能包含空格或\/')
      				return
    				}

    				done()
  				}
				},
				files: null,
				//isProfile: true,
				//headurl: null,
				_icon: null
      }
		},
		//created(){
		//	if(this.isProfile) this.gethead()
		//},
		methods: {
			sending (file, xhr, formData) {
				console.log(this.isProfile)
				this._icon = this.icon
				console.log(this._icon)
				this.icon = "el-icon-loading"
				formData.append('userid',localStorage.getItem('teamstyle_id'))
				formData.append('headpic',this.isProfile)
			},
			complete(file,status,xhr) {	
				this.icon = this._icon
				if(status === 'error'){
					//alert(file.errorMessage)
					this.$notify.error({
						message: file.errorMessage
					})
				}	else {
					//alert(status)
					this.$notify({
						message: status,
						type: 'success'
					})
				}
				if(!this.isProfile){
					if(eval('('+xhr.responseText+')').success === false) {					
						this.$parent.compileError = true
						this.$parent.ErrorDetail = eval('('+xhr.responseText+')').message
					} else {
						this.$parent.compileError = false
						this.$parent.ErrorDetail = null
					}
					fileSrv.getAI(this.$parent)
				}	else{
					this.gethead()
				} 
			},
			gethead() {
				console.log('click')
				authSrv.getHeadpic(this).then(response => {
					//console.log('success headpic')
					this.$parent.headurl = "data:image/jpeg;base64,"+response.body
				}, response => {
					//console.log('fail')
					//alert('网络状态不佳，获取头像失败')
					this.$notify.error({
						message: '网络状态不佳，获取头像失败'
					})
				})
			}
		}

  }
</script>

<style scoped>
  .uploader-icon{
    /*border: 1px dashed #d9d9d9;
    border-radius: 6px;*/
    cursor: pointer;
    position: relative;
    overflow: hidden;
		font-size: 84px;
    color: #8c939d;
    /*width: 100px;
    height: 100px;
    line-height: 100px;*/
		width: 100%;
		height: 100%;
		line-height: inherit;
    text-align: center;
  }
  .uploader-icon:hover {
    border-color: #409EFF;
  }
  img{
		height: inherit;
		width: inherit;
	}
</style>
