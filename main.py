import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from google.api_core.exceptions import Conflict

from createBigQueryTable import create_table, schemaTempKeyword, schemaTransaction, \
                                schemaTopKeyword, schemaConvertedKeyword

from config import credential_academi, credential_albiyan,\
                    project_id_academi, project_id_albiyan, \
                    client_academi, client_albiyan, \
                    project_name



temp_search_history_table_id      = "academi-week2.search_history.temp_search_history"
converted_search_history_table_id = "academi-week2.search_history.converted_search_history"
top_search_history_table_id       = "academi-week2.search_history.top_search_history"
transaction_table_id              = "academi-week2.transactions.transaction"


if __name__ == "__main__":
    create_table(temp_search_history_table_id, schemaTempKeyword) #Create table all_search_history in search_history Dataset
    create_table(converted_search_history_table_id, schemaConvertedKeyword) #Create table all_search_history in search_history Dataset
    create_table(top_search_history_table_id, schemaTopKeyword) #Create table top_search_history_table_id in search_history Dataset
    create_table(transaction_table_id, schemaTransaction) #Create table transaction in transactions Dataset