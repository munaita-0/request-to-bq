from flask import Flask, request
from google.cloud import bigquery
import json

app = Flask(__name__)


@app.route("/")
def main():
    print(json.dumps(request.args))

    a = request.args

    data = {
        'aid': a['sgtm_app_id'],
        'timestamp': a['event_timestamp'],
        'inserted_at': None,
        'user': {
            'client_id': a['FPID_cookie'],
            'client_id_1st_cookie': None,
            'client_id_3rd_cookie': None,
            'client_id_local_storage': None,
            'properties': json.dumps({
                '_ga_cookie': a['_ga_cookie'],
                'FPLC_cookie': a['FPLC_cookie'],
                '_fbc_cookie': a['_fbc_cookie'],
                '_fbp_cookie': a['_fbp_cookie'],
                '_od_cid_cookie': a['_od_cid_cookie']
            })
        },
        'tracing': {
            'trace_id': None,
            'requested_at': None,
            'resent_flg': None,
            'resent_trace_id': None,
            'request_id': None,
            'url_hash': None,
        },
        'sdk': {
            'type': a['sdk_type'],
            'version': a['x-ga-gtm_version']
        },
        'request': {
            'ip': a['ip_override'],
            'user_agent': a['user_agent'],
            'referer': a['page_location']
        },
        'device_info': {
            'os': 'get_from_user_agent',
            'os_version': 'get_from_user_agent',
            'browser': 'get_from_user_agent',
            'browser_version': 'get_from_user_agent',
            'screen_resolution': a['screen_resolution'],
            'viewport_size': None,
            'encoding': None,
            'screen_colors': None,
            'lanuage': a['language'],
            'java_enabled': None,
            'flash_version': None
        },
        'origin': {
            'referrer': a['page_referrer'],
            'utm': {
                'source': 'get_from_pege_location',
                'medium': 'get_from_pege_location',
                'campaign': 'get_from_pege_location',
                'term': 'get_from_pege_location',
                'content': 'get_from_pege_location',
            },
            'adplan': {
                'medium': None,
                'campagn': None,
                'ad_group': None,
                'keyword': None,
                'keyword_match_type': None
            }
        },
        'location': {
            'protocol': 'get_from_page_location',
            'origin': a['page_location'],
            'hostname': a['page_location_hostname'],
            'pathname': a['page_location_pathname'],
            'search': a['page_location_search'],
            'hash': None
        },
        'page_lifecycle': {
            'navigation_type': a['navigation_type'],
            'was_discarded': None,
        },
        'event': {
            'action': a['event_name'],
            'category': None,
            'label': None,
            'params': json.dumps({
                'ga_session_id': a['ga_session_id'],
                'ga_session_number': a['ga_session_number'],
            }),
        },
        'latency_tracking': {
            'dom_content_loaded_time': a['dom_content_loaded_time'],
            'page_load_time': a['page_load_time'],
        },
        'document': {
            'title': a['page_title']
        }

    }

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
