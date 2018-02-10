from django.urls import path
from . import views


app_name = 'backend'
urlpatterns = [
    path('teams/', views.TeamProcess),
    path('team_id=<int:pk>/', views.GroupDetail.as_view(), name='GroupDetail'),
    path('user_id=<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    path('RuleFile_id=<int:pk>', views.RuleFileView.as_view(), name='RuleFile'),
    path('students/',views.StudentProcess),
]
