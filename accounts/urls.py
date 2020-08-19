from django.urls import path
from.import views


urlpatterns = [
    path("registr",views.registr,name="registr"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout")

]