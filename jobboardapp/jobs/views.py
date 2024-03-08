from django.shortcuts import render

from .models import Employer, JobApplications, JobSeeker, Jobs
from .serializers import EmployerSerializer, JobApplicationsSerializer, JobsSerializer, SeekerSerializer
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


class EmployerCreate(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class JobsCreate(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class JobsUpdate(generics.UpdateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    lookup_url_kwarg = 'job_id'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class JobsView(generics.ListAPIView):
    serializer_class = JobsSerializer
    def get_queryset(self):
        return Jobs.objects.all()

class EmployerView(generics.ListAPIView):
    serializer_class = EmployerSerializer
    def get_queryset(self):
        return Employer.objects.all()

class SeekerView(generics.ListAPIView):
    serializer_class = SeekerSerializer
    def get_queryset(self):
        return JobSeeker.objects.all()

class JobsViewFilter(generics.ListAPIView):
    serializer_class = JobsSerializer
    def get_queryset(self):
        location = self.kwargs['location']
        return Jobs.objects.filter(location=location)

class JobsViewFilterEmp(generics.ListAPIView):
    serializer_class = JobsSerializer
    def get_queryset(self):
        location = self.kwargs['emp_id']
        return Jobs.objects.filter(emp_id=location)



class JobAppCreate(generics.ListCreateAPIView):
    queryset = JobApplications.objects.all()
    serializer_class = JobApplicationsSerializer

class JobAppView(generics.ListAPIView):
    serializer_class = JobApplicationsSerializer
    def get_queryset(self):
        student_id = self.kwargs['seeker_id']
        return JobApplications.objects.filter(seeker_id=student_id)

class JobAppUpdate(generics.UpdateAPIView):
    queryset = JobApplications.objects.all()
    serializer_class = JobApplicationsSerializer
    lookup_url_kwarg = 'app_id'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    


class SeekerCreate(generics.ListCreateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = SeekerSerializer

class ViewProfile(generics.ListAPIView):
    serializer_class = SeekerSerializer
    def get_queryset(self):
        idd = self.kwargs['seeker_id']
        return JobSeeker.objects.filter(seeker_id=idd)

class ProfileNameUpdate(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = SeekerSerializer
    lookup_field = 'seeker_id'
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        status_value = request.data.get('name')  # Assuming 'status' is the field to be updated
        if status_value is not None:
            instance.name = status_value
            instance.save()
            return Response({'message': 'Name updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Name field is required'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdate(generics.UpdateAPIView):
    queryset = JobSeeker.objects.all()
    serializer_class = SeekerSerializer
    lookup_url_kwarg = 'seeker_id'
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)










