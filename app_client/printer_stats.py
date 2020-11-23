import requests
from pprint import pprint

def request_info(url, params):
    response = requests.get(url, params)
    response.raise_for_status()
    data = response.json()
    pprint(data)


def main():
    app_url = "http://localhost:5500/history"
    
    # Get both printers' history
    params = {'printer': None}
    print("Single request getting both printers' history:")
    request_info(app_url, params)

    # Get gutenberg's history
    params['printer'] = 'gutenberg'
    print("Single request getting gutenberg's history:")
    request_info(app_url, params)

    # Get xerox's history
    params['printer'] = 'xerox'
    print("Single request getting xerox's history:")
    request_info(app_url, params)

if __name__ == '__main__':
    main()