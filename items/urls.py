# items/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, ProjectListCreateView, ProjectDetailView, TaskListCreateView, TaskDetailView, CollaborationListCreateView, CollaborationDetailView


router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('collaborations/', CollaborationListCreateView.as_view(), name='collaboration-list'),
    path('collaborations/<int:pk>/', CollaborationDetailView.as_view(), name='collaboration-detail'),
]