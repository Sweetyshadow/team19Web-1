<template>
<div>
	<vue-clip  :options="options" :on-sending="sending" :on-complete="complete">
    <template slot="clip-uploader-action">
      <div class="uploader-icon">
				<img v-if="headurl" :src="headurl" class="dz-message">
				<i v-else :class="icon" class="dz-message"></i>
        <!--el-button class="dz-message">点击或拖拽到此处开始上传</el-button!-->
      </div>
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
		props: ['isProfile','icon','acceptedFormat'],
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
				headurl: null,
				_icon: null
      }
		},
		created(){
			if(this.isProfile) this.gethead()
		},
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
				if(status === 'error')
					alert(file.errorMessage)
				else alert(status)
				if(this.isProfile){
					this.gethead()
				} else{
					fileSrv.getAI(this.$parent)
				}
			},
			gethead() {
				console.log('click')
				authSrv.getHeadpic(this)
			}
		}

  }
</script>

<style scoped>
  .uploader-icon{
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
		font-size: 84px;
    color: #8c939d;
    width: 100px;
    height: 100px;
    line-height: 100px;
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
