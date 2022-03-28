from django.contrib import admin
from mainapp.models import Task,Reward,User
# Register your models here.
admin.site.register(Task)
admin.site.register(Reward)
admin.site.register(User)