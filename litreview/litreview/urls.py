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
from django.conf import settings
from django.conf.urls.static import static

from feed import views
from authentication import views as authviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         LoginView.as_view(
                           template_name='authentication/login.html',
                           redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', authviews.signup_page, name='signup'),
    path('password/',
         PasswordChangeView.as_view(template_name='authentication/password.html'),
         name='password-change'),
    path('password/done',
         PasswordChangeDoneView.as_view(template_name='authentication/passchangedone.html'),
         name='password_change_done'),
    path('upload_profile_photo/',authviews.upload_profile_photo,name='upload-profile-photo'),
    path('feed/', views.feed, name='feed'),
    path('follow/', views.follow_users, name='follow-users'),
    path('follow/<int:follow_id>/delete/', views.follow_delete, name='follow-delete'),
    path('tickets/add/', views.ticket_create, name='ticket-add'),
    path('tickets/<int:ticket_id>/', views.ticket_detail,name="ticket"),
    path('tickets/<int:ticket_id>/update/', views.ticket_update, name='ticket-update'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket-delete'),
    path('reviews/add/', views.review_create, name='review-add'),
    path('reviews/<int:review_id>/', views.review_detail,name="review"),
    path('reviews/<int:review_id>/update/', views.review_update, name='review-update'),
    path('reviews/<int:review_id>/delete/', views.review_delete, name='review-delete'),
    path('photos/add/', views.photo_upload, name='photo_upload'),
    path('photos/', views.photo_feed)
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
