from django.urls import path
from .views import *


urlpatterns = [
    # paths for post
    path('', PostList.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/edit/', PostEditView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view()),

    # paths for comments
    path('comments/', CommentListView.as_view()),
    path('<int:pk>/comments/create/', CommentCreateView.as_view()),
    path('comments/<int:pk>/edit/', CommentEditView.as_view()),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view()),
]