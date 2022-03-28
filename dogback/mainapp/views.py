from urllib import request
from django.shortcuts import render
from rest_framework import viewsets,views
from rest_framework.response import Response
from datetime import date, datetime

from mainapp.models import Reward, Task
from mainapp.serializers import RewardSerializer, TaskSerializer, UserSerializer
# Create your views here.
from mainapp.models import User


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    def get_queryset(self):
        if self.request.GET.get("date",None):
            d = date.fromisoformat(self.request.GET["date"].split("T")[0])
            print("date is",date)
            return Task.objects.filter(user=self.request.user,event_date__date=d).order_by("-id").all()
        else:
            return Task.objects.filter(user=self.request.user).order_by("-id").all()
        # return super().get_queryset()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = TaskSerializer

class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    def get_queryset(self):
        return Reward.objects.filter(user=self.request.user).order_by("-id").all()
        # return super().get_queryset()

class UserUpdateView(views.APIView):
    serializer_class = UserSerializer
    def get(self,request):
        pass

class TaskCompleteView(views.APIView):
    def get(self,request):
        taskid = self.request.GET["taskid"]
        task = Task.objects.get(pk=taskid)
        task.is_completed = True
        task.save()
        Reward.objects.create(task=task,user=self.request.user,point=10)
        return Response(True,200)
