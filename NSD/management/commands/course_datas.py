from django.core.management.base import BaseCommand
from django.core.files import File
from NSD.models import Driving_Courses
import json
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Populate the Driving Course database with Different Course Details'

    def handle(self, *args, **kwargs):
        
        data_path = os.path.join(settings.BASE_DIR / 'NSD' / 'management' / 'commands', 'courses.json')

        if not os.path.exists(data_path):
            self.stdout.write(self.style.ERROR("Course Data not Found!"))
            return
        
        with open(data_path, 'r+') as file:
            course_data = json.load(file)

        for course in course_data:
            course_img_path = os.path.join(settings.STATICFILES_DIRS[0], "images", "courses", course["image"])

            description_content = "\n".join(course['description'])

            if os.path.exists(course_img_path):
                with open(course_img_path, "rb") as image_file:
                    course_image = File(image_file)

                    driving_course, created = Driving_Courses.objects.get_or_create(
                        name = course["name"],
                        description = description_content,
                        duration = course["duration"],
                        type = course["type"],
                        price = course["price"]
                    )
                    driving_course.image.save(course["image"], course_image, save=True)
                    self.stdout.write(self.style.SUCCESS(f"Added {course['name']} to the Driving Course Database"))
            else:
                self.stdout.write(self.style.WARNING(f"Can't Find Image: {course['image']}"))
