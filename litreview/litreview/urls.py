"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from feed import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
                               template_name='authentication/login.html',
                               redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('feed/', views.feed, name='feed'),
    path('tickets/add/', views.ticket_create),
    path('tickets/', views.my_posts),
    path('tickets/<int:ticket_id>/', views.ticket_detail,name="ticket"),
    path('tickets/<int:ticket_id>/update/', views.ticket_update, name='ticket-update'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket-delete'),
    path('critics/add/', views.critic_create),
    path('critics/add/<int:ticket_id>/', views.critic_create),
    path('formsent/', views.form_sent,name='form_sent')
]
