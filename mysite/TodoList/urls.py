from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('mytasks/', views.MyTaskListView.as_view(), name='mytasks'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]