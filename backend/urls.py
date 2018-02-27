from django.urls import path
from . import views


app_name = 'backend'
urlpatterns = [
    path('teams/add/', views.TeamAdd),
    path('teams/join/',views.TeamJoin),
    path('teams/exit/',views.TeamExit),
    path('teams/oneteam/',views.MyTeam),
    path('teams/allteam/',views.AllTeam),
    path('team_id=<int:pk>/', views.GroupDetail.as_view(), name='GroupDetail'),
    path('user_id=<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    path('RuleFile_id=<int:pk>', views.RuleFileView.as_view(), name='RuleFile'),
    path('students/reg/',views.StudentReg),
    path('students/login/',views.StudentLogin),
    path('students/leader/',views.StudentLeader),
    path('students/modify/',views.ModifyPwd),
    path('students/headpic/',views.GetHeadpic),
    path('upload/file/',views.UploadFile),
    path('download/code/',views.GetCode),
    path('download/allfiles/',views.GetIndex),
    path('download/file/<str:filename>',views.GetFile)
]
