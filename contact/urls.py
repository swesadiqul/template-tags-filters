from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_view, name="contact"),
    path('contact-list/', views.contact_list, name="contact_list"),
    path('create_account/', views.usercreation, name="create_account"),
]
