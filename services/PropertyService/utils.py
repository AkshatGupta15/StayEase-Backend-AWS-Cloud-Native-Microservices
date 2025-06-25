import json
from datetime import datetime

def _response(code, body):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }

def fix_dates(record):
    for k, v in record.items():
        if isinstance(v, datetime):
            record[k] = v.isoformat()
    return record
