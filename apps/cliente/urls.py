from django.urls import path
from . import views

urlpatterns = [
    		path('', views.home, name='Home'),
            path('cadastro',views.create_user, name='cadastro'),
            path('entrar', views.entrar, name='entrar'),
            

	    ]