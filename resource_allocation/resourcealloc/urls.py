from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login_check',views.Login_check.as_view()),
    url(r'^', views.Index.as_view()),
]
