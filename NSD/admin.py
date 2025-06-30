from django.contrib import admin
from .models import Newsletter_DB, Driving_Courses, Swimming_Courses, Driving_Course_Identity_DB, Currency_DB, Appointment_DB, FeedBack_DB, Contact_Messages_DB, State_DB, LGA_DB, Client_DB, Swimming_Client_DB


class Newsletter1(admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ['email']

class DrivingCourses1(admin.ModelAdmin):
    list_display = ('name', 'type', 'duration', 'price')
    search_fields = ['name', 'duration', 'price']

class Swimming_Courses1(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price')
    search_fields = ['name', 'duration', 'price']


class Currency1(admin.ModelAdmin):
    list_display = ('name', 'currency', 'rate')
    search_fields = ['name', 'rate']

class Appointment1(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'email', 'phone']

class FeedBack1(admin.ModelAdmin):
    list_display = ('surname', 'course_type', 'profession', 'feedback')
    search_fields = ['surname', 'course_type']

class Contact_Messages1(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ['name', 'email']

class State_DB1(admin.ModelAdmin):
    list_display = ('id', 'states', 'capitals')
    search_fields = ['states', 'capitals']

class LGA_DB1(admin.ModelAdmin):
    list_display = ('lga', 'state__states', 'state__capitals')
    search_fields = ['lga', 'state__states', 'state__capitals']


class Client1(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'email', 'nin', 'applicant_phone', 'state_of_origin', 'nationality', 'gender')
    search_fields = ['surname', 'firstname', 'email', 'nin', 'applicant_phone', 'nationality']


class Driving_Course_Identity_DB1(admin.ModelAdmin):
    list_display = ('course', 'course_identity_number', 'course_name', 'type', 'couse_price')
    search_fields = ['course_identity_number', 'course_name', 'type', 'couse_price']

class Swimming_Client_DB1(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'applicant_phone', 'next_of_kin_phone', 'gender')
    search_fields = ['surname', 'firstname', 'other_name', 'applicant_phone', 'gender']


# Register your models here.
admin.site.register(Newsletter_DB, Newsletter1)
admin.site.register(Driving_Courses, DrivingCourses1)
admin.site.register(Swimming_Courses, Swimming_Courses1)
admin.site.register(Driving_Course_Identity_DB, Driving_Course_Identity_DB1)
admin.site.register(Currency_DB, Currency1)
admin.site.register(Appointment_DB, Appointment1)
admin.site.register(FeedBack_DB, FeedBack1)
admin.site.register(Contact_Messages_DB, Contact_Messages1)
admin.site.register(State_DB, State_DB1)
admin.site.register(LGA_DB, LGA_DB1)
admin.site.register(Client_DB, Client1)
admin.site.register(Swimming_Client_DB, Swimming_Client_DB1)
