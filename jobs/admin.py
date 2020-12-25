from django.contrib import admin
from.models import jobs,application
# Register your models here.
class jobsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'job_type', 'published_date', 'Employee']
    list_display_links = ['id', 'title']
    list_filter = ['Employee__name']
    list_editable = ['is_published']
    search_fields = ['title', 'description', 'location', 'category',  'nature', 'salary']
    list_per_page = 25

    class Meta:
        model = jobs




admin.site.register(jobs,jobsAdmin)
admin.site.register(application)