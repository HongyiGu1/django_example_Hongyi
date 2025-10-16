from rest_framework import serializers
from .models import (
    BiometricsProvider, Device, DeviceMaster, Notifications, OrgDept,
    Organisation, PatientDetails, PatientThresholds, PatientVitals, UserOrg
)

class BiometricsProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricsProvider
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceMaster
        fields = '__all__'

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

class OrgDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgDept
        fields = '__all__'

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'

class PatientThresholdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientThresholds
        fields = '__all__'

class PatientVitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVitals
        fields = '__all__'

class UserOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrg
        fields = '__all__'