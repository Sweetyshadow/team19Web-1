# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class TeamInfo(models.Model):
    team_name = models.CharField(max_length=30, default = 'null',null=True)
    leader = models.CharField(max_length=50, default = 'null',null=True)
    member1 = models.CharField(max_length=50, default = 'null',null=True)
    member2 = models.CharField(max_length=50, default = 'null',null=True)
    member3 = models.CharField(max_length=50, default = 'null',null=True)
    member_num = models.IntegerField(default = 1)
    invite_code = models.CharField(max_length=20, null=True)
    codes = models.TextField(null=True)
    history = models.TextField(null=True)
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.team_name


class StudentInfo(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.CASCADE, default = 'null',null=True)
    is_leader = models.BooleanField(default=False)
    student_id = models.CharField(max_length=20, null=True)
    student_nickname = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=30, default='000', null=True)
    thu_email = models.CharField(max_length=20, null=True)
    profile_photo = models.ImageField(null=True)

    def __str__(self):
        return self.student_nickname


class RuleFile(models.Model):
    title = models.CharField('标题', max_length=20)
    desc = models.CharField('描述', max_length=50)
    pub_date = models.DateField('date published')
    address = models.FileField(null=True)

    def __str__(self):
        return self.title