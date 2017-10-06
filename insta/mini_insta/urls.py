from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^liked',views.AddLike.as_view()),
    url(r'^',views.IndexPage.as_view())
]