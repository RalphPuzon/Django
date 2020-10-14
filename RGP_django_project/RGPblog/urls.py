from django.urls import path
from . import views # '.' == current directory
from .views import (PostListView,
					PostDetailView,
					PostCreateView,
					PostUpdateView,
					PostDeleteView,
					UserPostListView)

"""
the first argument from path indicates the url extension that defines
that view. the "name" for each path is for HTML referencing
"""


urlpatterns = [
    #path('admin/', admin.site.urls), the admin mapping
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),                         # route to home page
    # <int:pk> allows us to grab the value from the URL,
    # detail view expects pk so we use pk:
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),         # route to individual post
    path('post/new/', PostCreateView.as_view(), name='post-create'),              # route to create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # route to update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # route to delete post
    path('about/', views.about, name = 'blog-about'),                             # route to about page
]