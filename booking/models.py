from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField 
from users .models import User
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title  = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    about_main_pic = models.ImageField(upload_to='header/', blank=True, null=True)
    about_pic   = models.ImageField(upload_to='about_images/', blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    our_numbers = models.CharField(max_length=200, null=True, blank=True)
    reload = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title   

class Lessee(models.Model):
    lessee_images = models.ImageField(upload_to='lessee_images/', blank=True, null=True)
    lessee = models.ForeignKey(User, on_delete=models.CASCADE) 
    ministry = models.CharField(max_length=200, null=True, blank=False)
    ministry_address = models.CharField(max_length=100, null=True, blank=False)
    ministry_phone = models.CharField(max_length=100, null=True, blank=False)
    ministry_email = models.CharField(max_length=100, null=True, blank=True)
    ministry_central_location = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    def __str__(self):
         return f'{self.lessee}  {self.ministry}  {self.ministry_address} {self.ministry_phone} {self.ministry_email} {self.ministry_central_location}'
        

class Truck(models.Model):
    truck_image = models.ImageField(upload_to='truck_images/', blank=True, null=True)
    truck_name = models.CharField(max_length=200, null=True, blank=False)
    truck_color = models.CharField(max_length=200, null=True, blank=True)
    truck_plates = models.CharField(max_length=200, null=True, blank=False)
    truck_description = models.CharField(max_length=200, null=True, blank=False)
    timestamp = models.DateTimeField(default=timezone.now)     
    is_published = models.BooleanField(default=False)
    def __str__(self):
         return f'{self.truck_name} {self.truck_color} {self.truck_plates}'
        

class Lessor(models.Model):
    main_image = models.ImageField(upload_to='lesser_images/', blank=True, null=True)
    lessor = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=False)
    phone = models.CharField(max_length=100, null=True, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    central_location = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now) 
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.lessor} {self.phone} {self.central_location} {self.email} {self.address}'
        
class Driver(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    driver_pic = models.ImageField(upload_to='driver_images/', blank=True, null=True)
    truck_assigned = models.ForeignKey(Truck, on_delete=models.CASCADE)
    age = models.CharField(max_length=200, blank=False, null=True)
    date_hired = models.DateTimeField(default=timezone.now) 
    id_number = models.IntegerField()
    def __str__(self):
         return f'{self.driver}  {self.date_hired}  {self.id_number}'    

class Onhire(models.Model): 
    hirer = models.ForeignKey(Lessee, on_delete=models.CASCADE)
    truck_ownership = models.ForeignKey(Lessor, on_delete=models.CASCADE)
    truck  = models.ForeignKey(Truck, on_delete=models.CASCADE)
    mission_location = models.CharField(max_length=200, null=True, blank=True)
    hire_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    def __str__(self):
         return f'{self.hirer}  {self.truck_ownership}  {self.mission_location}'

class Booktruck(models.Model):
    person_hiring_the_truck = models.ForeignKey(User, on_delete=models.CASCADE)
    ministry_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    booking_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    approved = models.BooleanField(default=False, null=True, blank=True)
    unapproved = models.BooleanField(default=True, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.Person_hiring_the_truck }  {self.phone_number}  {self.ministry_name} {self.email} {self.booking_date} {self.return_date}'
        
    def save(self, **kwargs):
        super().save()

