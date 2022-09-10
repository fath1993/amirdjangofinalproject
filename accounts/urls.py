from django.urls import path
from accounts.views import login, signup

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='logins'),
    # path('logout/', login, name='logout'),
    path('signup/', signup, name='signup'),

]