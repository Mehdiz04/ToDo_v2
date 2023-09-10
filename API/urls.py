from django.urls import path
from .views import TaskList , TaskCreate , TaskDetail , BlacklistToken , Register , ResetPassword
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    #authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #create new user
    path('register/' , Register.as_view() , name='register'),
    #logout or something like this
    path('token/blacklist/' , BlacklistToken.as_view() , name='blacklist-token'),
    #reset password
    path('user/reset-password/' , ResetPassword.as_view() , name='reset-password'),
    #.
    path('' , TaskList.as_view() , name='task-list') ,
    path('create/' , TaskCreate.as_view() , name='task-create'),
    path('task/<int:pk>' , TaskDetail.as_view() , name='task-detail')
]