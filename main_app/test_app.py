import app
from redis import Redis
import json
from history import get_job_info
import pytest

r = Redis()

def reset_redis():
    r.delete('test_gutenberg_history')
    r.delete('test_xerox_history')
    r.delete('test_gutenberg_nozzle_1_temps')
    r.delete('test_gutenberg_nozzle_2_temps')
    r.delete('test_xerox_nozzle_1_temps')
    r.delete('test_xerox_nozzle_2_temps')


def test_app_returns_print_job_when_gutenberg_is_printing():
    job = {
        "datetime_cleaned": "2020-10-25T18:30:41",
        "datetime_finished": "2020-10-25T18:29:13",
        "datetime_started": "2020-10-25T18:22:39",
        "name": "UM3E_BAT_Cookie_cutter_rgproduct_Heidi",
        "reprint_original_uuid": None,
        "result": "Aborted",
        "source": "WEB_API/Unknown/Cura connect",
        "time_elapsed": 25.502346,
        "time_estimated": 0,
        "time_total": 0,
        "uuid": "3178a7c4-87e2-481d-8aa7-5a2d074d0e43"
    }

    app_ = app.create_app("test_", lambda url: 'printing')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = get_job_info(job)
    r.rpush('test_gutenberg_history', json.dumps(expected))
    r.rpush('test_gutenberg_nozzle_1_temps', 225.0)
    r.rpush('test_gutenberg_nozzle_2_temps', 220.0)
    expected['nozzle_1'] = 225.0
    expected['nozzle_2'] = 220.0
    
    response = client.get('/current_job?printer=gutenberg')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_print_job_when_xerox_is_printing():
    job = {
        "datetime_cleaned": "2020-10-25T18:30:41",
        "datetime_finished": "2020-10-25T18:29:13",
        "datetime_started": "2020-10-25T18:22:39",
        "name": "UM3E_BAT_Cookie_cutter_rgproduct_Heidi",
        "reprint_original_uuid": None,
        "result": "Aborted",
        "source": "WEB_API/Unknown/Cura connect",
        "time_elapsed": 25.502346,
        "time_estimated": 0,
        "time_total": 0,
        "uuid": "3178a7c4-87e2-481d-8aa7-5a2d074d0e43"
    }

    app_ = app.create_app("test_", lambda url: 'printing')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = get_job_info(job)
    r.rpush('test_xerox_history', json.dumps(expected))
    r.rpush('test_xerox_nozzle_1_temps', 225.0)
    r.rpush('test_xerox_nozzle_2_temps', 220.0)
    expected['nozzle_1'] = 225.0
    expected['nozzle_2'] = 220.0
    
    response = client.get('/current_job?printer=xerox')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_message_when_gutenberg_not_printing():
    app_ = app.create_app("test_", lambda url: 'idle')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = {'gutenberg': 'gutenberg is not currently printing'}
    response = client.get('/current_job?printer=gutenberg')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_message_when_xerox_not_printing():
    app_ = app.create_app("test_", lambda url: 'idle')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = {'xerox': 'xerox is not currently printing'}
    response = client.get('/current_job?printer=xerox')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_gutenberg_and_xerox_print_jobs_formatted_correctly():
    xerox_job = {
        "datetime_cleaned": "2020-10-26T22:59:30",
        "datetime_finished": "2020-10-26T22:58:36",
        "datetime_started": "2020-10-26T22:47:06",
        "name": "UM3E_star_guy_bottom",
        "reprint_original_uuid": "dd30fe04-dea8-4d7e-89bc-4b49f83284e9",
        "result": "Printing",
        "source": "USB",
        "time_elapsed": 0,
        "time_estimated": 0,
        "time_total": 0,
        "uuid": "a8f8e030-b24b-490a-b145-ce5d900ad768"
    }

    app_ = app.create_app("test_", lambda url: 'idle' if url == app.gutenberg_url else 'printing')
    app_.config['TESTING'] = True
    client = app_.test_client()

    gutenberg_expected = {'gutenberg': 'gutenberg is not currently printing'}
    xerox_expected = get_job_info(xerox_job)
    r.rpush('test_xerox_history', json.dumps(xerox_expected))
    r.rpush('test_xerox_nozzle_1_temps', 225.0)
    r.rpush('test_xerox_nozzle_2_temps', 220.0)
    xerox_expected['nozzle_1'] = 225.0
    xerox_expected['nozzle_2'] = 220.0

    expected = {'gutenberg_current_job': gutenberg_expected, 'xerox_current_job': xerox_expected}
    response = client.get('/current_job')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_empty_temp_list_when_no_gutenberg_nozzle_temps_recorded():
    app_ = app.create_app("test_", lambda url: 'idle')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = {"gutenberg_nozzle_temps": {"nozzle_1_temps": [], "nozzle_2_temps": []}}
    response = client.get('/nozzle_temps?printer=gutenberg')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_empty_temp_list_when_no_xerox_nozzle_temps_recorded():
    app_ = app.create_app("test_", lambda url: 'idle')
    app_.config['TESTING'] = True
    client = app_.test_client()

    expected = {"xerox_nozzle_temps": {"nozzle_1_temps": [], "nozzle_2_temps": []}}
    response = client.get('/nozzle_temps?printer=xerox')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_valid_temp_list_from_gutenberg_nozzle_temps_recorded():
    app_ = app.create_app("test_", lambda url: 'idle')
    app_.config['TESTING'] = True
    client = app_.test_client()

    for temp in (223.5, 222.1, 224.3):
        r.rpush('test_gutenberg_nozzle_1_temps', temp)
    for temp in (221.7, 220.7, 224.9):
        r.rpush('test_gutenberg_nozzle_2_temps', temp)

    expected = {"gutenberg_nozzle_temps": {"nozzle_1_temps": [223.5, 222.1, 224.3], "nozzle_2_temps": [221.7, 220.7, 224.9]}}
    response = client.get('/nozzle_temps?printer=gutenberg')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_valid_temp_list_from_xerox_nozzle_temps_recorded():
    app_ = app.create_app("test_", lambda url: 'printing')
    app_.config['TESTING'] = True
    client = app_.test_client()

    for temp in (220.1, 220.9, 222.2):
        r.rpush('test_xerox_nozzle_1_temps', temp)
    for temp in (224.9, 220.4, 223.3):
        r.rpush('test_xerox_nozzle_2_temps', temp)

    expected = {"xerox_nozzle_temps": {"nozzle_1_temps": [220.1, 220.9, 222.2], "nozzle_2_temps": [224.9, 220.4, 223.3]}}
    response = client.get('/nozzle_temps?printer=xerox')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()

def test_app_returns_valid_temp_lists_from_gutenberg_and_xerox():
    app_ = app.create_app("test_", lambda url: 'printing')
    app_.config['TESTING'] = True
    client = app_.test_client()

    for temp in (223.5, 222.1, 224.3):
        r.rpush('test_gutenberg_nozzle_1_temps', temp)
    for temp in (221.7, 220.7, 224.9):
        r.rpush('test_gutenberg_nozzle_2_temps', temp)
    for temp in (220.1, 220.9, 222.2):
        r.rpush('test_xerox_nozzle_1_temps', temp)
    for temp in (224.9, 220.4, 223.3):
        r.rpush('test_xerox_nozzle_2_temps', temp)

    expected = {"gutenberg_nozzle_temps": {"nozzle_1_temps": [223.5, 222.1, 224.3], "nozzle_2_temps": [221.7, 220.7, 224.9]},
        "xerox_nozzle_temps": {"nozzle_1_temps": [220.1, 220.9, 222.2], "nozzle_2_temps": [224.9, 220.4, 223.3]}}
    response = client.get('/nozzle_temps')
    assert response.status_code == 200
    assert response.get_json() == expected
    reset_redis()