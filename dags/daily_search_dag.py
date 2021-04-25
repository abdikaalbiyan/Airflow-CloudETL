from datetime import datetime, timedelta

from airflow import models
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.utils.dates import days_ago


bucket_path = models.Variable.get("bucket_path")
bucket_input = models.Variable.get("bucket_input")

project_id = models.Variable.get("project_id")


convert_search_keyword_query = """
            SELECT
                SAFE_CAST(user_id AS INT64 ) user_id,
                search_keyword,
                SAFE_CAST(search_result_count AS INT64 ) search_result_count,
                created_at
            FROM
                `academi-week2.search_history.temp_search_history`
            """


most_searched_keyword_query = """
            SELECT
                search_keyword,
                SUM(search_result_count) AS total_search_result,
                '{{ ds }}' AS date
            FROM
                `academi-week2.search_history.converted_search_history`
            WHERE
                SAFE_CAST(LEFT(created_at, 10) AS DATE) = '{{ ds }}'
            GROUP BY
                search_keyword
            ORDER BY 
                SUM(search_result_count) DESC
            LIMIT 1;
            """

default_args = {
    "start_date": datetime(2021, 3, 10),
    "end_date": datetime(2021, 3, 15),
    "depends_on_past": True,
    "dataflow_default_options": {
        "project": project_id,
        # This is a subfolder for storing temporary files, like the staged pipeline job.
        "temp_location": bucket_path + "/tmp/",
        "numWorkers": 1,
    },
}


# Define a DAG (directed acyclic graph) of tasks.
# Any task you create within the context manager is automatically added to the
# DAG object.
with models.DAG(
    # The id you will see in the DAG airflow page
    "search_history_dag",
    default_args=default_args,
    # The interval with which to schedule the DAG
    schedule_interval=timedelta(days=1),  # Override to match your needs
) as dag:
    
    store_to_bq = GoogleCloudStorageToBigQueryOperator(
        task_id="gcs_to_bq",
        bucket=bucket_input,
        source_objects= ["keyword_search-search_{{ ds_nodash }}.csv"],
        destination_project_dataset_table="search_history.temp_search_history",
        source_format="csv",
        skip_leading_rows=1,
        schema_fields=[
            {'name': 'user_id', 'type': 'STRING', 'mode': 'REQUIRED'},
            {'name': 'search_keyword', 'type': 'STRING', 'mode': 'REQUIRED'},
            {'name': 'search_result_count', 'type': 'STRING', 'mode': 'REQUIRED'},
            {'name': 'created_at', 'type': 'STRING', 'mode': 'REQUIRED'},
        ],
        schema_object=bucket_path + '/jsonSchema.json',
        write_disposition="WRITE_TRUNCATE",
        wait_for_downstream=True,
        depends_on_past=True
    )

    convert_data_type = BigQueryOperator(
        task_id='convert_data_type',
        sql=convert_search_keyword_query,
        write_disposition='WRITE_APPEND',
        destination_dataset_table=project_id + ":search_history.converted_search_history",
        use_legacy_sql=False,
    )


    bigquery_job = BigQueryOperator(
        task_id='bigquery_most_searched_keywords',
        sql=most_searched_keyword_query,
        write_disposition='WRITE_APPEND',
        destination_dataset_table=project_id + ":search_history.top_search_history",
        use_legacy_sql=False,
    )

    store_to_bq >> convert_data_type >> bigquery_job
