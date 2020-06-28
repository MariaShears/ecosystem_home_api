import os
from functools import wraps
from flask import request 
from pprint import pprint

from app import app
from app.recording import save_recording

api_prefix = '/ecosystem-home/v1'

@app.route(f'{api_prefix}/record', methods=['POST'])
def handle_record_post():
    """records sensor data from particle cloud"""
    data = request.get_json()
    save_recording(data)
    return ("thanks", 200)