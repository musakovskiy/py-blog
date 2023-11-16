from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),  # Redirect to post list view for the root URL
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('commentary/create/<int:pk>/', CommentaryCreateView.as_view(), name='commentary-create'),
]


app_name = "blog"
