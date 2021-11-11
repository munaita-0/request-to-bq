from flask import Flask, request
from google.cloud import bigquery

app = Flask(__name__)


@app.route("/")
def main():
    client = bigquery.Client()
    table = client.get_table("sandbox.test001")
    load_job_config = bigquery.LoadJobConfig(
        autodetect=True,
        create_disposition='CREATE_IF_NEEDED',
        write_disposition='WRITE_TRUNCATE'
    )
    job = client.load_table_from_json(
        [request.args.to_dict()],
        table,
        load_job_config
    )
    job.result()

    return "success"
