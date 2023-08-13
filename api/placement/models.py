from django.db import models

# Create your models here.
from api.account.models import User

# Create your models here.
class Placement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_website = models.URLField()
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    company_salary = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)
    company_category = models.CharField(max_length=255)
    company_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    # return company name + name of user
    def __str__(self):
        return self.company_name + ' - ' + self.user.name
    

