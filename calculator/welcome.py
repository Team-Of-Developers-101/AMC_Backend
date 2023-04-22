from amc.utils.utils import custom_response


def welcome_status():
    """ This Function returns the API status of the Welcome Page"""
    response = {
        'message': "Loading...",
        'data': "Welcome to AMC",
        'status_code': 200
    }
    return custom_response(**response)