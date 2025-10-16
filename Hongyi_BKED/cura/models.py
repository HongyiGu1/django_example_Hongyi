# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BiometricsProvider(models.Model):
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    device_provider = models.TextField(blank=True, null=True)
    device_type_model = models.TextField(blank=True, null=True)
    api_provider = models.TextField(blank=True,primary_key=True)
    dev_api_vital_name = models.TextField(blank=True, null=True)
    vital_name = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)
    dev_api_vital_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biometrics_provider'

class Device(models.Model):
    device_id = models.TextField(blank=True,primary_key=True)
    device_type = models.TextField(blank=True, null=True)
    device_working_status = models.TextField(blank=True, null=True)
    device_provider = models.TextField(blank=True, null=True)
    device_reference_id = models.TextField(blank=True, null=True)
    device_user_id = models.TextField(blank=True, null=True)
    device_email = models.TextField(blank=True, null=True)
    device_kit_ref_id = models.TextField(blank=True, null=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    dev_alloc_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    patient_id = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DeviceMaster(models.Model):
    device_id = models.TextField(blank=True,primary_key=True)
    device_type = models.TextField(blank=True, null=True)
    device_working_status = models.TextField(blank=True, null=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    sensors_perdev_qty = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    device_provider = models.TextField(blank=True, null=True)
    device_reference_id = models.TextField(blank=True, null=True)
    device_user_id = models.TextField(blank=True, null=True)
    device_email = models.TextField(blank=True, null=True)
    device_kit_ref_id = models.TextField(blank=True, null=True)
    dev_start_date = models.DateTimeField(blank=True, null=True)
    dev_end_date = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_master'


class Notifications(models.Model):
    device_id = models.TextField(blank=True, null=True)
    patient_id = models.TextField(blank=True, null=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    patient_vital = models.TextField(blank=True, null=True)
    notification_type = models.TextField(blank=True, null=True)
    notification_desc = models.TextField(blank=True,primary_key=True)
    notification_time = models.DateTimeField(blank=True, null=True)
    hcp_user_email = models.TextField(blank=True, null=True)
    hcp_mobile_number = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OrgDept(models.Model):
    organisation_id = models.TextField(blank=True, null=True,)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    dept_id = models.TextField(blank=True,primary_key=True)
    dept_desc = models.TextField(blank=True, null=True)
    vital_name = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_dept'


class Organisation(models.Model):
    organisation_id = models.TextField(blank=True,primary_key=True)
    organisation_desc = models.TextField(blank=True, null=True)
    organisation_type = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    org_status_flg = models.TextField(blank=True, null=True)
    org_address = models.TextField(blank=True, null=True)
    address_line1 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    post_code = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    contact_person = models.TextField(blank=True, null=True)
    contact_number = models.TextField(blank=True, null=True)
    contact_email_id = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organisation'


class PatientDetails(models.Model):
    patient_id = models.TextField(blank=True,primary_key=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    patient_monitoring_status = models.TextField(blank=True, null=True)
    familyname = models.TextField(blank=True, null=True)
    givenname = models.TextField(blank=True, null=True)
    middlename = models.TextField(blank=True, null=True)
    nametype = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    post_code = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    patient_age = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    patient_discharge_dt = models.DateField(blank=True, null=True)
    dateofdeath = models.DateField(blank=True, null=True)
    email_id = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    identities = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    maritalstatus = models.TextField(blank=True, null=True)
    pasid = models.TextField(blank=True, null=True)
    mergedpasid = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    mobilenumber = models.TextField(blank=True, null=True)
    landlinenumber = models.TextField(blank=True, null=True)
    medicarenumber = models.TextField(blank=True, null=True)
    medicareexpirydate = models.DateTimeField(blank=True, null=True)
    healthinsurer = models.TextField(blank=True, null=True)
    insurancepolicynumber = models.TextField(blank=True, null=True)
    insuranceexpirydate = models.DateTimeField(blank=True, null=True)
    dr_name_1 = models.TextField(blank=True, null=True)
    contact_no1 = models.TextField(blank=True, null=True)
    contact_speciality_1 = models.TextField(blank=True, null=True)
    dr_name_2 = models.TextField(blank=True, null=True)
    contact_no2 = models.TextField(blank=True, null=True)
    contact_speciality_2 = models.TextField(blank=True, null=True)
    dr_name_3 = models.TextField(blank=True, null=True)
    contact_no3 = models.TextField(blank=True, null=True)
    contact_speciality_3 = models.TextField(blank=True, null=True)
    dr_name_4 = models.TextField(blank=True, null=True)
    contact_no4 = models.TextField(blank=True, null=True)
    contact_speciality_4 = models.TextField(blank=True, null=True)
    dr_name_5 = models.TextField(blank=True, null=True)
    contact_no5 = models.TextField(blank=True, null=True)
    contact_speciality_5 = models.TextField(blank=True, null=True)
    dr_name_6 = models.TextField(blank=True, null=True)
    contact_no6 = models.TextField(blank=True, null=True)
    contact_speciality_6 = models.TextField(blank=True, null=True)
    dr_name_8 = models.TextField(blank=True, null=True)
    contact_no8 = models.TextField(blank=True, null=True)
    contact_speciality_8 = models.TextField(blank=True, null=True)
    dr_name_9 = models.TextField(blank=True, null=True)
    contact_no9 = models.TextField(blank=True, null=True)
    contact_speciality_9 = models.TextField(blank=True, null=True)
    dr_name_10 = models.TextField(blank=True, null=True)
    contact_no10 = models.TextField(blank=True, null=True)
    contact_speciality_10 = models.TextField(blank=True, null=True)
    diagnosis_summary = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)
    patient_admission_dt = models.DateField(blank=True, null=True)
    dr_name_7 = models.TextField(blank=True, null=True)
    contact_no7 = models.TextField(blank=True, null=True)
    contact_speciality_7 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_details'


class PatientThresholds(models.Model):
    patient_id = models.TextField(blank=True,primary_key=True)
    patient_qr_code = models.BinaryField(blank=True, null=True)
    patient_bar_code = models.BinaryField(blank=True, null=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    threshold_monitoring_status = models.TextField(blank=True, null=True)
    patient_location_timezone = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    vital_type = models.TextField(blank=True, null=True)
    threshold_max_value = models.FloatField(blank=True, null=True)
    threshold_min_value = models.FloatField(blank=True, null=True)
    hcp_mobile_number = models.TextField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_thresholds'


class PatientVitals(models.Model):
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    device_id = models.CharField(blank=True, null=True)
    device_type = models.CharField(blank=True, null=True)
    device_provider = models.TextField(blank=True, null=True)
    device_reference_id = models.TextField(blank=True, null=True)
    device_user_id = models.TextField(blank=True, null=True)
    device_email = models.TextField(blank=True, null=True)
    device_kit_ref_id = models.TextField(blank=True, null=True)
    patient_id = models.CharField(blank=True,primary_key=True)
    vital_type = models.CharField(blank=True, null=True)
    vital_value = models.FloatField(blank=True, null=True)
    vital_time_utc = models.DateTimeField(blank=True, null=True)
    vital_status = models.CharField(blank=True, null=True)
    vital_time_patient_tz = models.DateTimeField(blank=True, null=True)
    patient_location_timezone = models.TextField(blank=True, null=True)
    threshold_max_value = models.FloatField(blank=True, null=True)
    threshold_min_value = models.FloatField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_vitals'


class UserOrg(models.Model):
    mobileapp_user_email = models.TextField(blank=True,primary_key=True)
    user_role = models.TextField(blank=True, null=True)
    organisation_id = models.TextField(blank=True, null=True)
    organisation_desc = models.TextField(blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True)
    branch_desc = models.TextField(blank=True, null=True)
    dept_service = models.TextField(blank=True, null=True)
    user_status = models.TextField(blank=True, null=True)
    user_start_date = models.DateTimeField(blank=True, null=True)
    user_end_date = models.DateTimeField(blank=True, null=True)
    org_location_tz = models.TextField(blank=True, null=True)
    enigma_cr_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_cr_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_cr_by = models.TextField(blank=True, null=True)
    enigma_up_dt_mobdevtz = models.DateTimeField(blank=True, null=True)
    enigma_up_dt_utc = models.DateTimeField(blank=True, null=True)
    enigma_up_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_org'
