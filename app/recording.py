import json
from pprint import pprint
from mongoengine import *


def _parse_raw_recording(raw_record):
    data_parts = raw_record["data"].split(',')
    return {
        'device_id': raw_record["coreid"],
        'temp': round(float(data_parts[0]), 2),
        'humidity': round(float(data_parts[1]), 2)
    }


def save_recording(raw_record):
    parsed_data = _parse_raw_recording(raw_record)
    new_record_db_object = _Recording(
        device_id=parsed_data['device_id'], 
        # temp=parsed_data['temp'], 
        # humidity=parsed_data['humidity']
    )
    pprint(new_record_db_object)
    new_record_db_object.save()

class _Recording(Document):
    device_id = StringField(required=True)
    # temp = FloatField(required=True)
    # humidity = FloatField(required=True)
