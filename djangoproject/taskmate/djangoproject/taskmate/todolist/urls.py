from django.urls import path
from todolist import views

urlpatterns = [
    path('delete/<task_id>', views.deletetask, name='deletetask'),
    path('edit/<task_id>', views.edittask, name='edittask'),
    path('complete/<task_id>', views.completetask, name='completetask'),
    path('pending/<task_id>', views.pendingtask, name='pendingtask'),

]
