from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import now, timedelta
from django.utils.crypto import get_random_string
from django.http import JsonResponse
from django.templatetags.static import static
import json
from django.conf import settings
from .models import Newsletter_DB, Driving_Courses, Swimming_Courses, Currency_DB, Appointment_DB, FeedBack_DB,  Contact_Messages_DB,  Client_DB, Swimming_Client_DB, Driving_Course_Identity_DB, State_DB, LGA_DB
import os
import re
from django.conf import settings
from django.utils.html import strip_tags


# Create your views here.
def HOME(requests):
    driving_courses = Driving_Courses.objects.all()
    swimming_courses = Swimming_Courses.objects.all()
    feedbacks = FeedBack_DB.objects.all()


    hero_images = []

    # Accessing the Hero-Carousel Folder
    hero_carousel_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'hero-carousel')

    if os.path.exists(hero_carousel_path):

        # Get all image filenames in the directory (Only JPG files)
        for img in os.listdir(hero_carousel_path):
            if img.lower().endswith(".jpg"):
                hero_images.append(f"images/hero-carousel/{img}")

        # hero_images = [
        #     f"images/hero-carousel/{img}"
        #     for img in os.listdir(hero_carousel_path)
        #     if img.lower().endswith((".jpg"))
        # ]

            # hero_images = [
        #     "images/hero-carousel/hero-1.jpg",
        #     "images/hero-carousel/hero-2.jpg",
        #     "images/hero-carousel/hero-3.jpg",
        # ]
        # print(hero_images)
    else:
        hero_images = []  # Return an empty list if the directory doesn't exist


    context = {
        "hero_images": hero_images,
        "driving_courses": driving_courses,
        "swimming_courses": swimming_courses,
        "feedbacks": feedbacks
        }


    if requests.method == "POST":
        try:
            data = json.loads(requests.body)  # Parse JSON data

            name = data.get("name", "").strip()
            email = data.get("email", "").strip()
            phone = data.get("phone", "").strip()
            programme = data.get("programme", "").strip()
            state = data.get("state", "").strip()
            country = data.get("country", "").strip()
            message = data.get("message", "").strip()

            print(email)
            print(programme, state, country)

            # Calculate Appointment Date (2 days from today)
            # appointment_date = datetime.today() + timedelta(days=2)
            # appointment_location = "Marilyn Auto Schools, 123 Main Street, Your City"
            # instructor_details = "John Doe, Certified Driving Instructor"

            # appointment_date.strftime('%A, %d %B %Y')

            # Check if email or phone already exists
            # appointment, created = Appointment_DB.objects.update_or_create(
            #     email=email, 
            #     defaults={
            #         "name": name,
            #         "phone": phone,
            #         "course_type": course_type,
            #         "car_type": car_type,
            #         "message": message
            #     }
            # )

            # Check if a record exists with the given email
            appointment = Appointment_DB.objects.filter(email=email).first()

            if not appointment:
                # If no record found with email, check for phone
                appointment = Appointment_DB.objects.filter(phone=phone).first()

            if appointment:
                # If a record is found (either by email or phone), update it
                appointment.name = name
                appointment.email = email
                appointment.phone = phone
                appointment.programme = programme
                appointment.state = state
                appointment.message = message
                appointment.country = country
                appointment.save()
                created = False  # Indicates record was updated
            else:
                # If no record exists with either email or phone, create a new one
                appointment = Appointment_DB.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    programme=programme,
                    state=state,
                    country=country,
                    message=message
                )
                created = True  # Indicates new record was created

            # Send Confirmation Email
            subject = "Appointment Confirmation - Nevada Driving School"
            message_body = f"Dear {name.split()[0]},\n\nThank you for booking an appointment with Nevada Driving School.\nYour appointment has been received and will be reviewed soon.\n\nOnce Reviewed, An Email will be sent to you containing the 📅 Appointment Date and 📍Location .\n\nBest regards,\n\nNevada Driving School Team"

            send_mail(
                subject, 
                message_body, 
                "chizzichukwudubem@gmail.com",  # Replace with your sender email
                [email], 
                fail_silently=False
            )

            return JsonResponse({"message": "Appointment Submitted Successfully"}, status=200)
        
        except:
            return JsonResponse({"error": "An Error occurred while submitting your appointment, Try again!"}, status=500)

    return render(requests, "NSD/home_page.html", context)


def subscribe_for_newsletter(requests):
    if requests.method == "POST":
        try:
            data = json.loads(requests.body)  # Parse JSON data
            email = data.get("email", "").strip()

            if email:

                subscribed = Newsletter_DB.objects.filter(email=email).first()
                if subscribed:
                    pass
                else:
                    # newletter = Newsletter_DB.objects.get_or_create(email=email)
                    newletter = Newsletter_DB.objects.create(email=email)
                    newletter.save()

                    print(f"Received email: {email}")  # Debugging

                return JsonResponse({"message": "Successfully subscribed!"}, status=201)
            else:
                return JsonResponse({"error": "Invalid email address"}, status=400)

        except Exception as e:
            return JsonResponse({"error": "An Error occurred while subscribing for newsletter,  Try again!"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)



def COURSE(requests):
    driving_courses = Driving_Courses.objects.all()

    # for i in driving_courses:
    #     print(i.description)

    context = {
        "driving_courses": driving_courses
    }

    return render(requests, "NSD/course_page.html", context)


def SWIMMING_COURSE(requests):
    swimming_courses = Swimming_Courses.objects.all()

    context = {
        "swimming_courses": swimming_courses
    }

    return render(requests, "NSD/swimming_course_page.html", context)



def enroll_course(requests, course_id):

    # # Check if user is logged in
    # client_id = requests.session.get("client_id")
    # client_email = requests.session.get("client_email")    

    # if not client_id or not client_email:
    #     return redirect("login")
    
    # Get the clicked course
    course = get_object_or_404(Driving_Courses, id=course_id)

    # # Store the course info in the session
    # requests.session["client_id"] = client_id
    # requests.session["client_email"] = client_email

    requests.session["selected_course_id"] = course.id
    requests.session["selected_course_name"] = course.name
    # requests.session["selected_course_type"] = course.type
    requests.session["selected_course_price"] = str(course.price)
    requests.session["selected_course_duration"] = course.duration

    # Set session expiry
    # requests.session.set_expiry(5 * 60)  # 5 minutes


    # client = Client_DB.objects.filter(email=client_email).first()  # Get instructor by email
    # if client:
    #     get_client = Client_DB.objects.get(email = client_email)
    #     registrations = get_client.registrations.all().first()

    #     if registrations:            
    #         if registrations.status == "Active":
    #             requests.session["client_id"] = client.id  # Store session manually
    #             requests.session["client_email"] = client.email

    #             requests.session.set_expiry(5 * 60)  # 5 minutes
                        
    #             return redirect("client")

    #         else:
    #             # Redirect to payment page
    #             return redirect("payment")

        # else:
            # Redirect to payment page
    return redirect("register")



def enroll_swim_course(requests, course_id):
    # Get the clicked course
    course = get_object_or_404(Swimming_Courses, id=course_id)

    # # Store the course info in the session
    # requests.session["client_id"] = client_id
    # requests.session["client_email"] = client_email

    requests.session["selected_course_id"] = course.id
    requests.session["selected_course_name"] = course.name
    # requests.session["selected_course_type"] = course.type
    requests.session["selected_course_price"] = str(course.price)
    requests.session["selected_course_duration"] = course.duration


    return redirect("swimming-register")



def get_durations(requests, programme):
    # get_durations = Driving_Courses.objects.filter(name=programme).values('name', 'description', 'duration', 'type', 'price')
    get_durations = Driving_Courses.objects.filter(name=programme).values('duration')
    print(list(get_durations)[0]['duration'])
    return JsonResponse({'duration': list(get_durations)[0]['duration']})


def get_swim_durations(requests, programme):
    # get_durations = Driving_Courses.objects.filter(name=programme).values('name', 'description', 'duration', 'type', 'price')
    get_durations = Swimming_Courses.objects.filter(name=programme).values('duration')
    print(list(get_durations)[0]['duration'])
    return JsonResponse({'duration': list(get_durations)[0]['duration']})


def get_lgas(request, state_id):
    state = get_object_or_404(State_DB, id=state_id)
    # print(state_id)
    lgas = LGA_DB.objects.filter(state=state).values('id', 'lga')
    return JsonResponse({'lgas': list(lgas)})





def REGISTRATION(requests):
    currencies = Currency_DB.objects.all()
    courses = Driving_Courses.objects.all()
    states = State_DB.objects.all()
    # print(states)

    courses_names = []

    for each_course in courses:
        if each_course.name in courses_names:
            pass
        else:
            courses_names.append(each_course.name)



    error_messages = []

    flag_images = {}

    flag_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'country-flag')

    # if os.path.exists(flag_image_path):

    #     # Get all image filenames in the directory (Only JPG files)
    #     for img in os.listdir(flag_image_path):
    #         if img.lower().endswith(".jpg"):
    #             flag_images.append(f"images/country-flag/{img}")

    if os.path.exists(flag_image_path):
        for img in os.listdir(flag_image_path):
            if img.lower().endswith(".jpg"):
                # Normalize filename to match country name lookup
                country_key = os.path.splitext(img)[0].replace("-", " ").lower()
                flag_images[country_key] = f"images/country-flag/{img}"

    
    raw_country_data = [
        ("+971", "United Arab Emirates"),
        ("+374", "Armenia"),
        ("+61", "Australia"),
        ("+994", "Azerbaijan"),
        ("+880", "Bangladesh"),
        ("+32", "Belgium"),
        ("+359", "Bulgaria"),
        ("+55", "Brazil"),
        ("+1", "Canada"),
        ("+41", "Switzerland"),
        ("+56", "Chile"),
        ("+86", "China"),
        ("+49", "Germany"),
        ("+45", "Denmark"),
        ("+213", "Algeria"),
        ("+372", "Estonia"),
        ("+20", "Egypt"),
        ("+34", "Spain"),
        ("+33", "France"),
        ("+44", "United Kingdom"),
        ("+62", "Indonesia"),
        ("+353", "Ireland"),
        ("+91", "India"),
        ("+98", "Iran"),
        ("+39", "Italy"),
        ("+962", "Jordan"),
        ("+81", "Japan"),
        ("+82", "South Korea"),
        ("+961", "Lebanon"),
        ("+223", "Mali"),
        ("+52", "Mexico"),
        ("+60", "Malaysia"),
        ("+258", "Mozambique"),
        ("+234", "Nigeria"),
        ("+31", "Netherlands"),
        ("+977", "Nepal"),
        ("+64", "New Zealand"),
        ("+63", "Philippines"),
        ("+92", "Pakistan"),
        ("+48", "Poland"),
        ("+7", "Russia"),
        ("+966", "Saudi Arabia"),
        ("+46", "Sweden"),
        ("+963", "Syria"),
        ("+66", "Thailand"),
        ("+90", "Turkey"),
        ("+1", "United States"),
        ("+998", "Uzbekistan"),
        ("+84", "Vietnam"),
        ("+27", "South Africa")
    ]

    # Build final list with flags
    country_codes = []
    for code, name in raw_country_data:
        key = name.lower()
        flag = flag_images.get(key, "images/country-flag/default.jpg")  # fallback
        country_codes.append({"code": code, "flag": flag, "name": name})


    country_codes = sorted(country_codes, key=lambda x: x["name"].lower())

    if requests.method == "POST":
        surname = requests.POST.get('surname').strip()
        firstname = requests.POST.get('firstname').strip()
        other_names = requests.POST.get('others').strip()
        mother_maiden_name = requests.POST.get('maiden').strip()
        gender = requests.POST.get('sex')
        dob = requests.POST.get('dob')
        blood_group = requests.POST.get('blood')
        facial_mark = requests.POST.get('facial')
        glasses = requests.POST.get('glasses')
        height_in_meters = requests.POST.get('height')
        disability = requests.POST.get('disability')
        nin = requests.POST.get('nin').strip()
        phone = requests.POST.get('phone').strip()
        applicant_phone = requests.POST.get('applicant_phone').strip()
        applicant_country_code = requests.POST.get('applicant_country_code', '')
        country_code = requests.POST.get('country_code', '')
        nationality = requests.POST.get('nationality').strip()
        state_of_origin = requests.POST.get('stateoforigin').strip()
        lga = requests.POST.get('lga')
        place_of_birth = requests.POST.get('place')
        occupation = requests.POST.get('profession')
        marital = requests.POST.get('marital')
        duration = requests.POST.get('duration')
        resident_address = requests.POST.get('resident')
        email = requests.POST.get('email').strip()
        programme = requests.POST.get('course_type')  
        profile_picture = requests.FILES.get("profile_picture")
        terms_accepted = requests.POST.get("terms") == "on"

        # print(course_type)

        client_email = Client_DB.objects.filter(email=email).first()
        client_phone = Client_DB.objects.filter(applicant_phone=f"{applicant_country_code} {applicant_phone}").first()
        client_nin = Client_DB.objects.filter(nin=nin).first()

        state_of_origin = State_DB.objects.filter(id=state_of_origin).first().states
        lga = LGA_DB.objects.filter(id=lga).first().lga


        print(state_of_origin, lga, duration)
        # region_instructors = []

        # Validate full name (must contain more than one word)
        if len(surname) < 3:
            error_messages.append("Surname not Accepted, Please Enter your Surname !.")

        elif len(firstname) < 3:
            error_messages.append("First name not Accepted, Please Enter your First name !.")

        elif client_email or client_phone:
            error_messages.append("An Account already exist with this Email or Phone number, check your email to see your Account Credentials or Proceed to Login !")

        elif not email.endswith('@gmail.com'):
            error_messages.append("Please Enter a Valid Email Address")

        elif height_in_meters.count('.') > 1 or not height_in_meters.replace('.', '', 1).isdigit() or float(height_in_meters) <= 0:
            error_messages.append("Height must be a number !.")

        elif len(nin) != 11:
            error_messages.append("NIN is Invalid, NIN must be 11 digit !.")

        elif client_nin:
            error_messages.append("NIN already registered !.")

        elif not terms_accepted:
            error_messages.append("You must agree to the terms and conditions !.")

        # Validate phone number length (between 8 and 16 characters)
        elif not (8 <= len(phone) <= 16):
            error_messages.append("The phone number you entered is Invalid !.")

        # elif not profile_picture:
        #     error_messages.append("Upload a Profile Picture in (.jpg ,.jpeg ,.png) format!.")



        selected_country_flag = []
        applicant_selected_country_flag = []

        for flag in country_codes:
            if flag["code"] == str(country_code):
                selected_country_flag.append(flag["flag"])

        for flag in country_codes:
            if flag["code"] == str(applicant_country_code):
                applicant_selected_country_flag.append(flag["flag"])

        

        # print(selected_country_flag)
        
        if error_messages:
            error_context = {
                "error_messages": error_messages,
                "country_codes": country_codes,
                "currencies": currencies,
                "courses": courses_names,
                "states": states,
                # "transmission_type": transmission_type,
                "form_data": {
                    "surname": surname,
                    "firstname": firstname,
                    "others": other_names,
                    "maiden": mother_maiden_name,
                    "sex": gender,
                    "dob": dob,
                    "blood": blood_group,
                    "facial": facial_mark,
                    "glasses": glasses,
                    "height": height_in_meters,
                    "disability": disability,
                    "nin": nin,
                    "phone": phone,
                    "applicant_phone": applicant_phone,
                    "country_code": country_code,
                    "applicant_country_code": applicant_country_code,
                    "flag": selected_country_flag[0],
                    "applicant_flag": applicant_selected_country_flag[0],
                    "nationality": nationality,
                    "stateoforigin": state_of_origin,
                    "lga": lga,
                    "place": place_of_birth,
                    "profession": occupation,
                    "marital": marital,
                    "duration": duration,
                    "resident": resident_address,
                    "email": email,
                    "course_type": programme,
                    # "password": password,
                    # "confirm_password": confirm_password,                    
                    "terms_accepted": terms_accepted
                },
            }
            return render(requests, "NSD/registration_page.html", error_context)
        


        Client = Client_DB.objects.create(
            surname = surname,
            firstname = firstname,
            other_name = other_names,
            mother_maiden_name = mother_maiden_name,
            gender = gender,
            dob = dob,
            blood_group = blood_group,
            facial_mark = facial_mark,
            glasses = glasses,
            height_in_meters = height_in_meters,
            disability = disability,
            nin = nin,
            next_of_kin_phone = f"{country_code} {phone}",
            applicant_phone = f"{applicant_country_code} {applicant_phone}",
            nationality = nationality,
            state_of_origin = state_of_origin,
            lga_of_origin = lga,
            place_of_birth = place_of_birth,
            occupation = occupation,
            marital_status = marital,
            programme = programme,
            training_duration = duration,
            residential_address = resident_address,
            email = email,
            # password = make_password(password),
            # profile_picture = profile_picture
        )

            # course_type = course_type,
            # transmission = transmission,
            # instructor = instructor,

        Client.save()


        # Store course details and client details in session
        requests.session["email"] = email
        requests.session["course_type"] = programme
        # requests.session["transmission"] = transmission

        requests.session.set_expiry(0) # Set to Whenever the user closes the browser


        # course_id = Driving_Courses.objects.filter(name = course_type).first()
        # course_id = course_id.id

        # Registration Success email
        subject = "Successful Registration - Proceed to Payment"
        message = (
                f"Dear {firstname} {surname},\n\n"
                "Congratulations! Your registration has been successfully received. "
                "To proceed, kindly make the payment for your selected course to confirm your enrollment.\n\n\n"

                "Here are your registration details:\n\n"
                f"📌 Name: {firstname} {surname}\n"
                f"📧 Email: {email}\n"
                f"📞 Phone: {country_code} {phone}\n"
                f"🏡 Address: {resident_address}, {place_of_birth}, {nationality}\n"
                f"💼 Profession: {occupation}\n"
                f"🚗 Programme: {programme}\n"
                f"⌚ Programme Duration: {duration}\n week(s)"
                "✅ Next Steps: Proceed to the payment to complete your registration.\n\n"
                "Thank you for choosing Nevada Driving School. We look forward to training you!\n\n"
                "Best Regards,\nNevada Driving School Team"
            )
        
        send_mail(subject, message, 'chizzichukwudubem@gmail.com', [email], fail_silently=True)

        # Redirect with success message
        # messages.success(requests, "Your Application has been received and will be under review. "
        #                         "If Qualified, an Approval message will be sent to your email. "
        #                         "Check your Mail for more information.")

        # return redirect('instructor-login')

        return redirect('payment')


    context = {
        "country_codes": country_codes,
        "error_messages": error_messages,
        "courses": courses_names,
        "states": states,
        # "transmission_type": transmission_type
        }


    return render(requests, "NSD/registration_page.html", context)





def SWIMMING_REGISTRATION(requests):

    courses = Swimming_Courses.objects.all()


    courses_names = []

    for each_course in courses:
        if each_course.name in courses_names:
            pass
        else:
            courses_names.append(each_course.name)


    error_messages = []

    flag_images = {}

    flag_image_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'country-flag')

    if os.path.exists(flag_image_path):
        for img in os.listdir(flag_image_path):
            if img.lower().endswith(".jpg"):
                # Normalize filename to match country name lookup
                country_key = os.path.splitext(img)[0].replace("-", " ").lower()
                flag_images[country_key] = f"images/country-flag/{img}"

    
    raw_country_data = [
        ("+971", "United Arab Emirates"),
        ("+374", "Armenia"),
        ("+61", "Australia"),
        ("+994", "Azerbaijan"),
        ("+880", "Bangladesh"),
        ("+32", "Belgium"),
        ("+359", "Bulgaria"),
        ("+55", "Brazil"),
        ("+1", "Canada"),
        ("+41", "Switzerland"),
        ("+56", "Chile"),
        ("+86", "China"),
        ("+49", "Germany"),
        ("+45", "Denmark"),
        ("+213", "Algeria"),
        ("+372", "Estonia"),
        ("+20", "Egypt"),
        ("+34", "Spain"),
        ("+33", "France"),
        ("+44", "United Kingdom"),
        ("+62", "Indonesia"),
        ("+353", "Ireland"),
        ("+91", "India"),
        ("+98", "Iran"),
        ("+39", "Italy"),
        ("+962", "Jordan"),
        ("+81", "Japan"),
        ("+82", "South Korea"),
        ("+961", "Lebanon"),
        ("+223", "Mali"),
        ("+52", "Mexico"),
        ("+60", "Malaysia"),
        ("+258", "Mozambique"),
        ("+234", "Nigeria"),
        ("+31", "Netherlands"),
        ("+977", "Nepal"),
        ("+64", "New Zealand"),
        ("+63", "Philippines"),
        ("+92", "Pakistan"),
        ("+48", "Poland"),
        ("+7", "Russia"),
        ("+966", "Saudi Arabia"),
        ("+46", "Sweden"),
        ("+963", "Syria"),
        ("+66", "Thailand"),
        ("+90", "Turkey"),
        ("+1", "United States"),
        ("+998", "Uzbekistan"),
        ("+84", "Vietnam"),
        ("+27", "South Africa")
    ]

    # Build final list with flags
    country_codes = []
    for code, name in raw_country_data:
        key = name.lower()
        flag = flag_images.get(key, "images/country-flag/default.jpg")  # fallback
        country_codes.append({"code": code, "flag": flag, "name": name})


    country_codes = sorted(country_codes, key=lambda x: x["name"].lower())



    if requests.method == "POST":
        surname = requests.POST.get('surname').strip()
        firstname = requests.POST.get('firstname').strip()
        other_names = requests.POST.get('others').strip()
        dob = requests.POST.get('dob')
        phone = requests.POST.get('phone').strip()
        applicant_phone = requests.POST.get('applicant_phone').strip()
        applicant_country_code = requests.POST.get('applicant_country_code', '')
        country_code = requests.POST.get('country_code', '')
        gender = requests.POST.get('sex')
        health = requests.POST.get('health')
        experience = requests.POST.get('experience')
        address = requests.POST.get('resident')
        course_type = requests.POST.get('course_type')
        duration = requests.POST.get('duration')
        profile_picture = requests.FILES.get("profile_picture")
        terms_accepted = requests.POST.get("terms") == "on"

        # print(course_type)

        # client_email = Client_DB.objects.filter(email=email).first()
        client_phone = Swimming_Client_DB.objects.filter(applicant_phone=f"{applicant_country_code} {applicant_phone}").first()
        # client_nin = Client_DB.objects.filter(nin=nin).first()

        # state_of_origin = State_DB.objects.filter(id=state_of_origin).first().states
        # lga = LGA_DB.objects.filter(id=lga).first().lga


        # print(state_of_origin, lga, duration)
        # region_instructors = []

        # Validate full name (must contain more than one word)
        if len(surname) < 3:
            error_messages.append("Surname not Accepted, Please Enter your Surname !.")

        elif len(firstname) < 3:
            error_messages.append("First name not Accepted, Please Enter your First name !.")

        elif client_phone:
            error_messages.append("An Account already exist with this Email or Phone number, check your email to see your Account Credentials or Proceed to Login !")


        elif not terms_accepted:
            error_messages.append("You must agree to the terms and conditions !.")

        # Validate phone number length (between 8 and 16 characters)
        elif not (8 <= len(phone) <= 16):
            error_messages.append("The phone number you entered is Invalid !.")

        # elif not profile_picture:
        #     error_messages.append("Upload a Profile Picture in (.jpg ,.jpeg ,.png) format!.")


        selected_country_flag = []
        applicant_selected_country_flag = []

        for flag in country_codes:
            if flag["code"] == str(country_code):
                selected_country_flag.append(flag["flag"])

        for flag in country_codes:
            if flag["code"] == str(applicant_country_code):
                applicant_selected_country_flag.append(flag["flag"])

        

        # print(selected_country_flag)
        
        if error_messages:
            error_context = {
                "error_messages": error_messages,
                "country_codes": country_codes,
                # "currencies": currencies,
                # "courses": courses_names,
                # "states": states,
                # "transmission_type": transmission_type,
                "form_data": {
                    "surname": surname,
                    "firstname": firstname,
                    "others": other_names,
                    "sex": gender,
                    "dob": dob,
                    "phone": phone,
                    "applicant_phone": applicant_phone,
                    "country_code": country_code,
                    "applicant_country_code": applicant_country_code,
                    "flag": selected_country_flag[0],
                    "applicant_flag": applicant_selected_country_flag[0],
                    "health": health,
                    "experience": experience,
                    "address": address,
                    "course_type": course_type,
                    "duration": duration,                    
                    "terms_accepted": terms_accepted
                },
            }
            return render(requests, "NSD/swimming_registration_page.html", error_context)


        Client = Swimming_Client_DB.objects.create(
            surname = surname,
            firstname = firstname,
            other_name = other_names,
            gender = gender,
            dob = dob,
            next_of_kin_phone = f"{country_code} {phone}",
            applicant_phone = f"{applicant_country_code} {applicant_phone}",
            previous_experience = experience,
            health_status = health,
            residential_address = address,
            programme = course_type,
            training_duration = duration
            # profile_picture = profile_picture
        )


        Client.save()


        # Store course details and client details in session
        requests.session["applicant_phone"] = f"{applicant_country_code} {applicant_phone}"
        requests.session["course_type"] = course_type

        requests.session.set_expiry(0) # Set to Whenever the user closes the browser

        # course_id = Driving_Courses.objects.filter(name = course_type).first()
        # course_id = course_id.id


        return redirect('swimming-payment')


    context = {
        "country_codes": country_codes,
        "error_messages": error_messages,
        "courses": courses_names,
        }


    return render(requests, "NSD/swimming_registration_page.html", context)




def PAYMENT(requests):
    context = {
        "surname": "",
        "firstname": "",
        "email": "",
        "phone": "",
        "address": "",
        "city": "",
        "country": "",
        # "profession": "",
        "course_type": "",
        "duration": "",
        # "transmission": "",
        # "choose_instructor": "",
        "course_price": "",
        # "registeration_details": ""
    }


    # Gotten from the Registration
    email = requests.session.get("email")
    course_type = requests.session.get("course_type")


    if email:
        client_details = Client_DB.objects.filter(email=email).first()
        # registeration_details = client_details.registrations.all().first()

        course_details = Driving_Courses.objects.filter(name = course_type).first()

        if client_details:
            context["surname"] = client_details.surname
            context["firstname"] = client_details.firstname
            # context["other_names"] = client_details.other_name
            context["email"] = client_details.email
            context["phone"] = client_details.applicant_phone
            # context["nin"] = client_details.nin
            context["address"] = client_details.residential_address
            context["city"] = client_details.place_of_birth
            context["country"] = client_details.nationality
            context["course_type"] = course_details.name
            context["duration"] = course_details.duration
            context["course_price"] = course_details.price # course_details.price


            if requests.method == "POST" and requests.headers.get('Content-Type') == 'application/json':
                payment_data = json.loads(requests.body)

                names = payment_data.get("names")
                email = payment_data.get("email")
                phone = payment_data.get("phone")
                address = payment_data.get("address")
                location = payment_data.get("location_detail")
                course = payment_data.get("course_type")
                duration = payment_data.get("duration")
                price = payment_data.get("price")

                # print(names, email, phone, address, price)


                client = Client_DB.objects.filter(email=email).first()
                # print(client)

                if client:

                    return JsonResponse({
                        'success': True,
                    })
                
                        
                
                else:
                    return JsonResponse({'success': False, 'error': 'Client not found'})


    return render(requests, "NSD/payment_page.html", context)




def SWIMMING_PAYMENT(requests):

    context = {
        "surname": "",
        "firstname": "",
        "other_names": "",
        "gender": "",
        "phone": "",
        "address": "",
        "health_status": "",
        "programme": "",
        "duration": ""
        # "city": "",
        # "country": "",
        # "profession": "",
        # "course_type": "",
        # "transmission": "",
        # "choose_instructor": "",
        # "course_price": "",
        # "registeration_details": ""
    }


    # Gotten from the Registration
    applicant_phone = requests.session.get("applicant_phone")
    course_type = requests.session.get("course_type")


    if applicant_phone:
        client_details = Swimming_Client_DB.objects.filter(applicant_phone=applicant_phone).first()
        # registeration_details = client_details.registrations.all().first()

        course_details = Swimming_Courses.objects.filter(name = course_type).first()

        if client_details:
            context["surname"] = client_details.surname
            context["firstname"] = client_details.firstname
            context["other_names"] = client_details.other_name
            context["gender"] = client_details.gender
            context["phone"] = client_details.applicant_phone
            # context["nin"] = client_details.nin
            context["address"] = client_details.residential_address
            context["health_status"] = client_details.health_status
            context["programme"] = client_details.programme,
            context["duration"] = client_details.training_duration
            context["course_price"] = course_details.price

            # context["city"] = client_details.place_of_birth
            # context["country"] = client_details.nationality
            # context["course_type"] = course_details.name
            # context["duration"] = course_details.duration
            # context["course_price"] = course_details.price # course_details.price


            if requests.method == "POST" and requests.headers.get('Content-Type') == 'application/json':
                payment_data = json.loads(requests.body)

                surname = payment_data.get("surname")
                firstname = payment_data.get("firstname")
                other_name = payment_data.get("other_name")
                gender = payment_data.get("gender")
                phone = payment_data.get("phone")
                address = payment_data.get("address")
                # duration = payment_data.get("duration")
                # price = payment_data.get("price")

                # print(names, email, phone, address, price)


                client = Swimming_Client_DB.objects.filter(applicant_phone=applicant_phone).first()
                # print(client)

                if client:

                    return JsonResponse({
                        'success': True,
                    })
                
                else:
                    return JsonResponse({'success': False, 'error': 'Client not found'})


    return render(requests, "NSD/swimming_payment_page.html", context)




def CONTACT_US(requests):

    if requests.method == "POST":
        try:
            data = json.loads(requests.body)  # Parse JSON data

            name = data.get("name", "").strip()
            email = data.get("email", "").strip()
            message = data.get("message", "").strip()

            print(name)
            print(email)
            print(message)

            contact_messages = Contact_Messages_DB.objects.filter(email=email.lower()).first()

            if contact_messages:
                contact_messages.name = name.lower()
                contact_messages.email = email.lower()
                contact_messages.message = message.lower()
                contact_messages.save()
                created = False

            else:
                contact_messages = Contact_Messages_DB.objects.create(
                    name = name.lower(),
                    email = email.lower(),
                    message = message.lower(),
                )
                created = True

            
            # Send Confirmation Email
            subject = "Message Received - Nevada Driving School"
            message_body = f"Dear {name.split()[0]},\n\nThank you for reaching out to Nevada Driving School. We have received your message and will get back to you as soon as possible.\n\nHere’s a summary of your inquiry:\n\n📌 **Name:** {name}\n📧 **Email:** {email}\n📝 **Message:** {message}\n\nOur team will review your message and respond shortly. If your inquiry is urgent, you can reach us directly at 📞 +234 9126425150.\n\nBest regards,\nNevada Driving School Team"
            send_mail(
                subject, 
                message_body, 
                "chizzichukwudubem@gmail.com",  # Replace with your sender email
                [email], 
                fail_silently=False
            )

            return JsonResponse({"message": "Message Sent Successfully"}, status=200)
        
        except:
            return JsonResponse({"error": "An Error occurred while sending your message, Try again!"}, status=500)


    context = {}

    return render(requests, "NSD/contact_page.html", context)




def TERMS_CONDITION(requests):

    context = {}

    return render(requests, "NSD/terms_condition.html", context)