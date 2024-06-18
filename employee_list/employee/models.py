from django.db import models

# Create your models here.
POSITION_CHOICES = {'': 'Select Position','Manager': 'Manager','Developer': 'Developer','Designer': 'Designer','QA': 'QA', 'HR': 'HR',}
class EmployeeDetails(models.Model):
    fullname = models.CharField(max_length=30)
    emp_no = models.CharField(max_length=10)
    phone = models.IntegerField()
    # position = models.CharField(max_length=30)
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)

    def __str__(self):
        return {{self.fullname}}