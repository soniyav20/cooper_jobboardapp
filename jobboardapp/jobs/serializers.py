from dataclasses import field
from rest_framework import serializers
from .models import JobApplications, Jobs,JobSeeker,Employer


class JobApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model= JobApplications
        fields='__all__'


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields='__all__'

class SeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields='__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields='__all__'
