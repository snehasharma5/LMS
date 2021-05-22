from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Student, CareerCounsellingFormModel, VideoModel, CourseModel, CourseCategoryModel, Expert


admin.site.site_header = 'Predulive Edutech Foundation Admin Dashboard'


class RegisterModelAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_student', 'is_expert', 'is_institute', 'is_industry', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'date_of_birth')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), RegisterModelAdmin)
admin.site.register(Student)
admin.site.register(Expert)
# admin.site.register(Institute)
admin.site.register(VideoModel)
admin.site.register(CourseModel)
admin.site.register(CourseCategoryModel)
admin.site.register(CareerCounsellingFormModel)

# Register your models here.
