from django.conf.urls import url
from . import views

# patterns matching url for the index/
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
