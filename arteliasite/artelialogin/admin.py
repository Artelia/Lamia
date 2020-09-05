from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Project)


# * Add project admin with project/user manytomany relation
# https://binary-data.github.io/2015/07/21/django-admin-manytomany-inline-enable-add-edit-buttons/


class UserProjectInline(admin.TabularInline):
    model = Project.users.through


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        UserProjectInline,
    ]
    exclude = ("users",)


# * end