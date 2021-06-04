from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class RegisterModelManager(BaseUserManager):
    def _create_user(self, email, password= None, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email= email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)


class RegisterModel(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(_('Email Address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False)
    is_industry = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = RegisterModelManager()


class Student(models.Model):
    user = models.OneToOneField(RegisterModel, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(blank=True, upload_to='images/', null=True)
    resume = models.FileField(blank=True, upload_to='resume/', null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    institute_name = models.CharField(max_length=1000, blank=True, null=True)
    linkedIn_url = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.pk)])


class Expert(models.Model):
    user = models.OneToOneField(RegisterModel, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(blank=True, upload_to='images/', null=True)
    resume = models.FileField(blank=True, upload_to='resume/', null=True)
    expertise_area = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField(default=0, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    institute_name = models.CharField(max_length=1000, blank=True, null=True)
    linkedIn_url = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('expert-profile', args=[str(self.pk)])


class Institute(models.Model):
    user = models.OneToOneField(RegisterModel, on_delete=models.CASCADE, primary_key=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    address = models.TextField(blank=True, null=True)
    contact_no = models.IntegerField(blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    linkedIn_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('expert-profile', args=[str(self.pk)])


class Industry(models.Model):
    user = models.OneToOneField(RegisterModel, on_delete=models.CASCADE, primary_key=True)
    industry_type = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ImageField(blank=True, null=True, upload_to='images/')
    address = models.TextField(blank=True, null=True)
    contact_no = models.IntegerField(blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    linkedIn_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('expert-profile', args=[str(self.pk)])


class CareerCounsellingFormModel(models.Model):
    user = models.OneToOneField(RegisterModel, on_delete=models.CASCADE)
    passion = models.CharField(max_length=1000)
    subject = models.CharField(max_length=255)
    work_env = models.CharField(max_length=255)
    future_city = models.CharField(max_length=255)
    your_future = models.CharField(max_length=255)
    ideal = models.CharField(max_length=255)
    purpose = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class VideoModel(models.Model):
    user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    video = models.FileField(null=True, blank=True, upload_to='videos/')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


class CourseModel(models.Model):
    course_title = models.CharField(max_length=500)
    category = models.CharField(max_length=500, default="Machine Learning")
    short_intro = models.CharField(max_length=500, default="Write short detail about course")
    about_course = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    course_file = models.FileField(blank=True, null=True, upload_to="course_files/")
    course_icon = models.ImageField(blank=True, null=True, upload_to="course_icon/")
    enrolled_students = models.ManyToManyField(RegisterModel, related_name='course')

    def __str__(self):
        return self.course_title


class CourseCategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class JobModel(models.Model):
    user = models.ForeignKey(RegisterModel, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    job_requirements = models.CharField(max_length=500)
    job_description = models.TextField()
    stipend = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100)
    contact_mail = models.EmailField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    date_of_posting = models.DateTimeField(default=timezone.now)
    contact_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.user) + " | " + self.job_title + " | " + self.job_type

    def get_absolute_url(self):
        return reverse('home')


class CareerAwareness(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    banner_image = models.ImageField(upload_to='career/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')