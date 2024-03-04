from googleapiclient.discovery import build
import functions_framework

@functions_framework.cloud_event
def trigger_df_job(cloud_event):   
 
    service = build('dataflow', 'v1b3')
    project = "your-project-name"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_CSV_to_BigQuery"

    template_body = {
        "jobName": "csv-to-bq-3",  # Provide a unique name for the job
        "parameters": {
        "inputFilePattern": "gs://your-bucket/path/*.csv",
        "schemaJSONPath": "gs://your-bucket/bq.json",
        "outputTable": "your-project-name:demo_dataset.demo_table",
        "bigQueryLoadingTemporaryDirectory": "gs://your-bucket/temp_dir",
        "badRecordsOutputTable": "your-project-name:demo_dataset.demo_bad_records",
        "delimiter": ",",
        "csvFormat": "RFC4180",     
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
