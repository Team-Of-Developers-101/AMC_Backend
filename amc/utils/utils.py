import datetime
import json
import logging
import traceback
from flask import Response, jsonify


def error_response(*, message, status_code):
    if type(message) != dict:
        message = str(message)
    return jsonify(status="error", data=None, message=message), status_code


def custom_response(*, message, data, status_code):
    response = {
        "status": "success",
        "message": message,
        "data": data,
    }

    return Response(
        mimetype="application/json",
        response=json.dumps(response),
        status=status_code
    )


def resource_not_found(e):
    return error_response(message="URL not be found", status_code=404)


def internal_server_error(e):
    logging.critical(
        f"\n{'='*30} SERVER ERROR {datetime.datetime.now()} {'='*30}\n\n {traceback.format_exc()}\n{'='*24} END SERVER ERROR {'='*24}\n",
    )
    return error_response(message="Internal server error.", status_code=500)
