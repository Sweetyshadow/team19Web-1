from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.db import models
from .models import TeamInfo, StudentInfo, RuleFile

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

def StudentProcess(request):
    if request.method == 'POST':
        return JsonResponse({'body':request.body,'request':request})
    elif request.method == 'GET':
        students = StudentInfo.objects.all()
        return JsonResponse({'success':str(request.method),'message':str(request.GET)})

def TeamProcess(request):
    if request.method == 'POST':
        if request.body['invitecode']:
            teams = TeamInfo.objects.all()
            for 


'''        students = StudentInfo.objects.all()
        success = True
        message = ""
        the_name = request.body['name']
        the_pwd = request.body['pwd']
        the_email = request.body['email']
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
        return JsonResponse({'success':success,'message':message})'''