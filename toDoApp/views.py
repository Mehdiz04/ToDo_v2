from typing import Any, Dict
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import  HttpResponseRedirect
from .models import Task

# Create your views here.
class Login(LoginView):
    template_name = 'toDoApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request , 'Your account has been created!')
            form.save()
            return redirect('login')

    context = {'form':UserCreationForm()}
    return render(request , 'toDoApp/register.html' , context)


class Main(LoginRequiredMixin , ListView):
    model = Task
    template_name = 'toDoApp/main.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(author=self.request.user)
        return context



class AddTask(LoginRequiredMixin , CreateView):
    template_name = 'toDoApp/add_task.html'
    model = Task
    fields = ['title' , 'description']
    success_url = reverse_lazy('main')

    def form_valid(self , form):
        task = form.save(commit=False)
        task.author = self.request.user
        task.save()
        return HttpResponseRedirect(reverse_lazy('main'))
    

class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'toDoApp/update_task.html'
    model = Task
    fields = ['title' , 'description', 'completed']
    success_url = reverse_lazy('main')

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


def deleteTask(request , pk):
    task = Task.objects.get(id=pk)
    if request.user != task.author:
        messages.warning(request, 'invalid request!!')
        return redirect('main')
    else:
        task.delete()
        return redirect('main')


class DetailTask(LoginRequiredMixin , DetailView):
    model = Task
    template_name = 'toDoApp/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
