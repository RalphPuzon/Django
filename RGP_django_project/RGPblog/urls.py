from django.urls import path
from . import views # '.' == current directory

"""
the first argument from path indicates the url extension that defines
that view. 
"""


urlpatterns = [
    #path('admin/', admin.site.urls), the admin mapping
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]