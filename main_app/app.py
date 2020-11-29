import subprocess
import json
import requests
from redis import Redis
from flask import Flask, request, jsonify

xerox_url = "http://localhost:5502/"
gutenberg_url = "http://localhost:5501/"


def get_status(url):
    url += 'printer/status'
    response = requests.get(url)
    data = response.json()
    return data['status']


def create_app():
    r = Redis()
    app = Flask(__name__)

    def get_job(printer_name):
        status = get_status(gutenberg_url if printer_name == 'gutenberg' else xerox_url)
        if status == 'printing':
            job = json.loads(r.lindex(printer_name + '_history', -1))
            job['nozzle_1'] = float(r.lindex(printer_name + '_nozzle_1_temps', -1))
            job['nozzle_2'] = float(r.lindex(printer_name + '_nozzle_2_temps', -1))
            return job
        else:
            return {printer_name: printer_name + ' is not currently printing'}

    def get_temps(printer_name):
        nozzle_1 = r.lrange(printer_name + '_nozzle_1_temps', 0, -1)
        nozzle_2 = r.lrange(printer_name + '_nozzle_2_temps', 0, -1)
        nozzle_1 = list(map(float, nozzle_1))
        nozzle_2 = list(map(float, nozzle_2))
        return nozzle_1, nozzle_2


    @app.route('/')
    @app.route('/current_job')
    def get_current_print_job():
        printer_name = request.args.get('printer')
        if printer_name == 'gutenberg' or printer_name == 'xerox':
            job = get_job(printer_name)
            return jsonify(job), 200
        else:
            gutenberg_job = get_job('gutenberg')
            xerox_job = get_job('xerox')
            return jsonify({'gutenberg_current_job': gutenberg_job, 'xerox_current_job': xerox_job}), 200

    @app.route('/nozzle_temps')
    def get_current_nozzle_temps():
        printer_name = request.args.get('printer')
        if printer_name == 'gutenberg' or printer_name == 'xerox':
            nozzle_1, nozzle_2 = get_temps(printer_name)
            data = {'nozzle_1_temps': nozzle_1, 'nozzle_2_temps': nozzle_2}
            return jsonify({printer_name + "_nozzle_temps": data}), 200
        else:
            gutenberg_nozzle_1_temps, gutenberg_nozzle_2_temps = get_temps('gutenberg')
            xerox_nozzle_1_temps, xerox_nozzle_2_temps = get_temps('xerox')
            gutenberg_data = {'nozzle_1_temps': gutenberg_nozzle_1_temps, 'nozzle_2_temps': gutenberg_nozzle_2_temps}
            xerox_data = {'nozzle_1_temps': xerox_nozzle_1_temps, 'nozzle_2_temps': xerox_nozzle_2_temps}
            return jsonify({"gutenberg_nozzle_temps": gutenberg_data, "xerox_nozzle_temps": xerox_data}), 200

    return app


if __name__ == '__main__':
    subprocess.Popen(['python3', 'history.py'])
    create_app().run(port=5500, use_reloader=False)

