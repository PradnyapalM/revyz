from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class api_s(models.Model):
    tech = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('ruby', 'Ruby'),
        ('docker', 'Docker'),
        ('node', 'Node'),
        ('javascript', 'JavaScript'),
    )
    Name  = models.CharField(max_length=120)
    Address  = models.CharField(max_length=120)
    City = models.CharField(max_length=120,default="")
    Number = models.IntegerField(null=True)
    Email = models.EmailField(null=True)
    Tech_skill  = models.CharField(max_length=120, choices= tech)

    def _str_(self):
        return self.Name


