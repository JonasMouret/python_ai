from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import json
from slugify import slugify

# BASE_URL_PERIODIC_ORBITS = "https://ssd-api.jpl.nasa.gov/sbwobs.api?"

# geolocator = Nominatim(user_agent="MoBot")
# location = geolocator.geocode("35 Impasse de la Gare, 40170 Bias")
# date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
# url = f'{BASE_URL_PERIODIC_ORBITS}lon={location.longitude}&lat={location.latitude}&alt={location.altitude}&obs-time={date}&elev-min=15&time-min=5&optical=true&fmt-ra-dec=true&mag-required=true&maxoutput=10&output-sort=name&output-sort-r=false&www=1'
# response = requests.get(url)
# response_json = response.json()
# print(response.status_code)


# def get_objects_observation():
#     BASE_URL_PERIODIC_ORBITS = "https://ssd-api.jpl.nasa.gov/sbwobs.api?"

#     geolocator = Nominatim(user_agent="MoBot")
#     location = geolocator.geocode("35 Impasse de la Gare, 40170 Bias")
#     date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
#     url = f'{BASE_URL_PERIODIC_ORBITS}lon={location.longitude}&lat={location.latitude}&alt={location.altitude}&obs-time={date}&elev-min=15&time-min=5&optical=true&fmt-ra-dec=true&mag-required=true&maxoutput=100&output-sort=name&output-sort-r=false&www=1'
#     response = requests.get(url).json()
#     rep = json.dumps(response, indent=4)
#     with open('data.json', 'w') as f:
#         f.write(str(rep))

#     with open('data.json', 'r') as f:
#         data = f.read()
#         data = json.loads(data)
#         get_fields = [slugify(i) for i in data['fields']]
#         for i in data['data']:
#             i.pop(1)
#         new_data = [dict(zip(get_fields, i)) for i in data['data']]
#         new_data = json.dumps(new_data, indent=4)

#     with open('clean_data.json', 'w') as f:
#         f.write(str(new_data))

#     return new_data

# get_objects_observation()

# def check():
#     data = {
#         "hello": "world",
#         "foo": "bar"
#     }
#     with open('tmp/data.json', 'w') as f:
#         f.write(str(data))

# check()



    
# import os
# import time
 
# if os.path.exists('observation_possibility.json'):
#     current_time = datetime.now().strftime("%Y-%m-%d")
#     ti_m = os.path.getmtime('observation_possibility.json')
#     m_ti = time.ctime(ti_m)
#     t_obj = time.strptime(m_ti)
#     T_stamp = time.strftime("%Y-%m-%d", t_obj)
#     print(T_stamp < current_time)
    
#     print(f"The file located at observation_possibility.json  was last modified at {T_stamp}")

with open('test.json', 'r') as f:
    data = f.read()
    data = json.loads(data)
    for i in data:
        if 'ceres' in i['full-name'].lower():
            print(i['rise-time'])