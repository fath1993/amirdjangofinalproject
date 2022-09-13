from django.urls import path

from website.views import home, elements, contact, about, newsletter

# it is needed to mention if dynamic urls are used in html
app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('elements/', elements, name='elements'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('newsletter/', newsletter, name='newsletter'),
]
