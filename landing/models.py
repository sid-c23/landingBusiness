from django.db import models

# Create your models here.
class UserLead(models.Model):
    f_name = models.CharField(max_length=50, verbose_name='First Name')
    email = models.EmailField()
    dateEntered = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date Entered')

    def __str__(self):
        return self.f_name