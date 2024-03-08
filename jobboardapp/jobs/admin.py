from django.contrib import admin
from .models import JobSeeker,JobApplications,Jobs,Employer
admin.site.register(JobSeeker)
admin.site.register(JobApplications)
admin.site.register(Jobs)
admin.site.register(Employer)