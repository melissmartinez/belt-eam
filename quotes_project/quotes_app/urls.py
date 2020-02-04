from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register),
    path('success', views.success, name='success'), 
    path('logout', views.logout), 
    path('login', views.login), 
    path('new_message', views.new_message),
    path('message/<int:id>/delete', views.delete_message),
    path('account/<int:id>/edit', views.edit_account), 
    path('account/<int:id>/update', views.update_account), 
    path('profile/<int:id>', views.show_profile),
]