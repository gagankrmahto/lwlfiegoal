from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from lwlife.models import Task,Answer, Question
from .forms import AnswerForm

class CustomLoginView(LoginView):
    template_name = 'lwlife/login.html'
    fields  = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')



# Create your views here.
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_superuser:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(complete=False).count()
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    # field = ['title']
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    # field = ['title']
    fields = '__all__'
    succes_url = reverse_lazy('tasks')
    template = 'lwlife/task'
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')


class AnswerView(LoginRequiredMixin, ListView):
    template = 'lwlife/index.html'
    model = Answer
    context_object_name = 'answers'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_superuser:
            context['answers'] = context['answers'].filter(user=self.request.user)
        return context
class TodayView(LoginRequiredMixin, ListView):
    template = 'lwlife/index.html'
    model = Answer
    context_object_name = 'answers'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = context['answers'].filter(user=self.request.user)
        context['answers'] = context['answers'].filter(ans_date='today')

        return context

class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = "__all__"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(AnswerCreate, self).form_valid(form)
    
def custom_form(request):
    if request.method == "POST":
        my_ques = Question.objects.all()
        
        for i in set(my_ques):
            print(request.POST[f"{i.id}-points"])
            a=Answer.objects.create(user=request.user, ques=i, points=request.POST[f"{i.id}-points"], language=request.POST[f"{i.id}-language"])
            a.save()
                    
        
    my_ques = Question.objects.all()
    print(my_ques[0].question)
    context = {
        "que": my_ques
    }
    return render(request,'lwlife/custom-page.html',context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname 

        myuser.save()
        messages.success(request, "Your Account has been successfully created")
        return redirect('/login')
    return render(request, "lwlife/signup.html")


















def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"lwlife/index.html" , {"fname":fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home')
    return render(request, "lwlife/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Log Our successfully")
    return redirect('home')
