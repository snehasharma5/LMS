from django.views.generic import DetailView, ListView, TemplateView, CreateView
from .models import RegisterModel, CourseModel, CourseCategoryModel
from .models import CareerCounsellingFormModel, VideoModel, JobModel, CareerAwareness
from .forms import CareerCounsellingForm, VideoUploadingForm, AddCourseForm, JobPostForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = RegisterModel
    template_name = 'web_app/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        all_career_awareness = CareerAwareness.objects.all()[0:4]
        all_courses = CourseModel.objects.all()[0:3]
        context['all_career_awareness'] = all_career_awareness
        context['all_courses'] = all_courses
        return context


class ContactView(TemplateView):
    template_name = 'web_app/contact.html'


@method_decorator(login_required, name='dispatch')
class AwareView(TemplateView):
    template_name = 'web_app/aware.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class VideoUploadingFormView(CreateView):
    model = VideoModel
    form_class = VideoUploadingForm
    template_name = 'web_app/video-upload.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class AddCourseView(CreateView):
    model = CourseModel
    template_name = 'web_app/add_course_form.html'
    form_class = AddCourseForm
    success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class AllCourseView(ListView):
    model = CourseModel
    template_name = 'web_app/all_courses.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AllCourseView, self).get_context_data(*args, **kwargs)
        category_item = CourseCategoryModel.objects.all()
        context['category'] = category_item
        return context


@method_decorator(login_required, name='dispatch')
class JobPostView(CreateView):
    model = JobModel
    template_name = "web_app/job_post.html"
    form_class = JobPostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class JobDetailView(DetailView):
    model = JobModel
    template_name = 'web_app/job_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(JobDetailView, self).get_context_data(*args, **kwargs)
        job = get_object_or_404(JobModel, id=self.kwargs['pk'])
        context['job'] = job
        return context


@method_decorator(login_required, name='dispatch')
class AllJobsView(ListView):
    model = JobModel
    template_name = 'web_app/all_jobs.html'

    def get_context_data(self, *args, **kwargs):
        all_jobs = JobModel.objects.all()
        context = {'all_jobs': all_jobs}
        return context