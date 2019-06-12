from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def _str (self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone}'