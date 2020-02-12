from zc_table import db, Area_info
from zip_dict import data

def make_table():
    for d in data:
        zc_info = Area_info(
        city = zipcode_data["city"],
        state = zipcode_data["state"],
        population = zipcode_data["population"],
        longitude = zipcode_data["longitude"],
        latitude = zipcode_data["latitude"],
        zipcode = zipcode_data["zipcode"]
        )
        db.session.add(zc_info)
        db.session.commit()
        return "Successfully added"