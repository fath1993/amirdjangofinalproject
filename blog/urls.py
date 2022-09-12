from django.urls import path
from blog.views import blog_home, blog_single

app_name = 'blog'
urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('<int:pid>', blog_single, name='blog-single')
]
