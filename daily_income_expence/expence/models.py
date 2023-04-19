from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Expence(models.Model):
    User = models.ForeignKey(User,on_delete = models.CASCADE)
    expence = models.IntegerField()
    expense_type = models.CharField(max_length=30)
    expence_date = models.DateField(auto_now=True)
    description = models.TextField(max_length = 300)
    
    class Meta:
        db_table = 'expence'
        
from django import forms
        
class ExpenceForm(forms.ModelForm):
    class Meta:
        model = Expence
        fields = '__all__'
