from django.db import models

# Create your models here.
from api.account.models import User

# Create your models here.
class Placement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, required=True)
    company_name = models.CharField(max_length=255, required=True)
    company_email = models.EmailField(null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    company_salary = models.CharField(max_length=255, required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    # return company name + name of user
    def __str__(self):
        return self.company_name + ' - ' + self.user.name
    


class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_duration = models.CharField(max_length=255)
    course_fee = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    # return course name + name of user
    def __str__(self):
        return self.course_name + ' - ' + self.user.name
    