import keys.azureA
import requests
import pandas as pd
from datetime import date


# Script Retrieves Alerts from MDE Service
# https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/run-advanced-query-api?view=o365-worldwide

# keys.azureA is just a file to store variables that is also ignored by gitignore
# This data can be stored and retrieved in env variables

tenant_id = keys.azureA.tenantid     # Tenant ID for Azure Tenant ID or Directory ID
client_id = keys.azureA.clientid     # Client ID from AAD-APP
client_secret = keys.azureA.secret   # Client secret from AAD-APP

# Set Variables for Auth Web Request

auth_url = f'https://login.windows.net/{tenant_id}/oauth2/token'

resource_url = 'https://api.securitycenter.windows.com'

auth_req_body = {
        'resource': resource_url,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
            }

auth_head = {'Content-Type': 'application/x-www-form-urlencoded'}

# Oath2 Token Retrieval Web Request

auth_response = requests.request('POST', auth_url, headers=auth_head, data=auth_req_body).json()
auth_token = auth_response['access_token']

# Token Validation
# print(auth_response)
# print(auth_token)

# Set API Request Variables

api_call_url = 'https://api.securitycenter.windows.com/api/alerts'

req_headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + auth_token
        }

# API Web Request
api_call_response = requests.request('GET', api_call_url, headers=req_headers).json()

# Validate
# print(api_call_response)

# Dict to Dataframe and Dump to csv
df = pd.DataFrame.from_dict(api_call_response['value'])
df.to_csv('MDE-Alert-Dump@' + str(date.today()) + '.csv')

