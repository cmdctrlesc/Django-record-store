from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'mainapp'


urlpatterns = [
    url(r'^$', views.mainview, name="mainview"),
    # path('', views.mainview, name="mainview"),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('search/', views.search, name="searchresults"),



]