from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^logout',views.Logout.as_view()),
    url(r'^random_request',views.RandomRequest.as_view()),
    url(r'^register_check',views.RegisterCheck.as_view()),
    url(r'^register',views.Register.as_view()),
    url(r'^login_check',views.LoginCheck.as_view()),
    url(r'', views.Index.as_view())
]