from django.db import models
from django.contrib.auth.models import AbstractUser


class StaffBase(AbstractUser):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_of_birth = models.DateField(null=True, blank=True)
  phone_number = models.CharField(max_length=15)

  def get_role(self):
    return f"{self.last_name}"

  
  def __str__(self):
    return f"{self.first_name}, {self.last_name}, {self.date_of_birth}, {self.phone_number }"

class Manager(models.Model):
  user = models.ForeignKey(StaffBase, on_delete=models.CASCADE, related_name='addresses')
  department = models.CharField(max_length=70)
  has_company_card = models.BooleanField(default="yes")

  def get_role(self):
    return f"{self.department}"

  def __str__(self):
    return f"{self.department}, {self.has_company_card}"

class Intern(models.Model):
  mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
  internship_end = models.DateField

  def get_role(self):
    return f"{self.department}"

  def __str__(self):
    return f"Internship ends at {self.internship_end}"

