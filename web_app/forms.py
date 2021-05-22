from django import forms
from .models import CareerCounsellingFormModel, VideoModel, CourseModel


class CareerCounsellingForm(forms.ModelForm):
    class Meta:
        model = CareerCounsellingFormModel
        fields = ['passion', 'subject', 'work_env', 'future_city', 'your_future', 'ideal', 'purpose']


class VideoUploadingForm(forms.ModelForm):
    class Meta:
        model = VideoModel
        fields = ['title', 'video']


class AddCourseForm(forms.ModelForm):

    class Meta:
        model = CourseModel
        fields = ['course_title', 'category', 'short_intro', 'about_course', 'course_icon', 'course_file', 'duration','price']

