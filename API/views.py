# from django.contrib.auth import logout
from rest_framework.status import HTTP_400_BAD_REQUEST , HTTP_200_OK , HTTP_201_CREATED
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import TaskSerializer , UserRegisterSerializer
from toDoApp.models import Task

# Create your views here.

class TaskList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)



class TaskCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    

#logout stuff  
class BlacklistToken(APIView):
    def post(self , request):
        try:
            token = request.data.get('refresh')
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
            # logout(request.user)
            return Response({'message':'Token blacklisted'} , status=HTTP_200_OK)
        except Exception:
            return Response({'error': 'Token not found or already revoked'}, status=HTTP_400_BAD_REQUEST)



class Register(APIView):
    def post(self , request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message':'user created' , 'user':user.username} , status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=HTTP_201_CREATED)
        


class ResetPassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request):
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        user = self.request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response({'message':'password updated'} , status=HTTP_200_OK)
        else:
            return Response({'error':'old password mismatch'} , status=HTTP_400_BAD_REQUEST)