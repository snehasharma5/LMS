from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from web_app.models import RegisterModel, Expert, Student, CourseModel, JobModel
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


@method_decorator(login_required, name='dispatch')
class ShowProfilePage(DetailView):
    model = Expert
    template_name = 'experts/expert_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        expert_user = get_object_or_404(Expert, user=self.kwargs['pk'])
        context['expert_user'] = expert_user
        return context


@method_decorator(login_required, name='dispatch')
class ExpertUpdateProfilePage(UpdateView):
    model = Expert
    form_class = ExpertProfileForm
    template_name = 'experts/update_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ExpertUpdateProfilePage, self).get_context_data(*args, **kwargs)
        expert_user = get_object_or_404(Expert, user=self.kwargs['pk'])
        context['expert_user'] = expert_user
        return context


@method_decorator(login_required, name='dispatch')
class ExpertDashboard(DetailView):
    model = Expert
    template_name = 'experts/expert_dashboard.html'

    def get_context_data(self, *args, **kwargs):
        students = Student.objects.all()
        jobs = JobModel.objects.filter(user=self.request.user)
        courses = CourseModel.objects.all()
        context = {'students': students, 'courses': courses, 'jobs':jobs}
        return context


@method_decorator(login_required, name='dispatch')
class AllExpertsView(ListView):
    model = Expert
    template_name = 'experts/all_experts.html'

    def get_context_data(self, *args, **kwargs):
        all_experts = Expert.objects.all()[0:8]
        context = {'all_experts': all_experts}
        return context
