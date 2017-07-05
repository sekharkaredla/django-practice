from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^send_data',views.output,name='output'),
    url(r'^show_data',views.show,name='show'),
    url(r'^',views.input,name='input'),
]