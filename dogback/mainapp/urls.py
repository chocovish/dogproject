from django.urls import path,include
from rest_framework import routers

from mainapp.views import RewardViewSet, TaskViewSet,TaskCompleteView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'rewards', RewardViewSet)

urlpatterns = [
    
    path('api/', include(router.urls)),
    path('api/tasks/taskcomplete', TaskCompleteView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]