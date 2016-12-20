from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dashboard$', (views.index)),
    url(r'create_page$',(views.create_page)),
    url(r'create$', views.create),
    url(r'delete/(?P<id>\d*)$', views.delete),
    url(r'logout$',views.logout),
    url(r'product_page/(?P<id>\d*)$', views.product_page),
    url(r'add/(?P<id>\d*)$',views.add),
    url(r'remove/(?P<id>\d*)$', views.remove)
    ]
