# Commands to create this file 

"""
Make sure you are in the app directory first of all

mkdir -p management/commands

touch management/__init__.py
touch management/commands/__init__.py
OR
New-Item -ItemType File -Path management\__init__.py
New-Item -ItemType File -Path management\commands\__init__.py


New-Item -ItemType File -Path management\commands\populate_states.py

"""

# Vote/management/commands/populate_states.py

from django.core.management.base import BaseCommand
from NSD.models import State_DB, LGA_DB
import json
import os

class Command(BaseCommand):
    help = 'Populate the database with states and their capitals'

    def handle(self, *args, **kwargs):
        States_Capital = {
            1: ["Abia", "Umuahia"],
            2: ["Adamawa", "Yola"],
            3: ["Akwa Ibom", "Uyo"],
            4: ["Anambra", "Awka"],
            5: ["Bauchi", "Bauchi"],
            6: ["Bayelsa", "Yenagoa"],
            7: ["Benue", "Makurdi"],
            8: ["Borno", "Maiduguri"],
            9: ["Cross River", "Calabar"],
            10: ["Delta", "Asaba"],
            11: ["Ebonyi", "Abakaliki"],
            12: ["Edo", "Benin City"],
            13: ["Ekiti", "Ekiti"],
            14: ["Enugu", "Enugu"],
            15: ["Gombe", "Gombe"],
            16: ["Imo", "Owerri"],
            17: ["Jigawa", "Dutse"],
            18: ["Kaduna", "Kaduna"],
            19: ["Kano", "Kano"],
            20: ["Katsina", "Katsina"],
            21: ["Kebbi", "Birnin Kebbi"],
            22: ["Kogi", "Lokoja"],
            23: ["Kwara", "Ilorin"],
            24: ["Lagos", "Ikeja"],
            25: ["Nasarawa", "Lafia"],
            26: ["Niger", "Minna"],
            27: ["Ogun", "Abeokuta"],
            28: ["Ondo", "Akure"],
            29: ["Osun", "Oshogbo"],
            30: ["Oyo", "Ibadan"],
            31: ["Plateau", "Jos"],
            32: ["Rivers", "Port Harcourt"],
            33: ["Sokoto", "Sokoto"],
            34: ["Taraba", "Jalingo"],
            35: ["Yobe", "Damaturu"],
            36: ["Zamfara", "Gusau"],
            37: ["FCT", "Abuja"],
        }

        # try:
        #     for id, states in States_Capital.items():
        #         State_DB.objects.create(id=id, states=states[0], capitals=states[1])
        # except Exception as e:
        #     print(e)

        # self.stdout.write(self.style.SUCCESS('Successfully populated states and capitals'))





# After you run the command in the terminal  -->>  python manage.py populate_states






class Command(BaseCommand):
    help = 'Populate the database with states and their LGAs'

    def handle(self, *args, **kwargs):
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_dir, 'states_and_lgas.json')

        # with open('../commands/states_and_lgas.json', 'r') as file:
        with open(data_path, 'r') as file:
            lga_data = json.load(file)

        for item in lga_data:
            state_name = item['state']
            lgas = item['lgas']
            try:
                state = State_DB.objects.get(states__iexact=state_name)  # Use case-insensitive lookup
                for lga_name in lgas:
                    LGA_DB.objects.get_or_create(lga=lga_name, state=state)
                    self.stdout.write(self.style.SUCCESS(f'Successfully created LGA: {lga_name} for state: {state_name}'))
            except State_DB.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'State "{state_name}" does not exist in the database.'))

        self.stdout.write(self.style.SUCCESS('Database populated with states and LGAs.'))