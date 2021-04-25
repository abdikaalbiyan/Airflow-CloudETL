from google.cloud import bigquery
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials



credential_academi = service_account.Credentials.from_service_account_file('pkl-playing-fields-7314d23dc2d0.json')
credential_albiyan = service_account.Credentials.from_service_account_file('academi-week2-e095c9cc0348.json')

project_id_academi = 'pkl-playing-fields'
project_id_albiyan = 'academi-week2'

client_academi = bigquery.Client(credentials=credential_albiyan,project=project_id_academi)
client_albiyan = bigquery.Client(credentials=credential_albiyan,project=project_id_albiyan)

# Your project name
project_name = 'academi-week2'

