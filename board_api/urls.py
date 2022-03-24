from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('board_api/', views.BoardList.as_view()),
    path('board_api/<int:pk>/', views.BoardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)