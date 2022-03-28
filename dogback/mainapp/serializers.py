from pyexpat import model
from rest_framework import serializers

from mainapp.models import Reward, Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ["user"]

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'