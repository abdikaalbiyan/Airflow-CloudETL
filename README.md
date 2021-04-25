# Cloud ETL On Google Cloud Platform
## *This Project still On Going*

<br>
<br>





First of all, we need to enable the API.


<img width="564" alt="Screen Shot 2021-04-22 at 19 54 52" src="https://user-images.githubusercontent.com/22974798/115717793-ba454d00-a3a4-11eb-85d3-f12b790d6ee2.png">




Create dataset on Google BigQuery<br>
Set dataset id, let say `search_history`<br>
Set location, choose `US` for example<br>

<img width="1422" alt="Screen Shot 2021-04-22 at 13 03 34" src="https://user-images.githubusercontent.com/22974798/115663892-58b4bc80-a36b-11eb-8aae-addaaed1aded.png">



Create virtualenv *(named venv or etc, up to you)*.
```bash
virtualenv venv
```

Activated python virtual env
```bash
source venv_academi/bin/activate
```

Then install all requirements
```bash
pip install -r requirements.txt
```


Change ./config.py cloud configuration
```
credential = service_account.Credentials.from_service_account_file('your_credential.json')

project_id = 'your_project_id'

client = bigquery.Client(credentials=credential,project=project_id)

project_name = 'your_project_name'

```
