from django.urls import path
from . import views
app_name="bankapp"

urlpatterns = [
    path("",views.demo,name="home"),
    path("formfilling/",views.form_view,name="forms"),
    path("application/",views.newdemo,name="application"),
    path("logout/",views.logout,name="signout"),
]