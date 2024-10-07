from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path("", views.home, name="home"),

    #URL REGISTRO LOGIN Y CIERRE SECION
path('signup/', views.signup, name='signup'),
path('logout/', views.signout, name='logout'),
path('signin/', views.signin, name='signin'),

]
