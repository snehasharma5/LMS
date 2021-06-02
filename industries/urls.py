from django.urls import path
from .views import IndustryRegisterView, ShowProfilePage, IndustryDashboard

urlpatterns = [
    path('', IndustryRegisterView.as_view(), name='industry-register'),
    path('industry-profile/<int:pk>', ShowProfilePage.as_view(), name='industry-profile'),
    path('industry-dashboard/<int:pk>', IndustryDashboard.as_view(), name='industry-dashboard'),
]