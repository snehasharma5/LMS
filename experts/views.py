from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from web_app.models import RegisterModel, Expert, Student, CourseModel
from members.forms import ExpertRegisterForm, ExpertProfileForm, InstituteRegisterForm


class ExpertRegisterView(CreateView):
    model = RegisterModel
    template_name = 'experts/expert_register.html'
    form_class = ExpertRegisterForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'expert'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowProfilePage(DetailView):
    model = Expert
    template_name = 'experts/expert_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        expert_user = get_object_or_404(Expert, user=self.kwargs['pk'])
        context['expert_user'] = expert_user
        return context


class ExpertUpdateProfilePage(UpdateView):
    model = Expert
    form_class = ExpertProfileForm
    template_name = 'experts/update_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ExpertUpdateProfilePage, self).get_context_data(*args, **kwargs)
        expert_user = get_object_or_404(Expert, user=self.kwargs['pk'])
        context['expert_user'] = expert_user
        return context


class ExpertDashboard(DetailView):
    model = Expert
    template_name = 'experts/expert_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        students = Student.objects.all()
        courses = CourseModel.objects.all()
        context = {'students': students, 'courses': courses}
        return context
