from django.views.generic import DetailView, ListView, TemplateView, CreateView
from .models import RegisterModel, CourseModel, CourseCategoryModel
from .models import CareerCounsellingFormModel, VideoModel
from .forms import CareerCounsellingForm, VideoUploadingForm, AddCourseForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = RegisterModel
    template_name = 'web_app/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        all_courses = CourseModel.objects.all()[0:3]
        context['all_courses'] = all_courses
        return context


class ContactView(TemplateView):
    template_name = 'web_app/contact.html'


@method_decorator(login_required, name='dispatch')
class AwareView(TemplateView):
    template_name = 'web_app/aware.html'


class CareerCounsellingFormView(CreateView):
    model = CareerCounsellingFormModel
    form_class = CareerCounsellingForm
    template_name = 'web_app/career_counselling.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class InspireView(ListView):
    model = VideoModel
    template_name = 'web_app/inspire.html'


class VideoUploadingFormView(CreateView):
    model = VideoModel
    form_class = VideoUploadingForm
    template_name = 'web_app/video-upload.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddCourseView(CreateView):
    model = CourseModel
    template_name = 'web_app/add_course_form.html'
    form_class = AddCourseForm
    success_url = reverse_lazy('home')


class CourseDetailView(DetailView):
    model = CourseModel
    template_name = 'web_app/course_detail.html'

    def get_context_data(self, *args, **kwargs):
        course = get_object_or_404(CourseModel, id=self.kwargs['pk'])
        context = {'course': course}
        return context


@method_decorator(login_required, name='dispatch')
class EducateView(ListView):
    model = CourseModel
    template_name = 'web_app/educate.html'


class AllCourseView(ListView):
    model = CourseModel
    template_name = 'web_app/all_courses.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AllCourseView, self).get_context_data(*args, **kwargs)
        category_item = CourseCategoryModel.objects.all()
        context['category'] = category_item
        return context
