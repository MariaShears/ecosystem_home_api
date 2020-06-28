import json
# from pprint import pprint
from mongoengine import *

def parse_raw_recording(raw_record):
    return {
        'device_id': 'xxxx'
    }
    #self._recording = _Recording(external_id=external_id)


class _Recording(Document):
    device_id = StringField(required=True)
    temp = FloatField(required=True)
    humidity = FloatField(required=True)

# class Recording():
#     def __init__(self, device_id, temp, humidity):
        # recordings = _Recording.objects(external_id=external_id)
        # if len(recordings) > 0:
        #     self._recording = recordings[0]
        # else:
        #     self._recording = _Recording(external_id=external_id)
        #     self._recording.save()

    # def update(self, fields):
    #     """given a list of tups update the keys on the user"""
    #     for field in fields:
    #         self._user[field] = fields[field]
    #     self._user.save()

    # def dump(self):
    #     """Return a object that can be json dumped and is clean of _id"""
    #     json_recording = self._recording.to_json()
    #     recording = json.loads(json_recording)
    #     del recording["_id"]
    #     return recording
