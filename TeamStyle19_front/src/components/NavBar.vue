<template>
<div>
    <el-menu :default-active="activeIndex" mode="horizontal" router class="PC" id="menu">
        <!--el-menu-item index="1" route="/"> index </el-menu-item!-->
        <el-menu-item index="2" route="/"> fakehome </el-menu-item>
        <el-menu-item index="3" route="/file"> 文件 </el-menu-item>
        <el-menu-item index="4" route="/ShowAllTeams"> 队伍 </el-menu-item>
        <el-menu-item index="5" route="/battle"> 对战 </el-menu-item>
        <el-menu-item v-if="hasLogin" id="profile">
            <el-dropdown @command="handleJump" trigger="click"> 
                <span> {{username}} </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="a">修改密码</el-dropdown-item>
                    <el-dropdown-item command="b">我的队伍</el-dropdown-item>
                    <el-dropdown-item command="c">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </el-menu-item>
        <el-menu-item v-else index="6" id="log" route="/login"> 登录|注册 </el-menu-item>
    </el-menu>
    <el-menu router class="mobile" mode="horizontal">
        <el-menu-item  id="mobile-menu">
            <img src ='/static/img/menu.png' class="close" @click="handleClick">
            <transition
                name="dropdown-animate"
                enter-active-class = "animated slideInDown"
                leave-active-class = "animated slideOutUp">
                <ul v-show="show" class="menu-dropdown">
                    <!--li @click="handleClick"><router-link to="/"> index </router-link></li!-->
                    <li @click="handleClick"><router-link to="/"> fakehome </router-link></li>
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
            <!--router-link to="/"><span @click = "logout"> 退出 </span></router-link-->
        </el-menu-item>  
        <el-menu-item v-else index="5" id="log" route="/login"> 登录|注册 </el-menu-item>  
    </el-menu>
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
img {
    height: 60px;
    width: 60px;
    overflow: hidden;
}
#menu {
    li {
        //border: none;
        font-family: '5efe7697695c42a99b24705c46f7ca0c';
    }
}
a,a:active,a:link,a:hover,a:visited{
    text-decoration: none;
}  
span {
    margin-left:10px;
    color: black;
}
@media screen and (max-width:720px) {
    .el-menu {
        height: 40px;
    }
    
    img {
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
        margin: auto 10px;
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
