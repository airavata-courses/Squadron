import io

import jsonpickle
import requests

# returns status and login token
import uuid
from django.conf import settings

from api.serializers import Experiment

from api.serializers import ExperimentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


def register(username, password, first_name, last_name, email):
    url = settings.USER_SERVICE_URL + 'api/register/'
    params = {
            'username': username,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
            }

    r = requests.create(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

    if r.status_code == 200:
        return {'token': r.json().get('token'), 'register': 'success'}
    else:
        return {'register': 'failed'}


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


def token_verify(token):
    url = settings.USER_SERVICE_URL + 'api/api-token-verify/'
    params = {'token': token}

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

    if r.status_code == 200:
        return True
    else:
        return False


def create_experiment(experiment):
    url = settings.SESSION_MANAGEMENT_SERVICE_URL + 'api/v1/session/'

    params = {'request_id': experiment.request_id,
              'user_id': experiment.username,
              'pincode': experiment.pincode,
              'house_area': experiment.house_area,
              'status': 'PENDING',
              'months': experiment.months}
    serializer = ExperimentSerializer(experiment)
    # content = JSONRenderer().render(serializer.data)
    print(serializer.data)
    print(json.dumps(serializer.data))

    response = requests.post(url,
                             json=serializer.data,
                             headers={'content-type': 'application/json'}
                             )
    if response.status_code == 201:
        print("Trigger experiment is called here")
        trigger_experiment(experiment)
        return {}
    else:
        return {}


def trigger_experiment(experiment):
    url = settings.DATA_RETRIEVAL_SERVICE_URL + 'api/v1/request/rain/'
    params = {
        'username': experiment.username,
        'request_id': experiment.request_id,
        'pincode': experiment.pincode,
        'house_area': experiment.house_area,
        'months': experiment.months
    }

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )
    print(r.status_code)
    print(r)
    if r.status_code == 200:
        print("Sent successfully")
        return {}
    else:
        return {}


def update_experiment(experiment):
    serializer = ExperimentSerializer(experiment)
    # content = JSONRenderer().render(serializer.data)
    print(serializer.data)
    print(json.dumps(serializer.data))


def get_all_experiments(username=None):
    url = settings.SESSION_MANAGEMENT_SERVICE_URL + 'api/v1/session/user/' + username

    '''# TODO remove this code
    experiment_1 = Experiment('admin', 1234, 110095, [1, 2, 6], '213213dfewfdfvadsf', "PENDING")
    experiment_2 = Experiment('admin', 1578, 110092, [2, 5], '23423fbgrfbg', "PENDING")
    experiments = [experiment_1, experiment_2]
    json_data = jsonpickle.encode(experiments, unpicklable=False)
    '''
    response = requests.get(url)
    json_data = response.json()
    print(response.json())
    # data = json.loads(json_data)
    serializer = ExperimentSerializer(data=json_data, many=True)
    serializer.is_valid(raise_exception=True)

    return serializer


def get_experiment(request_id):
    url = settings.SESSION_MANAGEMENT_SERVICE_URL + 'api/v1/session/' + request_id
    response = requests.get(url)
    json_data = response.json()
    print(json_data)

    serializer = ExperimentSerializer(data=json_data)
    serializer.is_valid(raise_exception=True)

    experiment = serializer.save()

    return experiment
