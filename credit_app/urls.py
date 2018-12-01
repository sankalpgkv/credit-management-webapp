from django.conf.urls import url
from . import views

app_name='credit_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users_table, name='users'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user_info, name='user_info'),
    url(r'^(?P<user_id>[0-9]+)/credit_transfer/$', views.credit_transfer, name='credit_transfer'),
]

 