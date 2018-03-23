<template>
<div>
    <el-menu :default-active="activeIndex" mode="horizontal" router class="PC" id="menu" @click="indexupdate(activeIndex)">
        <el-menu-item index="1"><a href="https://eesast.com"><img src="/static/img/EESAST.png"/></a></el-menu-item>
        <el-menu-item index="2" route="/"> 主页 </el-menu-item>
        <el-menu-item index="3" route="/file"> 文件 </el-menu-item>
        <el-menu-item index="4" route="/ShowAllTeams"> 队伍 </el-menu-item>
        <el-menu-item index="5" route="/battle"> 对战 </el-menu-item>
        <el-submenu index="6" id="submenu" > 
            <template slot="title">个人中心</template>
            <el-menu-item index="6-1" route="/teamprofile">个人信息</el-menu-item>
            <el-menu-item index="6-2" route="/teampulse">比分变化</el-menu-item>
            <el-menu-item index="6-3" route="/" @click="logout" v-if="hasLogin">退出登录</el-menu-item>
        </el-submenu>
        <el-menu-item index="7" v-if="hasLogin" id="profile">
            <span> {{username}} </span>
        </el-menu-item>
        <el-menu-item index="8" v-else id="log" route="/login"> 登录|注册 </el-menu-item>
    </el-menu>
    <div class="navbar">
        <img src ='/static/img/menu.png' class="close" @click="handleClick">
    </div>
    <transition
                name="dropdown-animate"
                enter-active-class = "animated slideInLeft"
                leave-active-class = "animated slideOutLeft">
        <el-menu
        default-active="2"
        v-show="show"
        router>
            <el-menu-item index="2" route="/" @click="handleClick">
                <span slot="title">主页</span>
            </el-menu-item>
            <el-menu-item index="3" route="/file" @click="handleClick">
                <span slot="title">文件</span>
            </el-menu-item>
            <el-menu-item index="4" route="/showAllTeams" @click="handleClick">
                <span slot="title">队伍</span>
            </el-menu-item>
            <el-menu-item index="5" route="/battle" @click="handleClick">
                <span slot="title">对战</span>
            </el-menu-item>
            <el-submenu index="6">
                <template slot="title"><span>个人中心</span></template>
                <el-menu-item-group>
                    <el-menu-item index="6-1" route="/teamprofile" @click="handleClick">
                    <span slot="title">我的队伍</span>
                </el-menu-item>
                    <el-menu-item index="6-2" route="/teampulse" @click="handleClick"> 
                        <span slot="title">比分变化</span>
                    </el-menu-item>
                    <el-menu-item index="6-3" v-if="hasLogin" @click="logout(); handleClick();">
                        <span slot="title">退出登录</span>
                    </el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-menu-item index="7" route="/login" v-if="!hasLogin" @click="handleClick"> 登陆/注册 </el-menu-item>
            <el-menu-item index="8" v-else class="usrname" >{{username}}</el-menu-item>
        </el-menu>
    </transition>
</div>
</template>

<script>
    import authSrv from '@/api/auth.js'
    export default{
        name: 'NavBar',
        data(){
            var _map = {
                    "/":'2',
                    "/file": '3',
                    "/ShowAllTeams": '4',
                    "/battle": '5',
                    "/login": '6'
                }
            return{
                activeIndex: _map[this.$router.history.current.path],
                router:Boolean(1),
                profile: avatar,
                show: false,                
            }
        },
        computed: {
            hasLogin(){
                return Boolean(this.$store.state.userid!=null)
            },
            username(){
                return this.$store.state.username
            },
                        
        },
        created () {
            this.hasLogin = Boolean(localStorage.getItem('teamstyle_id'))
        },
        methods: {
            logout () {
                console.log('trigger logout')
                this.hasLogin = false
                authSrv.logout(this)
                this.$router.push('/')
            },
            handleJump(command){
                if(command === "a"){
                    this.$router.push('/PwdChange')
                    console.log(this.$router.history.current)
                } else if(command === "b"){
                    this.$router.push('/MyTeam')
                } else if(command === "c"){
                    this.logout();
                    this.$router.push('/')
                }
            },
            handleClick(){
                this.show=!this.show
            }
        }
    }
</script>

<style lang="scss" scoped>
@import "/static/css/animate.css";
div {
    background-color: transparent;
}
#log,#profile{
    border:none;
    position: absolute;
    right: 0;
    height: 100%;
    line-height: 60px;
    &:visited{
        color:#909399;
    }
}

#menu {
    border: none;
    li:first-child {
        background-color: transparent;
        border: none;
    }
    li {
        font-family: '5efe7697695c42a99b24705c46f7ca0c';
        font-size: 1rem;
        border-bottom-width: 4px;
        border-color: #383838;
        img {
            width: 40px;
            height: 40px;
        }
    }
    li:first-child {
        margin: 0;
    }
}

.PC{
    z-index: 1000;
    background-color: transparent;
}
.navbar {
    display: none;
}
a,a:active,a:link,a:hover,a:visited{
    text-decoration: none;
}  
span {
    margin-left:10px;
    color: black;
    font-weight: 1rem;
}
@media screen and (max-width:720px) {
    .el-menu {
        position: fixed;
        top: 40px;
        height: 100vh;
        width: 200px!important;
        z-index: 2000;
        background-color: #f0f0f0;
        border: none;
        border-right: solid 1px #fefefe;
    }
    .navbar {
        display: block;
        width: 100%;
        position: fixed;
        top: 0;
        z-index: 2010;
        background-color: rgba(250, 250, 250, 0.9);
    }
    .el-menu-item-group{
        background-color: #f4f4f4;
        width: 200px;
    }
    .usrname {
        text-align: center;
    }
    img {
        position: fied;
        top:0;
        z-index: 1990;
        height: 30px;
        width: 30px;
        display: block;
        margin: 5px 5px;
    }
}
</style>
<style lang="scss">
div.el-submenu__title {
    border-bottom: none!important;
}
</style>