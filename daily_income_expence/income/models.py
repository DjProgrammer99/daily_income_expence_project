from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Income(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    income = models.IntegerField()
    income_type = models.CharField(max_length=30)
    income_date = models.DateField()
    description = models.TextField(max_length=250)
    
    class Meta:
        db_table = 'income'
        
from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'