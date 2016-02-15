from django.conf.urls import url

from gems import views

urlpatterns = [
    url(r'^(\d+)/$', views.view_gems, name='view_list'),
]

