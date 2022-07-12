
from django.db import models
# from PIL import Image 
import datetime

# Create your models here.
class Community(models.Model):
    community_id = models.IntegerField(max_length=200, default="123456")
    title = models.CharField(max_length=200, default="Developer Skills")
    champions = models.CharField(max_length=250, default="Lupita Tiara")



class Student(models.Model):
    first_name=models.CharField(max_length=10, default="Shanel")
    last_name = models.CharField(max_length=10, default="Lopez",)
    age = models.PositiveSmallIntegerField(default=29)
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=9, default=867)
    email = models.EmailField(default="shanelopez@gmail.com")
    registration = models.PositiveIntegerField(default=1324)
    phone_number = models.PositiveIntegerField(default=3211283957)
    guardian_name = models.CharField(max_length=15,default="Murathi",null=True,blank=True)
    guardian_contacts = models.PositiveIntegerField(default=2987653245)
    country = models.CharField(max_length=20, default=40,null=True,blank=True)
    # medical_report = models.FileField(default="default.png",null=True,blank=True)
    # class_name = models.CharField(max_length=12, default=30,null=True,blank=True)
    # room_number = models.CharField(max_length=15, default=60,null=True,blank=True)
    # big_sister = models.CharField(max_length=20, default=40)
    mentors_name = models.CharField(max_length=35, default=50,null=True,blank=True)
    passport_photo = models.ImageField(default="default.jpeg",null=True,blank=True)
    profile=models.ImageField(default="default.jpng")

    def __str__(self):
        return self.first_name


    def full_name(self):
        return f"{self.first_name}{self.last_name}"

    def year_of_birth(self):
        return datetime.datetime.now().year-self.age    

        



