from django.conf.urls import url
from . import views

#name corresponds to the url that identifies the view
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
