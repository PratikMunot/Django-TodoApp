from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    path('update_task/<str:pk>/',views.updateTask,name='update_task'),
    path('delete/<str:pk>/',views.deleteTask,name='delete'),
]
# thats the dynamic url pattern which changes its values at runtime

