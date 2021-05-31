from django.urls import path
from .views import StudentRegisterView, StudentView, ShowProfilePage, UpdateSettings, UpdateProfilePage, \
    RegisterChoice, DashboardView, StudentCourseView, StudentVideoView

urlpatterns = [
    path('member-register/', RegisterChoice.as_view(), name='member-register'),
    path('student-register/', StudentRegisterView.as_view(), name='student-register'),
    path('student/<int:pk>', StudentView.as_view(), name='student'),
    path('profile/<str:pk>', ShowProfilePage.as_view(), name='profile'),
    path('user-settings/<int:pk>', UpdateSettings.as_view(), name='user-settings'),
    path('user-profile/<int:pk>', UpdateProfilePage.as_view(), name='user-profile'),
    path('dashboard/<str:first_name>/<int:pk>', DashboardView.as_view(), name='dashboard'),
    path('student-course/<int:pk>', StudentCourseView.as_view(), name='student-course'),
    path('student-video/<int:pk>', StudentVideoView.as_view(), name='student-video'),
]
