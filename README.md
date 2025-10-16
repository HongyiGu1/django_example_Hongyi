by Hongyi 

Since the database has no primary or foreign keys defined, the backend is limited to handling only GET requests. Performing UPDATE, INSERT, or DELETE operations will result in errors.


install:
Django==5.2.7
django-filter==25.2
djangorestframework==3.16.1
psycopg2-binary==2.9.11

