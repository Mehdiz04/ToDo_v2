from rest_framework import serializers
from toDoApp.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title' , 'description' , 'completed']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def save(self):
        user = User(username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user