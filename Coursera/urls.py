"""Coursera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500
from django.contrib.auth import views as auth_view

handler404 = 'courses.views.view_404'
handler500 = 'courses.views.view_500'
handler403 = 'courses.views.view_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls',namespace='courses')),
    path('', include('blog.urls',namespace='blogs')),
    path('', include('memberships.urls',namespace='memberships')),
    path('', include('users.urls',namespace='')),
    path('accounts/', include('allauth.urls')),
    path('password-reset/',auth_view.PasswordResetView.as_view(
        template_name='users/password_reset.html'),
    name='password_reset'),

    path('password-reset/done/',
        auth_view.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name ='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    name='password_reset_confirm'),

     path('password-reset-complete/',auth_view.PasswordResetView.as_view(
        template_name='users/password_reset_complete.html'),
    name='password_reset_complete'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
