from django import forms
from .models import CareerCounsellingFormModel, VideoModel, CourseModel, JobModel, CareerAwareness


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
        fields = ['course_title', 'category', 'short_intro', 'about_course', 'course_icon', 'course_file',
                  'duration', 'price']


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['job_type', 'job_title', 'job_requirements', 'job_description', 'stipend', 'location',
                  'contact_mail', 'duration', 'contact_number']


class CareerAwarenessForm(forms.ModelForm):
    class Meta:
        model = CareerAwareness
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter or Paste Link'}),
        }