from rest_framework import viewsets
from .models import *
from .serializers import *

class BiometricsProviderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BiometricsProvider.objects.all()
    serializer_class = BiometricsProviderSerializer

class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceMasterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeviceMaster.objects.all()
    serializer_class = DeviceMasterSerializer

class NotificationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer

class OrgDeptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrgDept.objects.all()
    serializer_class = OrgDeptSerializer

class OrganisationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class PatientDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

class PatientThresholdsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PatientThresholds.objects.all()
    serializer_class = PatientThresholdsSerializer

class PatientVitalsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PatientVitals.objects.all()
    serializer_class = PatientVitalsSerializer

class UserOrgViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserOrg.objects.all()
    serializer_class = UserOrgSerializer