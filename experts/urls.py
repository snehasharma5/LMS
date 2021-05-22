from django.urls import path
from .views import ExpertRegisterView, ShowProfilePage, ExpertUpdateProfilePage, ExpertDashboard, InstituteRegisterView


urlpatterns = [
    path('expert-register/', ExpertRegisterView.as_view(), name='expert-register'),
    path('institute-register/', InstituteRegisterView.as_view(), name='institute-register'),
    path('expert-profile/<int:pk>/', ShowProfilePage.as_view(), name='expert-profile'),
    path('expert-profile-update/<int:pk>', ExpertUpdateProfilePage.as_view(), name='expert-profile-update'),
    path('expert-dashboard/<str:first_name>/<int:pk>', ExpertDashboard.as_view(), name='expert-dashboard'),
]