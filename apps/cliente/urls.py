from django.urls import path
from . import views

urlpatterns = [
    		path('', views.home, name='Home'),
            path('cadastro',views.create_user, name='create_user'),
            path('entrar', views.entrar, name='entrar'),
	    ]