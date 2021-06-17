from django import forms
from dapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','contact')

class OrgProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('company_name','company_logo','service_provided', 
        'company_docs')