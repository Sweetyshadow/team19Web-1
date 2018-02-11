from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.db import models
from .models import TeamInfo, StudentInfo, RuleFile
from django.views.decorators.csrf import csrf_exempt

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
        the_name = request.POST['name']
        the_pwd = request.POST['pwd']
        the_email = request.POST['email']
        for s in students:
            if s.student_nickname == the_name:
                success = False
                message += "the name exist!"
                break
        if success == True:
            new_student = StudentInfo.objects.create(
                student_nickname = the_name,
                password = the_pwd,
                thu_email = the_email
            )
            new_student.save()
            message += "success!"
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
        the_name = request.POST['name']
        the_pwd = request.POST['pwd']
        for s in students:
            if the_name == s.student_nickname:
                one = s
                flag = True
                break
        if flag == True:
            if one.password == the_pwd:
                success = True
            else:
                message += "wrong password!"
        else:
            message += "the user doesn't exist!"    
        if success == True:
            return JsonResponse({'success':success,'id':str(one.id),'message':message})            
        else:
            return JsonResponse({'success':success,'post':str(request.POST),'message':message})
    elif request.method == 'GET':      
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})



def TeamAdd(request):
    if request.method == 'POST':
        if request.POST['invitecode']:#创建队伍
            teams = TeamInfo.objects.all()
            success = True
            message = ""
            the_name = request.POST['teamname']
            for t in teams:
                if t.team_name == the_name:
                    success = False
                    message += "team name exist!"
                    break
            if success == True:
                the_leader = request.POST['userid']
                invite_code = request.POST['invitecode']
                new_team = TeamInfo.objects.create(
                    team_name = the_name,
                    leader = the_leader,
                    invite_code = invite_code
                    )
                new_team.save()
        return JsonResponse({'success':success,'message':message,'team':the_name})
    elif request.method == 'GET':
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})

def TeamJoin(request):
    if request.method == 'POST':
        invitecode = request.POST['invitecode']
        the_team = TeamInfo.objects.get(invite_code = invitecode)
        success = False
        message = ""
        if the_team:
            success = True
            return HttpResponse(render(request,locals()))
    elif request.method == 'GET':
        return JsonResponse({'success':str(request.body),'POST':str(request.POST),'GET':str(request.GET)})





