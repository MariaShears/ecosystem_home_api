import json
# from pprint import pprint

from mongoengine import *

class _Recording(Document):
    external_id = StringField(required=True)
    age = IntField()
    size_x = IntField()
    size_y = IntField()

class Recording():
    def __init__(self, external_id):
        recordings = _Recording.objects(external_id=external_id)
        if len(recordings) > 0:
            self._recording = recordings[0]
        else:
            self._recording = _Recording(external_id=external_id)
            self._recording.save()

    # def update(self, fields):
    #     """given a list of tups update the keys on the user"""
    #     for field in fields:
    #         self._user[field] = fields[field]
    #     self._user.save()

    def dump(self):
        """Return a object that can be json dumped and is clean of _id"""
        json_recording = self._recording.to_json()
        recording = json.loads(json_recording)
        del recording["_id"]
        return recording
