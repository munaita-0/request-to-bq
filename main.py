from flask import Flask, request
from google.cloud import bigquery

app = Flask(__name__)


@app.route("/")
def main():
    data = {}
    for k, v in request.args.items():
        data[k.replace('.', '_')] = v

    client = bigquery.Client()
    table = client.get_table("sandbox.test001")
    load_job_config = bigquery.LoadJobConfig(
        autodetect=True,
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_APPEND',
        ignore_unknown_values=True,
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION
            ]
    )

    job = client.load_table_from_json(
        [data],
        table,
        load_job_config
    )
    job.result()

    return "success"
