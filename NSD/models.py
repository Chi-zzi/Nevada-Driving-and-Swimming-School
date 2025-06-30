from django.db import models
from django.utils import timezone
import os

# Create your models here.

class Newsletter_DB(models.Model):
    email = models.EmailField(max_length=255, default='', unique=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email


class Driving_Courses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default='')
    duration = models.IntegerField(default=0)
    type = models.CharField(max_length=200, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='driving_courses/')

    def __str__(self):
        return f"{self.name} - {self.type} - {self.duration}"


class Swimming_Courses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='swimming_courses/')

    def __str__(self):
        return f"{self.name} - {self.duration}"


class Driving_Course_Identity_DB(models.Model):
    course = models.ForeignKey(Driving_Courses, on_delete=models.CASCADE, related_name="course_identity")
    course_identity_number = models.CharField(max_length=200, unique=True)
    course_name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200, default='')
    couse_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.course_name} - {self.course_identity_number}"


class Currency_DB(models.Model):
    currency = models.CharField(max_length=10)
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)
    rate = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.currency} - {self.rate}"
    


class Appointment_DB(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    programme = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    message = models.CharField(max_length=500, default='')

    def __str__(self):
        return  f"{self.name} - {self.email} - {self.phone}"
    


class FeedBack_DB(models.Model):
    surname = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to="feedback_profile_images/", default="feedback_profile_images/default.jpg", blank=True, null=True)
    first_name = models.CharField(max_length=200)
    course_type = models.CharField(max_length=150)
    profession = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    feedback = models.TextField()

    def __str__(self):
        return  f"{self.surname} - {self.first_name} - {self.course_type}  -  {self.feedback}"
    

class Contact_Messages_DB(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    


class State_DB(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    states = models.CharField(unique=True, default='', max_length=200)
    capitals = models.CharField(unique=True, default='', max_length=200)

    def __str__(self):
        return self.states
    

class LGA_DB(models.Model):
    lga = models.CharField(max_length=500, default='')
    state = models.ForeignKey(State_DB, on_delete=models.CASCADE, null=True, related_name='lgas')

    def __str__(self):
        return self.lga


class Client_DB(models.Model):
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    mother_maiden_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField()
    blood_group = models.CharField(max_length=50)
    facial_mark = models.CharField(max_length=50)
    glasses = models.CharField(max_length=50)
    height_in_meters = models.DecimalField(max_digits=10, decimal_places=2)
    disability = models.CharField(max_length=50)
    nin = models.CharField(max_length=20, unique=True)
    next_of_kin_phone = models.CharField(max_length=20)
    applicant_phone = models.CharField(max_length=20, unique=True)
    nationality = models.CharField(max_length=150)
    state_of_origin = models.CharField(max_length=200)
    lga_of_origin = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    occupation = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20)
    programme = models.CharField(max_length=150)
    training_duration = models.IntegerField()
    residential_address = models.CharField(max_length=500)
    email = models.EmailField(max_length=200, unique=True)
    profile_picture = models.ImageField(upload_to="clients/profile_pictures/", default="clients/profile_pictures/default.jpg", blank=True, null=True)  # New field

    def __str__(self):
        return f"{self.surname} - {self.firstname} - {self.email} - {self.applicant_phone}"        



class Swimming_Client_DB(models.Model):
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    dob = models.DateField()
    next_of_kin_phone = models.CharField(max_length=20)
    applicant_phone = models.CharField(max_length=20, unique=True)
    previous_experience = models.CharField(max_length=100)
    health_status = models.CharField(max_length=150)
    residential_address = models.CharField(max_length=500)
    programme = models.CharField(max_length=150)
    training_duration = models.IntegerField()

    def __str__(self):
        return f"{self.surname} - {self.firstname} - {self.other_name} - {self.applicant_phone}"        
