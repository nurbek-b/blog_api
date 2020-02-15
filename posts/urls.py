from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/edit/', PostEditView.as_view()),
]