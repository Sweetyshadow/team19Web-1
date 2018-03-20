from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.urls import reverse
from django.views import generic
from django.db import models,connection
from django.conf import settings
from django.core.mail import send_mail, mail_admins, BadHeaderError
from .models import TeamInfo, StudentInfo, RuleFile, DockerServer
from .forms import StudentRegForm, StudentLoginForm, PasswordModifyForm, TeamAddForm, EmailValidation
from django.views.decorators.csrf import csrf_exempt

from base64 import b64encode
import re
import hashlib
import os
import binascii
import requests
import json
import random
import time
import shutil

# Create your views here.


class StartView(generic.ListView):
    template_name = 'backend/groups.html'
    context_object_name = 'all_teams'

    def get_queryset(self):
        return TeamInfo.objects.all()


class GroupDetail(generic.DetailView):
    model = TeamInfo
    template_name = 'backend/GroupDetail.html'


class StudentDetail(generic.DetailView):
    model = StudentInfo
    template_name = 'backend/StudentDetail.html'


class RuleFileView(generic.DetailView):
    model = RuleFile
    template_name = 'backend/RuleFile.html'

@csrf_exempt
def StudentReg(request):
    if request.method == 'POST':
        students = StudentInfo.objects.all()
        success = True
        message = ""
        form = StudentRegForm(request.POST)
        if form.is_valid():
            the_name = form.cleaned_data['name']
            the_student_id = form.cleaned_data['studentID']
            the_pwd = form.cleaned_data['pwd']
            the_email = form.cleaned_data['email']
            if StudentInfo.objects.filter(student_nickname=the_name).exists():
                success = False
                message += "用户名已存在！"
            elif StudentInfo.objects.filter(student_id=the_student_id).exists():
                success = False
                message += "学号已存在！"
            elif StudentInfo.objects.filter(thu_email=the_email).exists():
                success = False
                message += "电子邮箱已存在！"
            else:
                success = True
            if success is True:
                the_salt = binascii.hexlify(os.urandom(4)).decode()
                new_student = StudentInfo.objects.create(
                    student_nickname = the_name,
                    student_id = the_student_id,
                    salt = the_salt,
                    password = hashvalue(the_pwd,the_salt),
                    thu_email = the_email
                )
                result = active_email(the_name,the_email)
                new_student.save()              
                message += "success!"
                return JsonResponse({'success':success,'message':message,'email':result})
        else :
            success = False
            message = form.errors
        return JsonResponse({'success':success,'message':message})

    elif request.method == 'GET':      
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})

@csrf_exempt
def StudentLogin(request):
    if request.method == 'POST':
        students = StudentInfo.objects.all()
        success = False
        flag = False
        message = ""
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            the_name = form.cleaned_data['name']
            try:
                the_student = StudentInfo.objects.get(student_nickname = the_name)
                the_pwd = hashvalue(form.cleaned_data['pwd'],the_student.salt)
                if the_student.password == the_pwd :
                    if the_student.is_active == True:
                        success = True
                    else :message += "你还不是正式用户！"
                else :
                    message += "用户名或密码错误！"
            except:
                message += "用户名或密码错误!"

            if success == True:
                return JsonResponse({'success':success,'id':str(the_student.id),'message':message})            
            else:
                return JsonResponse({'success':success,'post':str(request.POST),'message':message})
        else:
            return JsonResponse({'success':False,'message':form.errors})
    elif request.method == 'GET':      
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})


def StudentActivate(request):
    userid = request.GET.get('userid','')
    userkey = request.GET.get('userkey','')
    try:
        the_student = StudentInfo.objects.get(id = userid)
    except :
        return HttpResponse("激活失败1!请联系管理员")
    if the_student.is_active == True:
        pass
        return HttpResponseRedirect("/")
    elif userkey == hashvalue(the_student.student_nickname,'team19'):
        the_student.is_active = True
        the_student.save()
        return HttpResponseRedirect("/")



@csrf_exempt
def StudentLeader(request):
    success = False
    message = ""
    if request.method == 'POST':
        the_id = request.POST['userid']
        the_student = StudentInfo.objects.get(id = the_id)
        isleader = the_student.is_leader
        the_name = the_student.student_nickname
        success = True
        return JsonResponse({'success':success,'message':message,'name':the_name,'isleader':isleader})
    else :
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})

@csrf_exempt
def ModifyPwd(request):
    success = False
    if request.method == 'POST':
        form = PasswordModifyForm(request.POST)
        if form.is_valid():
            the_id = form.cleaned_data['id']
            the_student = StudentInfo.objects.get(id = the_id)
            if the_student:
                old_pwd = hashvalue(form.cleaned_data['oldpwd'],the_student.salt)
                #hashlib.sha224((form.cleaned_data['oldpwd'] + the_student.salt).encode('utf-8')).hexdigest()
                if the_student.password == old_pwd:
                    new_pwd = form.cleaned_data['newpwd']
                    the_student.password = hashlib.sha224((new_pwd + the_student.salt).encode('utf-8')).hexdigest()
                    the_student.save()
                    success = True
                    return JsonResponse({'userid':the_id,'password':the_student.password})
                else :
                    message = "原密码错误！"
                    return JsonResponse({'success':success,'message':message})
            else :
                message = "该用户不存在！"
                return JsonResponse({'success':success,'message':message})
        else:
            return JsonResponse({'success':success,'message':form.errors})
    else :
        return JsonResponse({'response':str(request.body)})


@csrf_exempt
def TeamAdd(request):
    if request.method == 'POST':
        form = TeamAddForm(request.POST)
        if form.is_valid():#创建队伍
            teams = TeamInfo.objects.all()
            success = True
            message = ""
            response = {}
            the_leader = form.cleaned_data['userid']
            invite_code = form.cleaned_data['invitecode']
            the_name = form.cleaned_data['teamname']
            the_student = StudentInfo.objects.get(id = the_leader)
            for t in teams:
                if t.team_name == the_name:
                    success = False
                    message += "队伍名称重复！"
                    return JsonResponse({'success':success,'message':message})
                if t.invite_code == invite_code:
                    success = False
                    message += "邀请码重复！"
                    return JsonResponse({'success':success,'message':message})
            if the_student.team_name :
                success = False
                message += "你已经加入了一支队伍！"
            if success == True:
               new_team = TeamInfo.objects.create(
                    team_name = the_name,
                    leader = the_student.student_nickname,
                    invite_code = invite_code
                    )
               new_team.member_num = 1
               new_team.save()
               the_student.team_name = new_team
               the_student.is_leader = True
               the_student.save()
               response['success'] = success
               response['teamname'] = the_name
               response['teamid'] = new_team.id
               response['leader'] = the_student.student_nickname
               response['scale'] = new_team.member_num
               return JsonResponse(response)
        else :
            return JsonResponse({'success':False,'message':form.errors})
        return JsonResponse({'success':success,'message':message,'team':the_name})
    elif request.method == 'GET':
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})

@csrf_exempt
def TeamJoin(request):
    if request.method == 'POST':
        invite_code = request.POST['invitecode']
        success = False
        message = ""
        response = {}
        the_id = request.POST['userid']
        the_student = StudentInfo.objects.get(id = the_id)
        if the_student.team_name :
            message += "您已经加入了一支队伍！"
            return JsonResponse({'success':success,'message':message,'name':the_student.student_nickname,'team':the_student.team_name.team_name})
        else :
            the_team = TeamInfo.objects.get(id = request.POST['teamid'])
            if the_team.invite_code != invite_code:
                message = "邀请码不存在！"
                return JsonResponse({'success':success,'message':message})
            the_scale = the_team.member_num
            if the_scale < 4:
                success = True
                the_student.team_name = the_team
                the_student.save()
                if the_scale == 1:
                    the_team.member1 = the_student.student_nickname
                    the_team.member_num += 1
                    the_team.save()
                elif the_scale == 2:
                    the_team.member2 = the_student.student_nickname
                    the_team.member_num += 1
                    the_team.save()
                else :
                    the_team.member3 = the_student.student_nickname
                    the_team.member_num += 1
                    the_team.save()
                #return JsonResponse(response)
                response['teamname'] = the_team.team_name
                response['teamid'] = the_team.id
                response['leader'] = the_team.leader 
                response['scale'] = the_team.member_num
                response['member1'] = the_team.member1
                response['member2'] = the_team.member2
                response['member3'] = the_team.member3                
                response['success'] = success
                return JsonResponse(response)
            else:
                message += "队伍已满！"
                member_num = 4
                return JsonResponse({'success':success,'message':message})
        #except:
        #    message += "the team doesn't exist!"
        #    return JsonResponse({'success':success,'message':message})
    elif request.method == 'GET':
        return HttpResponse(locals())
        #return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})

@csrf_exempt
def TeamExit(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        the_student = StudentInfo.objects.get(student_nickname = request.POST['name'])
        the_team = TeamInfo.objects.get(team_name = the_student.team_name.team_name)
        the_name = the_student.student_nickname
        if the_team.member1 == the_name:
            if the_team.member2 :
                the_team.member1 = the_team.member2
                if the_team.member3:
                    the_team.member2 = the_team.member3
                else:
                    del the_team.member2
                    cursor.execute("update backend_teaminfo set member2 = null where id = " + str(the_team.id))
            else :
                del the_team.member1
                cursor.execute("update backend_teaminfo set member1 = null where id = " + str(the_team.id))

        elif the_team.member2 == the_name:
            if the_team.member3:
                the_team.member2 = the_team.member3
            else :
                del the_team.member2
                cursor.execute("update backend_teaminfo set member2 = null where id = " + str(the_team.id))

        elif the_team.member3 == the_name:
            del the_team.member3
            cursor.execute("update backend_teaminfo set member3 = null where id = " + str(the_team.id))
        else:
            message = "此人并不在您的队伍里！"
            success = False
            return JsonResponse({'success':success,'message':message})
        the_team.member_num -= 1
        the_team.save()
        cursor.execute("update backend_studentinfo set team_name_id = null where id = " + str(the_student.id))
        cursor.close()
        response = {}
        response['teamname'] = the_team.team_name
        response['teamid'] = the_team.id
        response['leader'] = the_team.leader 
        response['scale'] = the_team.member_num
        response['member1'] = the_team.member1
        response['member2'] = the_team.member2
        response['member3'] = the_team.member3        
        return JsonResponse(response)
    else :
        return JsonResponse({'response':str(request.body)})

@csrf_exempt
def MyTeam(request):
    success = False
    message = ""
    if request.method == 'POST':
        the_id = request.POST['userid']
        the_student = StudentInfo.objects.get(id = the_id)
        if the_student.team_name :
            the_team = TeamInfo.objects.get(team_name = the_student.team_name)
            success = True
            response = {}
            response['success'] = success
            response['teamid'] = the_team.id
            response['teamname'] = the_team.team_name
            response['scale'] = the_team.member_num
            response['leader'] = the_team.leader
            response['member1'] = the_team.member1
            response['member2'] = the_team.member2
            response['member3'] = the_team.member3
            if the_student.is_leader:
                response['invitecode'] = the_team.invite_code
            return JsonResponse(response)
        else :
            message += "你还没有加入一支队伍！"
            return JsonResponse({'success':success,'message':message})            
    elif request.method == 'GET':
        return HttpResponse(locals())

@csrf_exempt
def AllTeam(request):
    if request.method == 'POST':
        return HttpResponse(locals())
    elif request.method == 'GET':
        response = []
        teams = TeamInfo.objects.all()
        for team in teams:
            if team.battle_code:
                hasAI = True
            else:
                hasAI = False
            response.append({
                'teamid':team.id,
                'teamname':team.team_name,
                'scale':team.member_num,
                'leader':team.leader,
                'hasAI':hasAI,
                'member1':team.member1,
                'member2':team.member2,
                'member3':team.member3
                })
        return JsonResponse(response, safe = False)

'''@csrf_exempt
def UploadHeadpic(request):
    if request.method == 'POST':
        myfile = request.FILES.get("myfile",None)
'''
@csrf_exempt
def UploadFile(request):
    if request.method == 'POST':
        myfile = request.FILES['file']
        if not myfile:
            return JsonResponse({'success':False,'message':'no file found!'})
        else :
            the_id = request.POST['userid']
            the_student  = StudentInfo.objects.get(id = the_id)                       
            if request.POST['headpic'] == 'true':                
                if the_student:
                    '''cursor = connection.cursor()
                    cursor.execute("update backend_studentinfo set profile_photo = \'" + url + "\' where id = " + the_id)
                    cursor.close()'''
                    index = os.listdir('/home/ubuntu/team19/user')
                    if the_student.student_nickname in index:
                        pass
                    else :
                        os.system('mkdir /home/ubuntu/team19/user/' + the_student.student_nickname)
                    url = '/home/ubuntu/team19/user/' + the_student.student_nickname + '/' + str(myfile.name)
                    destination = open(url,'wb+')
                    for chunk in myfile.chunks():
                        destination.write(chunk)
                    destination.close()
                    the_student.profile_photo = url
                    the_student.save()
                    return JsonResponse({'success':'头像上传成功！'})
                else :
                    return JsonResponse({'success':False,'message':"该用户不存在！"})  
            else:
                if the_student:
                    if the_student.team_name:
                        index = os.listdir('/home/ubuntu/team19/team')
                        if the_student.team_name.team_name in index:
                            pass
                        else :
                            os.system('mkdir /home/ubuntu/team19/team/' + the_student.team_name.team_name)
                        url = '/home/ubuntu/team19/team/' + the_student.team_name.team_name + '/' + str(myfile.name)
                        if myfile.name[-4:] != '.cpp':
                            return JsonResponse({'success':False,'message':'代码格式错误！'})
                        with open(url,'wb') as destination:
                            for chunk in myfile.chunks():
                                destination.write(chunk)
                        url2 = '/home/ubuntu/team19/game/teamstyle19new/player_file_linux_for_player/%s.cpp'%the_student.team_name.team_name
                        shutil.copyfile(url, url2)
                        #destination = open(url2,'wb+')
                        #for chunk in myfile.chunks():
                        #    destination.write(chunk)
                        the_team = TeamInfo.objects.get(team_name = the_student.team_name)
                        the_team.battle_code = url
                        the_team.save()
                        the_student.save()
                        ai = True
                        if ai :
                            code = the_team.battle_code.name.split('/')
                            name = code[-2] + '/' + code[-1]
                            r = requests.post('http://123.207.140.186:8888/compile/',data = {'name':name})
                            #old_path = os.getcwd()#
                            #os.chdir('/home/ubuntu/team19/game/teamstyle19new/player_file_linux_for_server')
                            #execute = '/home/ubuntu/team19/team/' + the_team.team_name + '/' + the_team.team_name + '.exe'
                            #os.system('g++ main.cpp player.cpp api_player.cpp communication.cpp -pthread -std=c++11 -o ' + execute)
                            #os.chdir(old_p)
                            try:
                                response = json.loads(r.text)
                            except:
                                return JsonResponse({'success':False,'message':r.text})
                            if response['success']:
                                return JsonResponse({'success':True})
                            else:
                                return JsonResponse({'success':False,'message':response['message']})
                        return JsonResponse({'success':r.text})
                    else:
                        return JsonResponse({'success':False,'message':"该用户还没有加入一支队伍！"})
                else:
                    return JsonResponse({'success':False,'message':"该用户不存在！"})


            return JsonResponse({'success':True,'message':'Upload!','post':str(request.POST)})
    elif request.method == 'GET':
        s = StudentInfo.objects.get(id = 10)
        image = s.profile_photo
        end = re.findall(r'\.(\w+)',str(image.name))
        return HttpResponse(image,content_type = "image/" + end[0])

@csrf_exempt
def GetHeadpic(request):
    if request.method == 'POST':
        the_id = request.POST['userid']
        image = StudentInfo.objects.get(id = the_id).profile_photo
        f = open(image.name,'rb').read()
        response = b64encode(f) 
        return HttpResponse(response)
        #return JsonResponse({'url':image.name})
    elif request.method == 'GET':
        return HttpResponse('STUPID MAN!!!!')
        #vd

@csrf_exempt
def GetCode(request):#用于代码下载
    if request.method == 'POST':
        the_id = request.POST['userid']
        the_student = StudentInfo.objects.get(id = the_id)
        if the_student.team_name:
            the_team = the_student.team_name
            if the_team.battle_code:
                file_name = the_team.battle_code.name
            else:
                return JsonResponse({'success':False,'message':'您的队伍还没有上传代码！'})
        else :
            return JsonResponse({'success':False,'message':'您还没有加入一支队伍！'})       
        response = FileResponse(open(file_name))
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename=' + file_name
        return response
    else:
        response = FileResponse(open('/home/ubuntu/team19/user/std.pdf'))
        response['Content-Type'] = 'application/octet-stream'
        s = 'std.pdf'
        response['Content-Disposition'] = 'attachment;filename = ' + s
        return response

@csrf_exempt
def GetScore(request):
    if request.method == 'GET':
        return JsonResponse({'score':TeamInfo.objects.get(id = 1).score})
    else :
        the_student = StudentInfo.objects.get(id = request.POST['userid'])
        the_team = the_student.team_name
        return JsonResponse({'score':the_team.score})

@csrf_exempt
def GetFile(request,filename):
    if request.method == 'POST':
        the_file_name = request.POST['filename']
        file_path = os.path.join(settings.MEDIA_ROOT,the_file_name)
        response = FileResponse(open(file_path,'rb'))
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename = ' + the_file_name
        return response
    else :
        file_path = os.path.join(settings.MEDIA_ROOT,filename)
        response = FileResponse(open(file_path,'rb'))
        response['Content-Type']='application/octet-stream'  
        response['Content-Disposition']='attachment;filename = ' + filename
        return response

def GetIndex(request):
    if request.method == 'GET':
        index = os.listdir(settings.MEDIA_ROOT)
        return JsonResponse({'index':index})
    else :
        return JsonResponse({'message':'STUPID MAN!'})

@csrf_exempt
def Battle(request):
    if request.method == 'POST':
        #return HttpResponse(request.getHeader("Referer"))
        team1_id = request.POST['team1']
        team2_id = request.POST['team2']
        team1 = TeamInfo.objects.get(id = team1_id)
        team2 = TeamInfo.objects.get(id = team2_id)
        if team1.battle_time >= 30:
            return JsonResponse({'success':False,'message':'您的对战次数已达上限，不能再次主动发起对战！'})
        battle_data = {'team1':team1.team_name,'team2':team2.team_name,'id1':team1_id,'id2':team2_id}
        #d = requests.post('http://123.207.140.186:8888/enviroment/',data = {'team1':code_url1[-2],'team2':code_url2[-2]})
        #initial_time = time.time()
        #while time.time() - initial_time < 3:
        #    pass
        servers = DockerServer.objects.all()
        flag = False
        for server in servers:
            if server.is_busy == False:
                print(server.port)
                server.is_busy = True
                server.battle_id = team1_id + '+' +team2_id
                server.save()
                r = requests.post('http://123.207.140.186:%s/battle/'%server.port,data = battle_data)               
                flag = True
                break
            else:
                print(server.is_busy )
                pass
        if flag == False:
            return JsonResponse({'success':False,'message':'服务器正忙，请稍后再试！' + r.text})
        #r = requests.post('http://123.207.140.186:8888/battle/',data = battle_data)
        try:
            response = json.loads(r.text)
        except:
            return JsonResponse({'success':False,'message':r.text})
        if response['success']:
            return JsonResponse({'success':True,'battleid':team1_id + '+' +team2_id})
        else:
            return JsonResponse({'success':False,'message':response['message']})
    elif request.method == 'GET':
        r = requests.get('http://123.207.140.186:8888/battle/')
        team = TeamInfo.objects.get(id = 1)
        score1 = 90
        ti = time.time()
        team.add_score(["%s"%score1,"%s"%ti])
        return JsonResponse({'message':r.text})
#
@csrf_exempt
def Inquire(request,id1,id2):
    if request.method == 'POST':
        return JsonResponse({'success':False})
    elif request.method == 'GET':
        team1 = TeamInfo.objects.get(id = id1)
        team2 = TeamInfo.objects.get(id = id2)
        the_battle_id = '%s+%s'%(id1,id2)
        if DockerServer.objects.filter(battle_id = the_battle_id).exists():
            the_server = DockerServer.objects.get(battle_id = the_battle_id)            
            r = requests.get('http://123.207.140.186:%s/inquire/%s&*+%s&*+%s/'%(the_server.port,the_battle_id,team1.team_name,team2.team_name))
            #print('http://123.207.140.186:%s/inquire/%s&*+%s&*+%s/'%(the_server.port,the_battle_id,team1.team_name,team2.team_name) )
        else:
            return JsonResponse({'success':False,'message':'本场对战不存在！'})
        try:
            response = json.loads(r.text)
        except:
            return JsonResponse({'success':False,'message':r.text})
        if response['success']:
            the_server.is_busy = False
            the_server.battle_id = 'none'
            the_server.save()
            battle_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
            response['battle_time'] = battle_time
            score1 = team1.score
            score2 = team2.score
            E1 = 1/(1 + pow(10,(score2-score1)/400))
            E2 = 1/(1 + pow(10,(score1-score2)/400))
            if response['result']['winner'] == team1.team_name:
                score1 = score1 + 32 * (1 - E1)
                score2 = score2 + 32 * (0 - E2)
            else:
                score1 = score1 + 32 * (0 - E1)
                score1 = score2 + 32 * (1 - E2)
            team1.add_score(["%s"%score1,"%s"%str(response['battle_time'])])
            team2.add_score(["%s"%score1,"%s"%str(response['battle_time'])])
            team1.add_history(str(response['total_round']) + str(response['battle_time']) + 'w:%sl:%s'%(str(response['result']['winner']),str(response['result']['loser'])))
            team2.add_history(str(response['total_round']) + str(response['battle_time']) + 'w:%sl:%s'%(str(response['result']['winner']),str(response['result']['loser'])))
            team1.battle_time += 1
            team1.save()
            return JsonResponse(response)
        elif response['success'] == False:
            return JsonResponse({'success':False,'message':response['message']})
      


def hashvalue(value,salt):
    value = (value + salt).encode('utf-8')
    result = hashlib.sha224(value)
    result = result.hexdigest()
    return result

def active_email(username,email):
    try:
        receiver = email  # 设置邮件接收人
        key = hashvalue(username,'team19')
        path = os.path.join(settings.BASE_DIR,'backend/static/activemail.html')
        f = open(path,'rb')
        body = f.read()
        body = body.decode('utf-8')
        user = StudentInfo.objects.get(student_nickname = username)
        attach = "?userid=%s&&userkey=%s"%(user.id,key)
        body = body%(attach,attach)
        send_mail(
            subject = "AI挑战赛队式19账号激活", 
            message = "", 
            html_message = body,
            from_email = "team19_eesast@126.com", 
            fail_silently = False, 
            recipient_list = [receiver])
        return True
    except Exception as e:
        raise e


@csrf_exempt
def find_password(request):
    if request.method == 'POST':
        form = EmailValidation(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            if StudentInfo.objects.filter(thu_email=user_email).exists():
                the_student = StudentInfo.objects.get(thu_email=user_email)
                new_pwd = str(random.randint(10000000, 99999999))
                the_student.password = hashvalue(new_pwd, the_student.salt)
                the_student.save()
                password_email(the_student.student_nickname, user_email, new_pwd)
                return JsonResponse({'success':True,'name':the_student.student_nickname})
            else:
                return JsonResponse({'success': False, 'message': "invalid email!!!!!"})
        else:
            return JsonResponse({'success':False,'message':"invalid form!!!!!"})
    else:
        return HttpResponse("STUPID MAN!!!!")


def password_email(username, email, new_pwd):
    try:
        receiver = email  # 设置邮件接收人
        path = os.path.join(settings.BASE_DIR, 'backend/static/PasswordMessage.html')
        f = open(path, 'rb')
        body = f.read()
        body = body.decode('utf-8')
        attach1 = " %s " % username
        attach2 = new_pwd
        body = body % (attach1, attach2)
        send_mail(
            subject="AI挑战赛队式19账号密码找回",
            message="",
            html_message=body,
            from_email="team19_eesast@126.com",
            fail_silently=False,
            recipient_list=[receiver])
        return True
    except Exception as e:
        raise e
