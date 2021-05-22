from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView, ListView
from .forms import StudentRegisterForm, ProfileForm, EditSettingsForm, ExpertRegisterForm
from web_app.models import RegisterModel, Student, CourseModel


class RegisterChoice(ListView):
    model = RegisterModel
    template_name = 'registration/profession_choice.html'


class StudentRegisterView(CreateView):
    model = RegisterModel
    template_name = 'registration/student_register.html'
    form_class = StudentRegisterForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UpdateSettings(UpdateView):
    form_class = EditSettingsForm
    template_name = 'registration/update_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class StudentView(DetailView):
    model = RegisterModel
    template_name = 'registration/student.html'


class ShowProfilePage(DetailView):
    model = Student
    template_name = 'registration/student_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Student, user=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class UpdateProfilePage(UpdateView):
    model = Student
    form_class = ProfileForm
    template_name = 'registration/update_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Student, user=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class DashboardView(DetailView):
    model = RegisterModel
    template_name = 'registration/student_dashboard.html'


class StudentCourseView(DetailView):
    model = CourseModel
    template_name = 'registration/student_course_details.html'

    def get_context_data(self, **kwargs):
        all_courses = CourseModel.objects.filter(enrolled_students=self.request.user)
        context = {'all_courses':all_courses}
        return context
