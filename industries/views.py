from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from web_app.models import RegisterModel, Industry
from members.forms import IndustryRegisterForm


class IndustryRegisterView(CreateView):
    model = RegisterModel
    template_name = 'industries/industry_register.html'
    form_class = IndustryRegisterForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'industry'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ShowProfilePage(DetailView):
    model = Industry
    template_name = 'industries/industry_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(*args, **kwargs)
        institute_user = get_object_or_404(Industry, user=self.kwargs['pk'])
        context['institute_user'] = institute_user
        return context
