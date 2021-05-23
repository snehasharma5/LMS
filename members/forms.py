from django import forms
from web_app.models import RegisterModel, Student, Expert, Institute
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.db import transaction


class StudentRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    institute_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'institute_name', 'qualification', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name= self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.institute_name=self.cleaned_data.get('institute_name')
        student.qualification=self.cleaned_data.get('qualification')
        return user

    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ExpertRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    institute_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    expertise_area = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    experience = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'institute_name', 'qualification', 'expertise_area',
                  'experience', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_expert = True
        user.first_name= self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        expert = Expert.objects.create(user=user)
        expert.institute_name=self.cleaned_data.get('institute_name')
        expert.qualification=self.cleaned_data.get('qualification')
        expert.expertise_area=self.cleaned_data.get('expertise_area')
        return user

    def __init__(self, *args, **kwargs):
        super(ExpertRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class InstituteRegisterForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = RegisterModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'password1', 'password2', 'address']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_institute = True
        user.first_name = self.cleaned_data.get('first_name')
        if self.cleaned_data.get('last_name') == "#":
            user.last_name = ""
        else:
            user.last_name = self.cleaned_data.get('last_name')
        user.save()
        institute = Institute.objects.create(user=user)
        institute.address = self.cleaned_data.get('address')
        return user

    def __init__(self, *args, **kwargs):
        super(InstituteRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['profile_pic', 'resume', 'institute_name', 'qualification', 'linkedIn_url', 'address', 'mobile']


class ExpertProfileForm(forms.ModelForm):

    class Meta:
        model = Expert
        fields = ['profile_pic','expertise_area', 'experience', 'resume', 'institute_name', 'qualification', 'linkedIn_url', 'address', 'mobile']


class InstituteProfileForm(forms.ModelForm):

    class Meta:
        model = Institute
        fields = ['icon', 'contact_no', 'website_url', 'facebook_url', 'linkedIn_url', 'address', 'mobile_no']


class EditSettingsForm(UserChangeForm):
    first_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = RegisterModel
        fields = ('first_name', 'last_name', 'date_of_birth', 'password')


