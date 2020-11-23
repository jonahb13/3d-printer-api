import requests
import json
from redis import Redis

r = Redis()
current_offset = 0
# xerox_ip = '10.99.4.48'
xerox_url = "http://localhost:5502/history/print_jobs"
# gutenberg_ip = 'http://gutenberg.cslab.moravian.edu/api/v1/history/print_jobs'
gutenberg_url = "http://localhost:5501/history/print_jobs"
# xerox_url = f'http://xerox.cslab.moravian.edu/api/v1/history/print_jobs'


def get_print_job_info(params, url):
    """
    Remove unwanted keys from each job dict so that the only info 
    left is the start/end time of the print, print name, and result. 
    """
    response = requests.get(url, params=params)
    history = response.json()
    history = [{'name': job['name'], 'result': job['result'], 'datetime_started': job['datetime_started'], 
        'datetime_finished': job['datetime_finished']} for job in history]
    return history


def update_redis(response, params, offset_incr, url):
    key = 'gutenberg_history' if url == gutenberg_url else 'xerox_history'
    r.rpush(key, *map(json.dumps, response))
    params['offset'] += offset_incr


def get_print_history(url):
    """
    Get current history of the printer.
    """
    params = {'count': 500, 'offset': 0}
    response = get_print_job_info(params, url)
    while len(response) == params['count']:
        update_redis(response, params, params['count'])
        response = get_print_job_info(params)
    update_redis(response, params, len(response), url)
    current_offset = params['offset']
    

def update_history():
    params = {'offset': current_offset}
    while True:
        response = get_print_job_info(params)
        if response:
            update_redis(response, params, len(response))
            current_offset += len(response)
        # time.sleep(5)


if __name__ == '__main__':
    get_print_history(gutenberg_url)
    get_print_history(xerox_url)
    # update_history()