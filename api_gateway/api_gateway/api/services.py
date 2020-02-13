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


def create_experiment(experiment):
    trigger_experiment(experiment)
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

    try:
        response = requests.post(url,
                                 json=serializer.data,
                                 headers={'content-type': 'application/json'}
                                 )
    except:
        print("error")

    '''if response.status_code == 200:
        # trigger_experiment(request_id, house_area, pincode, months)
        return {}
    else:
        return {}
    '''


def trigger_experiment(experiment):
    url = settings.DATA_RETRIEVAL_SERVICE_URL + 'api/v1/request/rain/' + experiment.request_id
    params = {
        'requestId': experiment.request_id,
        'PinCode': experiment.pincode,
        'HouseArea': experiment.house_area,
        'Months': experiment.months
    }

    r = requests.post(url,
                      json=params,
                      headers={'content-type': 'application/json'}
                      )

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
    # TODO remove this code
    experiment_1 = Experiment('admin', 1234, 110095, [1, 2, 6], '213213dfewfdfvadsf', "PENDING")
    experiment_2 = Experiment('admin', 1578, 110092, [2, 5], '23423fbgrfbg', "PENDING")
    experiments = [experiment_1, experiment_2]
    json_data = jsonpickle.encode(experiments, unpicklable=False)

    data = json.loads(json_data)
    serializer = ExperimentSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=True)

    return serializer


def get_experiment(request_id):
    # TODO remove this code
    serializer = get_all_experiments()
    for experiment in serializer.save():
        if experiment.request_id == request_id:
            return experiment
