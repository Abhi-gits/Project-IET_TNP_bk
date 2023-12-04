from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
# Create your models here.
from api.account.models import User

# Create your models here.

branch_choices = (
    ('CSE', 'Computer Science & Engineering'),
    ('ECE', 'Electronics & Communication Engineering'),
    ('ME', 'Mechanical Engineering'),
    ('CE', 'Civil Engineering'),
    ('EE', 'Electrical Engineering'),
)


status_choices = (
    ('approved', 'Approved'),
    ('not_approved', 'Not Approved'),
    ('pending', 'Pending'),
    ('rejected', 'Rejected')
)


class Batch(models.Model):
    starting_year = models.IntegerField()
    ending_year = models.IntegerField()
    
    class Meta:
        ordering = ['-starting_year']
        
    def __str__(self):
        return str(self.starting_year) + ' - ' + str(self.ending_year)
    
    def clean(self):
        if self.starting_year < 1996:
            raise ValidationError('Starting year must be greater than 1996')
        if self.ending_year > datetime.now().year + 4:
            raise ValidationError(f'Ending year must be smaller than {datetime.now().year + 4}')
        if self.starting_year > self.ending_year:
            raise ValidationError('Starting year must be less than ending year')
        if (self.ending_year - self.starting_year) == 3:
            raise ValidationError('Batch duration must be 4 years')
    
class Placement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    student_branch = models.CharField(max_length=255, choices=branch_choices)
    student_roll_no = models.CharField(max_length=255)
    student_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    student_salary = models.CharField(max_length=255)
    position_offered = models.CharField(max_length=255)
    company_offer_letter = models.URLField(max_length=255, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=status_choices, default='pending')
    
    class Meta:
        ordering = ['-created_at']

    # return company name + name of user
    def __str__(self):
        return self.company_name + ' - ' + self.user.name
    


class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    student_branch = models.CharField(max_length=255, choices=branch_choices)
    student_roll_no = models.CharField(max_length=255)
    student_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_duration = models.CharField(max_length=255)
    course_certificate = models.URLField(max_length=255, blank=True, null=True)
    course_fee = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=status_choices, default='pending')
    
    
    
    class Meta:
        ordering = ['-created_at']

    # return course name + name of user
    def __str__(self):
        return self.course_name + ' - ' + self.user.name
    