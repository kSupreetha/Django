from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.confirm_delete, name='confirm_delete'),  # Show confirmation
    path('delete-confirmed/<int:id>/', views.delete_student, name='delete_student'),  # Actual delete
]
