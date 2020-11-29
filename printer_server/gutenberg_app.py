from flask import Flask, request, jsonify
import random

def create_app():
    app = Flask(__name__)

    gutenberg_print_history = [
        {
            "datetime_cleaned": "2020-11-22T17:15:09",
            "datetime_finished": "2020-11-22T09:34:43",
            "datetime_started": "2020-11-22T07:50:42",
            "name": "Timelapse_UM3E_Letter_V",
            "reprint_original_uuid": None,
            "result": "Finished",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "bc4707d0-910d-4987-850a-576b3d5ff67e"
        },
        {
            "datetime_cleaned": "2020-11-22T07:50:38",
            "datetime_finished": "2020-11-21T06:58:44",
            "datetime_started": "2020-11-21T05:15:01",
            "name": "Timelapse_UM3E_Letter_V",
            "reprint_original_uuid": None,
            "result": "Finished",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "7e5d990f-2648-4a5b-8dfa-85fa081814b0"
        },
        {
            "datetime_cleaned": "2020-11-21T04:10:35",
            "datetime_finished": "2020-11-21T04:09:48",
            "datetime_started": "2020-11-21T04:08:15",
            "name": "Timelapse_UM3E_Letter_V",
            "reprint_original_uuid": "423944ed-187f-4e2e-9e91-70d45144b55e",
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "cefe9a74-7d19-453b-8f7b-7fac88d8ab9a"
        },
        {
            "datetime_cleaned": "2020-11-21T04:08:14",
            "datetime_finished": "2020-11-21T04:07:11",
            "datetime_started": "2020-11-21T04:03:47",
            "name": "Timelapse_UM3E_Letter_V",
            "reprint_original_uuid": "423944ed-187f-4e2e-9e91-70d45144b55e",
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "a58a0958-286c-48bd-abaf-1d2eabee821a"
        },
        {
            "datetime_cleaned": "2020-11-21T04:03:45",
            "datetime_finished": "2020-11-21T04:03:05",
            "datetime_started": "2020-11-21T03:56:19",
            "name": "Timelapse_UM3E_Letter_V",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "423944ed-187f-4e2e-9e91-70d45144b55e"
        },
        {
            "datetime_cleaned": "2020-11-21T03:55:42",
            "datetime_finished": "2020-11-21T03:50:32",
            "datetime_started": "2020-11-21T03:44:31",
            "name": "UM3E_Letter_V",
            "reprint_original_uuid": "dd30fe04-dea8-4d7e-89bc-4b49f83284e9",
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 0,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "a8f8e030-b24b-490a-b145-ce5d900ad768"
        }
    ]

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
