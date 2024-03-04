# Building a fully automated data Pipeline with Google Cloud Services
The project is a fully automated data pipeline with various google cloud services.

## Description

### Objective
  The project is designed with a purpose to explore various google cloud services. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes cloud composer, cloud stoarage, cloud functions, dataflow, bigquery, looker.
  Although each of these cloud service can do individually the task of loading to bigquey from stoarage, the pipline explores connecting the various services. 

### Tools & Technologies
- Language - [**Python**](https://www.python.org)
- Orchestration - [**cloud composer**](https://cloud.google.com/composer?hl=en)
- trigger - [**cloud functions**](https://cloud.google.com/functions?hl=en)
- datalake - [**cloud stoarage**](https://cloud.google.com/storage?hl=en)
- data Processing - [**dataflow**](https://cloud.google.com/dataflow?hl=en)
- Data Warehouse - [**bigquery**](https://cloud.google.com/bigquery?hl=en)

### Architecture
![Architecture.JPG](https://github.com/mahesh-c-pathak/gcs_pipeline/blob/main/Architecture.JPG)

  The diagram above provides a detailed insight into pipeline's architecture. 
  
**Data ingestion** - Python library Faker is used that generate synthetic data for testing, development, and analysis purposes. It provides a range of methods to generate realistic fake data, such as names, addresses, phone numbers, email addresses, dates, and more

**Orchestration** - cloud composer, google managed Apache Airflow, automates the task to store the data in a CSV format within Google Cloud Storage (GCS), ensuring accessibility and scalability for future processing

**Cloud Function Trigger** - A cloud function triggers upon the file upload to the GCS bucket, serving as the initiator for our subsequent data processing steps. The function meticulously handle triggers and pass the requisite parameters to seamlessly initiate the Dataflow job, ensuring a smooth flow of data processing

**Dataflow Job for BigQuery** - A dataflow job triggered by the Cloud Function, this job orchestrates the transfer of data from the CSV file in GCS to BigQuery. The job settings meticulously configured to ensure optimal performance and accurate data ingestion into BigQuery. The dataflow template GCS_CSV_to_BigQuery is used.

**Data Warehouse** -  **BigQuery** stores & persists data from dataflow job.
