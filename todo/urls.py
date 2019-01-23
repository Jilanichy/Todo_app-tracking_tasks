from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<task_id>', views.delete, name='delete'),
    path('cross_off/<task_id>', views.cross_off, name='cross_off'),
    path('uncross/<task_id>', views.uncross, name='uncross'),
    path('edit/<task_id>', views.edit, name='edit'),
]
