from django.urls import url
from . import views


app_name = 'backend'
urlpatterns = [
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
]
