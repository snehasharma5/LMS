from django.urls import path
from .views import HomeView, ContactView, AwareView, CareerCounsellingFormView, VideoUploadingFormView, AddCourseView,\
    CourseDetailView, EducateView, AllCourseView, InspireView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contactUs/',ContactView.as_view(), name='contact'),
    path('aware/', AwareView.as_view(), name='aware'),
    path('career-counselling-form/<int:pk>/', CareerCounsellingFormView.as_view(), name='career-counselling'),
    path('inspire', InspireView.as_view(), name='inspire'),
    path('upload-your-video/<int:pk>/', VideoUploadingFormView.as_view(), name='video-upload'),
    path('add-course/', AddCourseView.as_view(), name='add-course'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('educate/',EducateView.as_view(), name='educate'),
    path('all-courses/', AllCourseView.as_view(), name='all-courses'),

]