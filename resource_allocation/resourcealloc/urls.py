from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login_check',view=views.login_check,name='login_check'),
    url(r'^', view=views.index, name='index'),
]
