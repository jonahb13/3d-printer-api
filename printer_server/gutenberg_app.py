from flask import Flask, request, jsonify
import random

def create_app():
    app = Flask(__name__)

    current_job = {
        "datetime_cleaned": "2020-11-21T03:55:42",
        "datetime_finished": "2020-11-21T03:50:32",
        "datetime_started": "2020-11-21T03:44:31",
        "name": "UM3E_Letter_V",
        "reprint_original_uuid": "dd30fe04-dea8-4d7e-89bc-4b49f83284e9",
        "result": "Printing",
        "source": "USB",
        "time_elapsed": 0,
        "time_estimated": 0,
        "time_total": 0,
        "uuid": "a8f8e030-b24b-490a-b145-ce5d900ad768"
    }

    @app.route('/printer/status')
    def get_status():
        return jsonify({'status': 'printing'}), 200

    @app.route('/printer/print_job')
    def get_print_job():
        return jsonify(current_job), 200

    @app.route('/printer/nozzles/temperatures')
    def get_temps():
        nozzle_1_temp_change = round(random.random() + random.randint(220, 225), 1)
        nozzle_2_temp_change = round(random.random() + random.randint(220, 225), 1)
        return jsonify({"nozzle_1": nozzle_1_temp_change, "nozzle_2": nozzle_2_temp_change}), 200

    return app


if __name__ == '__main__':
    create_app().run(port=5501)
