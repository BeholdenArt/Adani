from functools import total_ordering
from tokenize import Name
from django.db import models
# Create your models here.

class FeeFormat(models.Model):
    Sem = models.CharField(max_length= 11, null=True)
    AdYear = models.CharField(max_length= 50, null= True)
    Branch = models.CharField(max_length= 10, null=True)
    Type= models.CharField(max_length= 100, null=True)
    Enrollment = models.CharField(max_length=12, null=True)
    Name = models.CharField(max_length= 80, default= "Student Name", null=True)
    AdmissionType = models.CharField(max_length= 100, null=True)
    TuitionFee = models.IntegerField(default= 0, null=True)
    ReceivedFees = models.IntegerField(default= 0, null=True)
    Penalty = models.IntegerField(default= 0, null=True)
    Total = models.IntegerField(default= 0, null=True)
    MOP = models.CharField(max_length= 10, null=True)
    ChNo = models.CharField(max_length= 30, null=True)
    Date = models.CharField(max_length= 100, null=True)
    Bank = models.IntegerField(default= 0, null=True)
    DocumentNo = models.BigIntegerField(default= 0, null=True)
    
    
    def __str__(self):
        return str(self.Enrollment)
    
    