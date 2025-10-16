from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'biometrics_provider', views.BiometricsProviderViewSet)
router.register(r'device', views.DeviceViewSet)
router.register(r'device_master', views.DeviceMasterViewSet)
router.register(r'notifications', views.NotificationsViewSet)
router.register(r'org_dept', views.OrgDeptViewSet)
router.register(r'organisation', views.OrganisationViewSet)
router.register(r'patient_details', views.PatientDetailsViewSet)
router.register(r'patient_thresholds', views.PatientThresholdsViewSet)
router.register(r'patient_vitals', views.PatientVitalsViewSet)
router.register(r'user_org', views.UserOrgViewSet)

urlpatterns = [
    path('', include(router.urls)),
]