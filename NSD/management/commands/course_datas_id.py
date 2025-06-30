from django.core.management.base import BaseCommand
from django.core.files import File
from NSD.models import Driving_Courses, Driving_Course_Identity_DB
import json
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Populate the Database with the Course with their Respective identity IDs'

    def handle(self, *args, **kwargs):
        
        data_path = os.path.join(settings.BASE_DIR / 'NSD' / 'management' / 'commands', 'course_datas_id.json')

        if not os.path.exists(data_path):
            self.stdout.write(self.style.ERROR("Course Data not Found!"))
            return
        
        with open(data_path, 'r+') as file:
            course_data = json.load(file)

            for each_course in course_data:

                course_name = each_course["name"]
                course_details = Driving_Courses.objects.filter(name = course_name).first()

                if course_details:
                    course_id_no = each_course["course_id"]
                    course_identity = Driving_Course_Identity_DB.objects.filter(course_identity_number = course_id_no).first()

                    if not course_identity:
                        save_course_ids = Driving_Course_Identity_DB.objects.create(
                            course = course_details,
                            course_identity_number = each_course["course_id"],
                            course_name = each_course["name"],
                            type = each_course["type"],
                            couse_price = each_course["price"]
                        )

                        save_course_ids.save()

                        self.stdout.write(self.style.SUCCESS(f"Successfully saved {each_course['name']} - {each_course['course_id']}"))

                    else:
                        self.stdout.write(self.style.ERROR(f"Couldn't save. {each_course['name']} - {each_course['course_id']} already exists"))
                        return
                    
                else:
                    self.stdout.write(self.style.ERROR(f"{each_course['name']} not found in the Driving Course Database."))
                    return