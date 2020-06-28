from app.recording import parse_raw_recording

def test_parse_raw_recording():
    recording = parse_raw_recording({
        'coreid': 'e00fce681196db3ccb8a7faf',
        'data': '23.900000,73.800003',
        'event': 'temp_c_and_humidity',
        'published_at': '2020-06-28T19:27:03.620Z'
    })
    expected_output = {
        'device_id': 'e00fce681196db3ccb8a7faf',
        'temp': 23.9,
        'humidity': 73.8
    }
    assert recording == expected_output