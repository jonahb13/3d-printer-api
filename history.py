import requests
import json
from redis import Redis

r = Redis()
current_offset = 0
url = 'http://10.99.4.48/api/v1/history/print_jobs'


def get_print_job_info(params):
    """
    Remove unwanted keys from each job dict so that the only info 
    left is the start/end time of the print, print name, and result. 
    """
    response = requests.get(url, params=params)
    history = response.json()
    keys_to_remove = ["datetime_cleaned", "reprint_original_uuid", "source", 
        "time_elapsed", "time_estimated", "time_total", "uuid"]
    for job in history:
        for key in keys_to_remove:
            del job[key]
    return history


def update_redis(response, params, offset_incr):
    r.rpush('history', *map(json.dumps, response))
    params['offset'] += offset_incr


def get_print_history():
    """
    Get current history of the printer.
    """
    params = {'count': 500, 'offset': 0}
    response = get_print_job_info(params)
    while len(response) == params['count']:
        update_redis(response, params, params['count'])
        response = get_print_job_info(params)
    update_redis(response, params, len(response))
    current_offset = params['offset']
    

def update_history():
    params = {'offset': current_offset}
    while True:
        response = get_print_job_info(params)
        if response:
            update_redis(response, params, len(response))
            current_offset += len(response)
        # Do we need to sleep???


if __name__ == '__main__':
    get_print_history()
    # update_history()