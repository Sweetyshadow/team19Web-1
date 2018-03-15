# -*- coding: utf-8 -*-
from django.db import models
import hashlib
import json
# Create your models here.

HISTORY_LENGTH = 20#

class TeamInfo(models.Model):
    team_name = models.CharField(max_length=30, null=True)
    leader = models.CharField(max_length=50, null=True)
    member1 = models.CharField(max_length=50, null=True)
    member2 = models.CharField(max_length=50, null=True)
    member3 = models.CharField(max_length=50, null=True)
    member_num = models.IntegerField(default = 1)
    invite_code = models.CharField(max_length=20, null=True)
    battle_code = models.FileField(null = True)
    codes = models.TextField(null=True)
    history = models.CharField(max_length = 8000, default = '[]')
    score = models.CharField(max_length = 300, default = '[]')

    def __str__(self):
        return self.team_name

    def get_score(self):
        return json.loads(self.score)

    def add_score(self,x):
        a = json.loads(self.score)
        a.append(x)
        self.score = json.dumps(a)

    def get_history(self):
        return json.loads(self.history)

    def add_history(self,x):
        a = json.loads(self.history)
        a.append(x)
        if len(a) > HISTORY_LENGTH:
            del a[0]
        else:
            pass
        self.history = json.dumps(a)
        self.save()



class StudentInfo(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.CASCADE, null=True)
    is_leader = models.BooleanField(default=False)
    is_active = models.BooleanField(default = False)
    student_id = models.CharField(max_length=20, null=True)
    student_nickname = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=100, default='000', null=True)
    salt = models.CharField(max_length = 8, null = True)
    thu_email = models.CharField(max_length=50, null=True)
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