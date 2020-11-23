import subprocess
import json
from redis import Redis
from flask import Flask, request, jsonify


def create_app():
    r = Redis()
    app = Flask(__name__)

    @app.route('/')
    @app.route('/history')
    def get_history():
        printer_name = request.args.get('printer')
        if printer_name == 'gutenberg' or printer_name == 'xerox':
            print_history_list = r.lrange(printer_name + '_history', 0, -1)
            print_history_dict_list = [json.loads(x) for x in print_history_list]
            return jsonify({printer_name + "_history": print_history_dict_list}), 200
        else:
            gutenberg_history_list = [json.loads(x) for x in r.lrange('gutenberg_history', 0, -1)]
            xerox_history_list = [json.loads(x) for x in r.lrange('xerox_history', 0, -1)]
            return jsonify({"gutenberg history": gutenberg_history_list, "xerox history": xerox_history_list}), 200

    return app


if __name__ == '__main__':
    subprocess.Popen(['python3', 'history.py'])
    create_app().run(port=5500, use_reloader=False)

