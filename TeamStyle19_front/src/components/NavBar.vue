<template>
<div>
    <el-menu :default-active="activeIndex" mode="horizontal" router class="PC" id="menu" @click="indexupdate(activeIndex)">
        <!--el-menu-item index="1" route="/"> index </el-menu-item!-->
        <el-menu-item index="1"><a href="https://eesast.com"><img src="/static/img/EESAST.PNG"/></a></el-menu-item>
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
            <!--el-dropdown @command="handleJump" trigger="click"> 
                
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="a">修改密码</el-dropdown-item>
                    <el-dropdown-item command="b">我的队伍</el-dropdown-item>
                    <el-dropdown-item command="c">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown-->
        </el-menu-item>
        <el-menu-item index="8" v-else id="log" route="/login"> 登录|注册 </el-menu-item>
    </el-menu>
    <!--el-menu router class="mobile" mode="horizontal">
        <el-menu-item  id="mobile-menu">
            <img src ='/static/img/menu.png' class="close" @click="handleClick">
            <transition
                name="dropdown-animate"
                enter-active-class = "animated slideInDown"
                leave-active-class = "animated slideOutUp">
                <ul v-show="show" class="menu-dropdown">
                    <li @click="handleClick"><router-link to="/"> index </router-link></li!>
                    <li @click="handleClick"><router-link to="/"> home </router-link></li>
                    <li @click="handleClick"><router-link to="/file"> 文件 </router-link></li>
                    <li @click="handleClick"><router-link to="/ShowAllTeams"> 队伍 </router-link></li>
                    <li @click="handleClick"><router-link to="/battle"> 对战 </router-link></li>
                    <li @click="handleClick"> <img src='/static/img/close.png'></li>
                </ul>
            </transition>
        </el-menu-item>
        <el-menu-item v-if="hasLogin" id="profile">
            <el-dropdown @command="handleJump" class="user-dropdown" trigger="click"> 
                <span> {{username}} </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="a">修改密码</el-dropdown-item>
                    <el-dropdown-item command="b">我的队伍</el-dropdown-item>
                    <el-dropdown-item command="c">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
            <router-link to="/"><span @click = "logout"> 退出 </span></router-link>
        </el-menu-item>  
        <el-menu-item v-else index="5" id="log" route="/login"> 登录|注册 </el-menu-item>  
    </el-menu-->
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
            <el-menu-item index="7" route="\login" v-if="!hasLogin" @click="handleClick"> 登陆/注册 </el-menu-item>
            <el-menu-item index="8" v-else class="usrname" >{{username}}</el-menu-item>
        </el-menu>
    </transition>
</div>
</template>

<script>
    import authSrv from '@/api/auth.js'
    import avatar from '../../static/img/AC.png'
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
    #log {
        line-height: 40px;
    }
    #profile, .user-dropdown {
        position: absolute;
        right: 0;
        height: 100%;
        span {
        display:block;
        margin: auto;
        line-height: 40px;
    }
    }
    .el-dropdown{
        position: absolute;
        top: 0;
    }
    #mobile-menu {
        height: 10%;
        border: none;
        .close{
            position: absolute;
            left: 0;
        }
    }
    .mobile {
        li:nth-last-child(1) {
            padding-right: 5px;
        }
    }
    .menu-dropdown {
        height: 100vh;
        width: 100vw;
        padding: 0;
        color: white;
        background-color: hsla(0,0,0,0.85);
        z-index: 2000;
        position: absolute;
        top: 0;
        left:0;
        list-style-type: none;
        li:first-child {
            margin: 20% 0 0 0;
        }
        li:nth-last-child(1),li:nth-last-child(2) {
            border: none;
        }
        li:nth-last-child(1){
            padding: 10% 0 0 0;
        }
        li{
            padding: 0;
            height: 100px;
            line-height: 100px;
            text-align: center;
            border-bottom: {
                color: white;
                width: 1px !important;
                style: solid;
            }
            img {
                margin: 0 auto;
            }
        }
    }
}
</style>
<style lang="scss">
div.el-submenu__title {
    border-bottom: none!important;
}
li.el-menu-item.is-active {
        width: 200px;
    }
</style>