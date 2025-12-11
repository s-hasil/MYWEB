"""MYWEB URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from main.views import (
    index, about, service, contact, pricing, thank_you,
    bug_reports, register_view, login_view, logout_view,
    profile_view, CustomPasswordResetView
)

urlpatterns = [

    # Default pages
    path('admin/', admin.site.urls),
    path('', register_view, name='home'),   # homepage = register
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('contact/', contact, name='contact'),
    path('pricing/', pricing, name='pricing'),
    path('thank-you/', thank_you, name='thank_you'),
    path('bug_reports/', bug_reports, name='bug_reports'),

    # Auth
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('accounts/', include('allauth.urls')),

    # Password Reset (FULL + CORRECT)
    path(
        'password_reset/',
        CustomPasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url='/password_reset_complete/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'password_reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]

# Static / Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
