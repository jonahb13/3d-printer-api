import subprocess
import json
from redis import Redis
from flask import Flask, request, jsonify


def create_app():
    r = Redis()
    app = Flask(__name__)

    @app.route('/history')
    def get_history():
        print_history_list = r.lrange('history', 0, -1)
        print_history_dict_list = [json.loads(x) for x in print_history_list]

        return jsonify({"history": print_history_dict_list}), 200


    return app


if __name__ == '__main__':
    # subprocess.Popen(['python3', 'test_double_history.py'])
    create_app().run(port=5500)

