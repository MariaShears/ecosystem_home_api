import os
from functools import wraps
from flask import request 
from pprint import pprint

from app import app
# from app.recording import Recording

api_prefix = '/ecosystem-home/v1'

# @app.route(f'{api_prefix}/hello', methods=['GET'])
# def handle_get_hello():
#     return {
#         'message': 'hello world'
#     }

# @app.route(f'{api_prefix}/user/<user_id>', methods=['GET'])
# def handle_get_user_id(user_id):
#     """get special user id"""
#     return {
#         'user_id': f'xxx_{user_id}'
#     }

# @app.route(f'{api_prefix}/add10/<int:b>', methods=['GET'])
# def handle_get_add_10(b):
#     """add 10 to a number"""
#     return {
#         'sum': b + 10
#     }


# @app.route(f'{api_prefix}/add', methods=['POST'])
# def handle_post_add():
#     """add two numbers a and b"""
#     data = request.get_json()
#     pprint(data)
#     sum = data['a'] + data['b']
#     return {
#         'sum': sum
#     }

# @app.route(f'{api_prefix}/recording/<recording_id>', methods=['GET'])
# def handle_get_recording(recording_id):
#     """gets a new recording or creates a new one"""
#     recording = Recording(recording_id)
#     return recording.dump()

@app.route(f'{api_prefix}/record', methods=['POST'])
def handle_record_post():
    """records sensor data from particle cloud"""
    data = request.get_json()
    pprint(data)
    return ("thanks", 200)