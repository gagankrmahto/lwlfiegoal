from django.contrib import admin
from django.urls import path, include
from . import views
from . views import AnswerCreate, TaskCreate, TaskList,TaskDetail, TaskUpdate, TaskDelete,CustomLoginView, AnswerView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
  
    path('', AnswerView.as_view(), name="home"),
    path('create/', AnswerCreate.as_view(), name="create"),
    path('create-today/', views.custom_form, name="create-today"),

    path('tasks/',TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(), name='task-delete'),
    path('signup/',views.signup, name="signup"),
    path('signin/',views.signin, name="signin"),
    path('signout/',views.signout, name="signout"),
]