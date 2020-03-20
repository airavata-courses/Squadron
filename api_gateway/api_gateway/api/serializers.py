import jsonpickle
from rest_framework import serializers
from rest_framework.utils import json


class Experiment(object):
    def __init__(self, username, house_area, pincode, months, request_id=None, status=None, model_result=None, post_processed_result=None):
        self.username = username
        self.house_area = house_area
        self.pincode = pincode
        self.months = months
        self.request_id = request_id
        self.status = status
        self.model_result = model_result
        self.post_processed_result = post_processed_result


class ExperimentSerializer(serializers.Serializer):
    request_id = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(max_length=30, required=True)
    house_area = serializers.IntegerField(required=True)
    pincode = serializers.IntegerField(required=True)
    months = serializers.ListField(required=True)
    status = serializers.CharField(required=False, allow_blank=True)
    model_result = serializers.IntegerField(required=False, allow_blank=True)
    post_processed_result = serializers.IntegerField(required=False, allow_blank=True)

    def create(self, validated_data):
        return Experiment(**validated_data)

    def update(self, instance, validated_data):
        instance.house_area = validated_data.get('house_area', instance.house_area)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.months = validated_data.get('months', instance.months)
        instance.status = validated_data.get('status', instance.status)
        return instance

