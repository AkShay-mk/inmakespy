
from django.urls import path
from .import views

urlpatterns = [
    
    path('listview/',views.tasklistview.as_view(),name="listview"),
    path('taskdetail/<int:pk>/',views.taskdetail.as_view(),name="taskdetail")
]
