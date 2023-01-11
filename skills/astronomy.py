from pyowm import OWM
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import json
from slugify import slugify
import os
import time

class Astronomy():
    BASE_URL_PERIODIC_ORBITS = "https://ssd-api.jpl.nasa.gov/sbwobs.api?"

    def __init__(self):
        geolocator = Nominatim(user_agent="MoBot")
        location = geolocator.geocode("35 Impasse de la Gare, 40170 Bias")
        self.date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.location = location

    @property
    def check_if_need_update(self):
        if not os.path.exists('observation_possibility.json'):
            return True
        current_time = datetime.now().strftime("%Y-%m-%d")
        ti_m = os.path.getmtime('observation_possibility.json')
        m_ti = time.ctime(ti_m)
        t_obj = time.strptime(m_ti)
        T_stamp = time.strftime("%Y-%m-%d", t_obj)
        return current_time != T_stamp
    
    @property
    def update_objects_observation(self):
        # Check if tmp folder exists else create it
        if not self.check_if_need_update:
            return 'Votre catalogue de donnée est à jour.'
        print('Updating objects observation possibility...')
        if not os.path.exists('tmp'):
            os.makedirs('tmp')

        url = f'{self.BASE_URL_PERIODIC_ORBITS}lon={self.location.longitude}&lat={self.location.latitude}&alt={self.location.altitude}&obs-time={self.date}&elev-min=15&time-min=5&optical=true&fmt-ra-dec=true&mag-required=true&output-sort=name&output-sort-r=false&www=1'
        response = requests.get(url)
        response_json = response.json()
        rep = json.dumps(response_json, indent=4)
        with open('tmp/data.json', 'w') as f:
            f.write(str(rep))

        with open('tmp/data.json', 'r') as f:
            data = f.read()
            data = json.loads(data)
            get_fields = [slugify(i) for i in data['fields']]
            for i in data['data']:
                i.pop(1)
            new_data = [dict(zip(get_fields, i)) for i in data['data']]
            new_data = json.dumps(new_data, indent=4)

        with open('observation_possibility.json', 'w') as f:
            f.write(str(new_data))

        if response.status_code == 200:
            return 'Mise à jour effectuée avec succès'
        else:
            return 'Erreur lors de la mise à jour'
