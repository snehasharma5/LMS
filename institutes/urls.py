from django.urls import path
from .views import InstituteRegisterView, ShowProfilePage, InstituteUpdateProfilePage

urlpatterns = [
    path('institute-register/', InstituteRegisterView.as_view(), name='institute-register'),
    path('institute-profile/<int:pk>/', ShowProfilePage.as_view(), name='institute-profile'),
    path('institute-profile-update/<int:pk>', InstituteUpdateProfilePage.as_view(), name='institute-profile-update'),
]