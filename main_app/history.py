import requests
import json
from redis import Redis
import time

r = Redis()
xerox_url = "http://localhost:5502/"
gutenberg_url = "http://localhost:5501/"


def get_temps(url):
    url += 'printer/nozzles/temperatures'
    response = requests.get(url)
    temps = response.json()
    return temps['nozzle_1'], temps['nozzle_2']
  

def get_print_job(url):
    url += 'printer/print_job'
    response = requests.get(url)
    job = response.json()
    return job
    
    
def get_job_info(job):
    return {'name': job['name'], 'result': job['result'], 'datetime_started': job['datetime_started'], 
        'datetime_finished': job['datetime_finished']}


def update_print_and_temp_histories():
    gutenberg_prev_job = None    
    xerox_prev_job = None
    while True:
        gutenberg_response = get_print_job(gutenberg_url)
        xerox_response = get_print_job(xerox_url)

        if gutenberg_response and gutenberg_response != gutenberg_prev_job:
            job_info = get_job_info(gutenberg_response)
            r.rpush('gutenberg_history', json.dumps(job_info))
            gutenberg_prev_job = gutenberg_response
        if xerox_response and xerox_response != xerox_prev_job:
            job_info = get_job_info(xerox_response)
            r.rpush('xerox_history', json.dumps(job_info))
            xerox_prev_job = xerox_response

        gutenberg_nozzle_1, gutenberg_nozzle_2 = get_temps(gutenberg_url)
        xerox_nozzle_1, xerox_nozzle_2 = get_temps(xerox_url)

        r.rpush('gutenberg_nozzle_1_temps', gutenberg_nozzle_1)
        r.rpush('gutenberg_nozzle_2_temps', gutenberg_nozzle_2)

        r.rpush('xerox_nozzle_1_temps', xerox_nozzle_1)
        r.rpush('xerox_nozzle_2_temps', xerox_nozzle_2)
        

        time.sleep(5)


if __name__ == '__main__':
    update_print_and_temp_histories()