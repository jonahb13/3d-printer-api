from redis import Redis
from app import create_app
import pytest
import json


r = Redis()

def test_server_returns_single_job_in_history():
    r.rpush('history', json.dumps({
        "datetime_finished": "2020-11-10T20:21:32", 
        "datetime_started": "2020-11-10T20:00:28", 
        "name": "UM3E_LightClipLowerFlanges", 
        "result": "Finished"
    }))

    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('/history')
    expected = {
        "history": [
            {
                "datetime_finished": "2020-11-10T20:21:32", 
                "datetime_started": "2020-11-10T20:00:28", 
                "name": "UM3E_LightClipLowerFlanges", 
                "result": "Finished"
            }
        ]
    }

    assert response.status_code == 200
    assert response.get_json() == expected


def test_server_returns_updated_history_when_another_print_job_is_added():
    r.rpush('history', json.dumps({
        "datetime_finished": "2020-10-29T22:44:11", 
        "datetime_started": "2020-10-29T22:39:57", 
        "name": "UM3E_cube", 
        "result": "Aborted"
    }))

    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()
    response = client.get('/history')
    expected = {
        "history": [
            {
                "datetime_finished": "2020-11-10T20:21:32", 
                "datetime_started": "2020-11-10T20:00:28", 
                "name": "UM3E_LightClipLowerFlanges", 
                "result": "Finished"
            },
            {
                "datetime_finished": "2020-10-29T22:44:11", 
                "datetime_started": "2020-10-29T22:39:57", 
                "name": "UM3E_cube", 
                "result": "Aborted"
            }
        ]
    }

    assert response.status_code == 200
    assert response.get_json() == expected


# r.delete("history")
# test_server_returns_single_job_in_history()
# test_server_returns_updated_history_when_another_print_job_is_added()
