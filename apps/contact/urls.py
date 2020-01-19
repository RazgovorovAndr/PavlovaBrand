from django.conf.urls import url
from apps.contact import views

urlpatterns = [
    url('contact/', views.contact_info, name='contact')
]

