from django.db import models

class Employer(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    contact= models.IntegerField()
    def __str__(self):
        return self.name

class JobSeeker(models.Model):
    seeker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    resumelink = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mailid = models.EmailField()
    contact= models.IntegerField()
    def __str__(self):
        return self.name

class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(Employer,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    experience = models.IntegerField()
    salary = models.IntegerField()
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    postdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Job # -{self.title} {self.description} {self.location} ()"

class JobApplications(models.Model):
    STATUS_CHOICES = [
        ('hired', 'Pending'),
        ('interviewing', 'Interviewing'),
        ('applied', 'Applied'),
    ]
    app_id = models.AutoField(primary_key=True)
    coverletter = models.TextField()
    seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    appdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='applied')
    def __str__(self):
        return f"Complaint # - ({self.status})"

