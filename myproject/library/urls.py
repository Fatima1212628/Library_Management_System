from django.urls import path
from . import views

urlpatterns = [
    path('issue/', views.issue_book, name='issue_book'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
]