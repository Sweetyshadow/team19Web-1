<template>
<div>
	<vue-clip  :options="options" :on-sending="sending" :on-complete="gethead">
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
  export default {
		name: 'upload',
		props: ['isProfile','icon'],
    data () {
      return {
				options: {
          url: '/backend/upload/file/',
					paramName: 'file',
					maxFilesize: {
    				limit: 0.8,
    				message: 'Your file size is greater than the max file size'
  				},
					acceptedFiles: {
						extensions: ['image/*'],
						message: 'You are uploading an invalid file'
					}
				},
				files: null,
				//isProfile: true,
				headurl: null
      }
		},
		created(){
			if(this.isProfile) this.gethead()
		},
		methods: {
			sending (file, xhr, formData) {
				console.log(this.isProfile)
				formData.append('userid',localStorage.getItem('teamstyle_id'))
				formData.append('headpic',this.isProfile)
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
