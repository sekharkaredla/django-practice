from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send_data', views.send_data, name='send_data'),
    url(r'^', views.login, name='login')
]
