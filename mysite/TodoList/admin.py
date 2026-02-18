from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Task, TaskReview, CustomUser

class TaskReviewInLine(admin.TabularInline):
    model = TaskReview
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'doer', 'status', 'due_date']
    list_filter = ['status', 'doer', 'due_date']
    list_editable = ['status', 'due_date']
    inlines = [TaskReviewInLine]

class TaskReviewAdmin(admin.ModelAdmin):
    list_display = ['task', 'reviewer', 'date_created', 'content']

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets +(
    ('Additional Info', {'fields': ('photo',)}),
    )

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskReview, TaskReviewAdmin)
admin.site.register(CustomUser, CustomUserAdmin)