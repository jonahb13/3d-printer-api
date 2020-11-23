from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    xerox_print_jobs = [
        {
            "datetime_cleaned": "2020-10-26T23:25:57",
            "datetime_finished": "2020-10-26T23:25:02",
            "datetime_started": "2020-10-26T23:23:12",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": "d4b27408-cbf3-4368-95ca-f8661c59d4b5",
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 77.120703,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "a03c7645-0d44-4aa7-ac0a-7246d31a36cc"
        },
        {
            "datetime_cleaned": "2020-10-26T23:23:07",
            "datetime_finished": "2020-10-26T23:22:41",
            "datetime_started": "2020-10-26T23:14:38",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 3.874528,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "d4b27408-cbf3-4368-95ca-f8661c59d4b5"
        },
        {
            "datetime_cleaned": "2020-10-26T23:07:58",
            "datetime_finished": "2020-10-26T23:07:47",
            "datetime_started": "2020-10-26T23:01:26",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 219.419793,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "6dd8c222-e826-4cf1-808e-7938ba06549c"
        },
        {
            "datetime_cleaned": "2020-10-26T22:59:30",
            "datetime_finished": "2020-10-26T22:58:36",
            "datetime_started": "2020-10-26T22:47:06",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 510.946285,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "001b5c08-d1ec-4c69-be45-9f29514942ad"
        },
        {
            "datetime_cleaned": "2020-10-26T22:41:43",
            "datetime_finished": "2020-10-26T22:40:47",
            "datetime_started": "2020-10-26T22:37:56",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": "4489dcda-711c-45d2-9a3a-341040759aed",
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 77.028995,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "46bc3ae9-cf1f-4e17-8226-61c06be8bbf1"
        },
        {
            "datetime_cleaned": "2020-10-26T22:37:30",
            "datetime_finished": "2020-10-26T22:36:18",
            "datetime_started": "2020-10-26T22:29:46",
            "name": "UM3E_star_guy_bottom",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "USB",
            "time_elapsed": 0.056822,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "4489dcda-711c-45d2-9a3a-341040759aed"
        },
        {
            "datetime_cleaned": "2020-10-26T22:27:53",
            "datetime_finished": "2020-10-26T20:03:35",
            "datetime_started": "2020-10-26T17:56:03",
            "name": "UM3E_mascarilla_original",
            "reprint_original_uuid": None,
            "result": "Finished",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 7533.44613,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "d2da1c33-adea-4eff-973a-d5b1186cab22"
        },
        {
            "datetime_cleaned": "2020-10-26T17:55:52",
            "datetime_finished": "2020-10-26T17:54:20",
            "datetime_started": "2020-10-26T17:38:14",
            "name": "UM3E_mascarilla_original",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 592.140105,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "b3050688-e82c-45f0-9263-317cfa25a245"
        },
        {
            "datetime_cleaned": "2020-10-26T16:52:56",
            "datetime_finished": "2020-10-26T02:24:39",
            "datetime_started": "2020-10-25T19:20:16",
            "name": "UM3E_mascarilla_original",
            "reprint_original_uuid": "faf39c27-8b16-4c33-bffd-697a12151346",
            "result": "Finished",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 25360.402184,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "e4a03b8d-bbc2-446f-83ea-ab0c602f2f30"
        },
        {
            "datetime_cleaned": "2020-10-25T19:20:14",
            "datetime_finished": "2020-10-25T19:18:47",
            "datetime_started": "2020-10-25T19:11:16",
            "name": "UM3E_mascarilla_original",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 257.477297,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "faf39c27-8b16-4c33-bffd-697a12151346"
        },
        {
            "datetime_cleaned": "2020-10-25T19:08:22",
            "datetime_finished": "2020-10-25T19:07:02",
            "datetime_started": "2020-10-25T18:46:45",
            "name": "UM3E_mascarilla_original",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 0.172654,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "7be96263-05f3-4c68-be09-5f04f64a4ceb"
        },
        {
            "datetime_cleaned": "2020-10-25T18:37:13",
            "datetime_finished": "2020-10-25T18:33:05",
            "datetime_started": "2020-10-25T18:30:49",
            "name": "UM3E_BAT_Cookie_cutter_rgproduct_Heidi",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 26.209719,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "d2fdd454-9828-4f66-9381-dd1ed6c9f76d"
        },
        {
            "datetime_cleaned": "2020-10-25T18:30:41",
            "datetime_finished": "2020-10-25T18:29:13",
            "datetime_started": "2020-10-25T18:22:39",
            "name": "UM3E_BAT_Cookie_cutter_rgproduct_Heidi",
            "reprint_original_uuid": None,
            "result": "Aborted",
            "source": "WEB_API/Unknown/Cura connect",
            "time_elapsed": 25.502346,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "3178a7c4-87e2-481d-8aa7-5a2d074d0e43"
        },
        {
            "datetime_cleaned": "2020-10-25T16:59:13",
            "datetime_finished": "2020-10-24T05:41:11",
            "datetime_started": "2020-10-23T21:53:22",
            "name": "UM3E_bigger_star_top",
            "reprint_original_uuid": "ebdcc582-1985-4a43-b4c4-5ed2201c3ad2",
            "result": "Finished",
            "source": "USB",
            "time_elapsed": 28012.06421,
            "time_estimated": 0,
            "time_total": 0,
            "uuid": "1c143cac-6a9e-44c1-aa30-82e9bcb8a9f1"
        }
    ]


    @app.route('/history/print_jobs')
    def get_history():
        return jsonify(xerox_print_jobs), 200

    return app



if __name__ == '__main__':
    create_app().run(port=5502)
