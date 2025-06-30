from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path("home/", views.HOME, name="home"),
    path("courses/", views.COURSE, name="courses"),
    path("swimming-courses/", views.SWIMMING_COURSE, name="swimming-courses"),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('enroll-swimming/<int:course_id>/', views.enroll_swim_course, name='enroll_swim_course'),
    path("registration/", views.REGISTRATION, name="register"),
    path("swimming-registration/", views.SWIMMING_REGISTRATION, name="swimming-register"),
    path("payments/", views.PAYMENT, name="payment"),
    path("swimming-payments/", views.SWIMMING_PAYMENT, name="swimming-payment"),
    path("contact-us/", views.CONTACT_US, name="contact"),
    path('get-lgas/<int:state_id>/', views.get_lgas, name='get_lgas'),
    path("get-duration/<str:programme>/", views.get_durations, name='get_duration'),
    path("get-swim-duration/<str:programme>/", views.get_swim_durations, name='get_swim_duration'),
    path("term&condition/", views.TERMS_CONDITION, name="term-condition"),
    path("subscribe/", views.subscribe_for_newsletter, name="subscribe_newsletter"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)