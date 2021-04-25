# Cloud ETL On Google Cloud Platform


## Installation

Use git to clone this repository

```git clone https://github.com/abdikaalbiyan/Cloud-ETL.git```

## Prequisite

> Python 3.7.3

To run the script in this repository, you need to install the prerequisite library from requirements.txt

> pip install -r requirements.txt

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


<br>
<br>


<br>

Create dataset on Google BigQuery<br>
Set dataset id, let say `search_history`<br>
Set location, choose `US` for example<br>

<img width="1422" alt="Screen Shot 2021-04-22 at 13 03 34" src="https://user-images.githubusercontent.com/22974798/115663892-58b4bc80-a36b-11eb-8aae-addaaed1aded.png">







First of all, we need to enable the API.


<img width="564" alt="Screen Shot 2021-04-22 at 19 54 52" src="https://user-images.githubusercontent.com/22974798/115717793-ba454d00-a3a4-11eb-85d3-f12b790d6ee2.png">

## Google Cloud Platform Setup
Things that you need to set up are:
1. Service Accounts. Make sure that Service Account used has Owner role to enable all Google Services.
2. Google Cloud Composer. This is a fully managed workflow orchestration service built in popular Apache Airflow open source project and operated using the Python programming language. Create an environment here by using the Service Account that has Owner role. For complete steps please refer [this tutorial](https://cloud.google.com/composer/docs/how-to/managing/creating)
3. Airflow Web UI. In GCP we use Airflow to schedule workflow. After environment is created, go to Environment Configuration then click the Airflow web UI. Set up variables we will be using in Variables. Set:

     i.  ``bucket_path`` **(path of your created bucket)**<br>
     ii. ``project_id`` **(your project id)**
     
4. Google Cloud Storage. Create a bucket in Google Cloud Storage to store data sources and additional files needed. For complete steps, you can see [here](https://cloud.google.com/composer/docs/how-to/using/using-dataflow-template-operator)

<p align="center">
<img width="1440" alt="Screen Shot 2021-04-25 at 20 40 05" src="https://user-images.githubusercontent.com/22974798/115995712-86696200-a606-11eb-912e-2444b31e5b91.png">
<img width="1440" alt="Screen Shot 2021-04-25 at 20 40 23" src="https://user-images.githubusercontent.com/22974798/115995714-88332580-a606-11eb-985e-e277fd0fada3.png">
                                                          <i>Google Cloud Composer Environment Monitoring Tab</i>
</p>
<br>
<br>

## Apache Airflow
Apache Airflow is a platform to programmatically (using Python) author, schedule, and monitor workflows. Workflows are implemented as directed acyclic graphs (DAGs) of tasks. With Airflow, you can schedule your tasks and specify dependencies among them. Pipelines also generated to monitor tasks status and troubleshoot problem if needed.

<p align="center">
  <img width="1440" alt="Screen Shot 2021-04-25 at 20 47 59" src="https://user-images.githubusercontent.com/22974798/115995951-92a1ef00-a607-11eb-8c14-a40e72e75638.png">
<i>Airflow home UI</i>
</p>
<br>

### Writing the Airflow's DAGs

1.  Importing modules
2.  Default Arguments
3.  Instantiate a DAG Tasks
4.  Setting up Dependencies

<br>
<br>

## Batch Processing Cases
### Integrate Daily Search History

Running Interval: 2021-03-10 until 2021-03-15
<br>
Schedule: Daily
<br>
**Tasks:**

1.  Load .csv files into BigQuery (BQ) table. BQ Schema is same as .csv files.
2.  Convert fields into correct format.
3.  Get the most searched word and store to BQ table.
<br>

**Running steps:**

1.  Upload dag file daily_search_dag.py to dags/ folder of your environment.
Check the task status on Airflow Web UI by clicking this:<br>
<p align="center">
<img width="759" alt="Screen Shot 2021-04-25 at 21 07 03" src="https://user-images.githubusercontent.com/22974798/115996636-40160200-a60a-11eb-83eb-a3f108bd26bd.png">
</p>

  2.  Result:
<p align="center">
<img width="545" alt="Screen Shot 2021-04-25 at 21 18 12" src="https://user-images.githubusercontent.com/22974798/115997035-ce3eb800-a60b-11eb-8641-c6687f57c7d4.png">
</p>
