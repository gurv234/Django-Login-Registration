from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model): 
    SERVICES = (
    ('1', 'Service Type 1'),
    ('2', 'Service Type 2'),
    ('3', 'Service Type 3'),
    ('4', 'Service Type 4'),
    ('5', 'Service Type 5')
    )
    # USER DETAILS:
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, blank=True, verbose_name='Phone Number')
    profile_pic = models.ImageField(upload_to='profile_up',blank=True, verbose_name='Profile Picture')
    # COMPANY DETAILS:
    company_name = models.CharField(max_length=60, default='N/A', blank=True, verbose_name='Registered Name of Company')
    company_logo = models.ImageField(upload_to='logo_up',blank=True, verbose_name='Company Logo')
    company_docs = models.FileField(upload_to='docs_up', blank=True, verbose_name='Company Registration Documents')
    service_provided = models.CharField(choices=SERVICES, max_length=80, default='N/A', blank=True)

def __str__(self):
    return self.user.username