from django.urls import path
from .views import MainPageView, ProfileView, MyLoginView, SignUpView, MyLogoutView, AboutClubView, ScheduleView, KnowledgeView, JoinClubView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('about/', AboutClubView.as_view(), name='about'),
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('knowledge/', KnowledgeView.as_view(), name='knowledge'),
    path('join/', JoinClubView.as_view(), name='join'),

    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
