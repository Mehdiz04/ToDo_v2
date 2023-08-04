from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import Main , DetailTask , Login , register , AddTask , UpdateTask , deleteTask

urlpatterns = [
    path('login/', Login.as_view() , name='login') ,
    path('register/' , register , name='register'),
    path('logout/' , LogoutView.as_view(next_page='login') , name='logout'),
    path('' , Main.as_view() , name='main'),
    path('task/<int:pk>/' , DetailTask.as_view() , name='task'),
    path('add_task/' , AddTask.as_view() , name='add_task' ),
    path('update_task/<int:pk>', UpdateTask.as_view() , name='update_task'),
    path('delete_task/<int:pk>' , deleteTask  , name='delete_task')
]