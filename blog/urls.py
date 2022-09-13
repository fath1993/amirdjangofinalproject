from django.urls import path
from blog.views import blog_home, blog_single, blog_search
from blog.feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('<int:pid>', blog_single, name='blog-single'),
    path('category/<str:cat_name>', blog_home, name='category'),
    path('tag/<str:tag_name>', blog_home, name='tag'),
    path('author/<str:author_username>', blog_home, name='author'),
    path('search/', blog_search, name='search'),
    path('rss/feed/', LatestEntriesFeed()),
]
