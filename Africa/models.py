
from django.db import models
# from PIL import Image 
import datetime

# Create your models here.
class Community(models.Model):
    community_id = models.IntegerField()
    title = models.CharField(max_length=200,null=True)
    champions = models.CharField(max_length=250,null=True)



class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    national_id = models.CharField(max_length=9)
    email = models.EmailField()
    # registration = models.PositiveIntegerField(registration,on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField()
    guardian_name = models.CharField(max_length=15)
    guardian_contacts = models.PositiveIntegerField()
    country = models.CharField(max_length=20)
    medical_report = models.FileField(default="default.png",null=True)
    class_name = models.CharField(max_length=12, default=30,null=True)
    mentors_name = models.CharField(max_length=35, default=50,null=True)
    passport_photo = models.ImageField(default="",null=True)
    profile=models.ImageField(default="default.jpng")
# def __str__(self):
#         return self.first_name


# def full_name(self):
#         return f"{self.first_name}{self.last_name}"

# def year_of_birth(self):
#         return datetime.datetime.now().year-self.age


class Course(models.Model):
   name_of_the_course=models.CharField(max_length=10,null=True)
   course_code=models.CharField(max_length=20,null=True)
   syllabus=models.CharField(max_length=10,null=True)
   description=models.CharField(max_length=20,null=True)
   course_unit=models.CharField(max_length=15,null=True)
   course_duration=models.CharField(max_length=3,null=True)
   course_material=models.CharField(max_length=18,null=True)

#    def __str__(self):
#         return self.first_name
        



class Trainer(models.Model):
    first_name = models.CharField(max_length=10,null=True)
    last_name=models.CharField(max_length=25,null=True)
    email=models.EmailField(default=30,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    course=models.CharField(max_length=20,null=True)
    trainers_id=models.CharField(max_length=10,null=True)
    no_of_lessons_attended=models.PositiveSmallIntegerField(default=1,null=True)
    bank_account=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=15,null=True)
    profile_trainer=models.CharField(max_length=20,null=True)
    profession=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=15,null=True)
    image=models.ImageField(default="img.jpeg")
    cv=models.FileField(default="file.pdf")

    

