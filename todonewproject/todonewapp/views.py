from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
class tasklistview(ListView):
    model=Task
    template_name='add.html'
    context_object_name='task1'
    success_url=reverse_lazy('taskdetail')
    
class taskdetail(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task2'
    