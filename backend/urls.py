from django.urls import path
from . import views


app_name = 'backend'
urlpatterns = [
    path('teams/add/', views.TeamAdd),
    path('teams/join/',views.TeamJoin),
    path('teams/exit/',views.TeamExit),
    path('teams/oneteam/',views.MyTeam),
    path('teams/allteam/',views.AllTeam),
    path('teams/score/',views.GetScore),
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
]
