import requests

# returns status and login token
import uuid
from django.conf import settings


def user_login(username, password):
    url = settings.USER_SERVICE_URL + 'api/api-token-auth/'
    params = {'username': username, 'password': password}

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

    if r.status_code == 200:
        return {'token': r.json().get('token'), 'login': 'success'}
    else:
        return {'login': 'failed'}


def record_experiment(username, house_area, pincode, months=[], request_id=None):
    if request_id is None:
        request_id = username + uuid.uuid4()

    url = settings.SESSION_MANAGEMENT_SERVICE_URL + ''

    params = {'requestId': request_id,
              'userId': username,
              'pincode': pincode,
              'houseArea': house_area,
              'status': 'PENDING',
              'months': months}

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

    if r.status_code == 200:
        trigger_experiment(request_id, house_area, pincode, months)
        return {}
    else:
        return {}


def trigger_experiment(request_id, house_area, pincode, months=[]):
    url = settings.DATA_RETRIEVAL_SERVICE_URL + ''
    params = {'requestId': request_id,
              'pincode': pincode,
              'houseArea': house_area,
              'status': 'PENDING',
              'months': months}

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

    if r.status_code == 200:
        return {}
    else:
        return {}
