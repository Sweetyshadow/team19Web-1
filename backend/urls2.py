from django.conf.urls import url
from . import views


app_name = 'backend'
urlpatterns = [
<<<<<<< HEAD
    url('teams/add/', views.TeamAdd),
    url('teams/join/',views.TeamJoin),
    url('teams/exit/',views.TeamExit),
    url('teams/oneteam/',views.MyTeam),
    url('teams/allteam/',views.AllTeam),
    url('teams/score/',views.GetScore),
    url('teams/battle/',views.Battle),
    url('teams/inquire/<int:id1>+<int:id2>/',views.Inquire),
    url('team_id=<int:pk>/', views.GroupDetail.as_view(), name='GroupDetail'),
    url('user_id=<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    url('RuleFile_id=<int:pk>', views.RuleFileView.as_view(), name='RuleFile'),
    url('students/reg/',views.StudentReg),
    url('students/login/',views.StudentLogin),
    url('students/leader/',views.StudentLeader),
    url('students/modify/',views.ModifyPwd),
    url('students/headpic/',views.GetHeadpic),
    url('students/activate/',views.StudentActivate),
    url('students/find_password/',views.find_password),
    url('upload/file/',views.UploadFile),
    url('download/code/',views.GetCode),
    url('download/allfiles/',views.GetIndex),
    url('download/file/<str:filename>',views.GetFile)
=======
    path('teams/add/', views.TeamAdd),
    path('teams/join/',views.TeamJoin),
    path('teams/exit/',views.TeamExit),
    path('teams/oneteam/',views.MyTeam),
    path('teams/allteam/',views.AllTeam),
    path('teams/score/',views.GetScore),
    path('teams/history/',views.GetHistory),
    path('teams/battle/',views.Battle),
    path('teams/inquire/<int:id1>+<int:id2>/',views.Inquire),
    path('team_id=<int:pk>/', views.GroupDetail.as_view(), name='GroupDetail'),
    path('user_id=<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    path('RuleFile_id=<int:pk>', views.RuleFileView.as_view(), name='RuleFile'),
    path('students/reg/',views.StudentReg),
    path('students/login/',views.StudentLogin),
    path('students/leader/',views.StudentLeader),
    path('students/modify/',views.ModifyPwd),
    path('students/headpic/',views.GetHeadpic),
    path('students/activate/',views.StudentActivate),
    path('students/find_password/',views.find_password),
    path('upload/file/',views.UploadFile),
    path('download/code/',views.GetCode),
    path('download/allfiles/',views.GetIndex),
    path('download/file/<str:filename>',views.GetFile)
>>>>>>> def0e6d2d9727c980eae7b9ff0e27379839ee200
]
