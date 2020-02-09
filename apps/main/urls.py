from django.conf.urls import url
from apps.main import views

urlpatterns = [
    url('', views.main_page, name='main')
]

