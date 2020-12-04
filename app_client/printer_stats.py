import requests
from pprint import pprint

app_url = "http://localhost:5500/"

def request_info(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    pprint(data)

def request_current_job(params):
    url = app_url + 'current_job'
    request_info(url, params)


def request_temps(params):
    url = app_url + 'nozzle_temps'
    request_info(url, params)


def main():
    # Get both printers' current jobs
    params = {'printer': None}
    print('\nGetting the current job for both printers:')
    request_current_job(params)

    # Get Gutenberg's current job
    params = {'printer': 'gutenberg'}
    print('\nGetting the current job for Gutenberg:')
    request_current_job(params)

    # Get Xerox's current job
    params = {'printer': 'xerox'}
    print('\nGetting the current job for Xerox:')
    request_current_job(params)
    
    # Get both printers' past temps
    params = {'printer': None}
    print('\nGetting all the past temperatures for both printers')
    request_temps(params)

    # Get Gutenberg's past temps
    params = {'printer': 'gutenberg'}
    print('\nGetting all the past temperatures for gutenberg')
    request_temps(params)

    # Get Xerox's past temps
    params = {'printer': 'xerox'}
    print('\nGetting all the past temperatures for xerox')
    request_temps(params)


if __name__ == '__main__':
    main()
