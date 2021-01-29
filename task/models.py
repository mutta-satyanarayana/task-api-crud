from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length= 150, null= False, blank= False)
    created = models.DateTimeField(auto_now= True)
    completed = models.BooleanField(default= False, blank= True, null= True)

    def __str__(self):
        return self.title