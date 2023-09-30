from django.db import models

# Create your models here.
from api.account.models import User

# Create your models here.
class Placement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, required=True)
    company_email = models.EmailField(required=False)
    company_website = models.URLField(required=False)
    company_address = models.CharField(max_length=255, required=False)
    company_phone = models.CharField(max_length=255, required=False)
    company_salary = models.CharField(max_length=255, required=True)
    company_location = models.CharField(max_length=255, required=False)
    company_category = models.CharField(max_length=255, required=False)
    company_status = models.BooleanField(default=False)
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
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_duration = models.CharField(max_length=255)
    course_fee = models.CharField(max_length=255)
    course_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    # return course name + name of user
    def __str__(self):
        return self.course_name + ' - ' + self.user.name
    