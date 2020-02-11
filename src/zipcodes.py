import requests
import json 

data = requests.get('https://assets.breatheco.de/apis/fake/zips.php').json()

def mk_dict():
  new_dict = {}
  for d in data:
    new_dict[d['_id']] = {
    'city': d['city'],
    'state': d['state'],
    'longitude': d['loc'][0],
    'latitude': d['loc'][1],
    'population': d['pop']
  }
  return new_dict


zipcode_data = mk_dict()
with open('zipcodes.json', 'w') as jfile:
    json.dump(zipcode_data, jfile)

