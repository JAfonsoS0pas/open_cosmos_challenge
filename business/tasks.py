import requests
import struct
import logging
from celery import shared_task
from django.utils import timezone
from datetime import datetime
from .models import Value, DiscardedValue

logger = logging.getLogger(__name__)


@shared_task
def consumer():
    # Request data
    response = requests.get('http://data_server:28462')
    
    if response.status_code != 200:
        logger.error(f"Failed to fetch data. Status code: {response.status_code}")
        return
    
    data = response.json()

    # Convert time from UNIX Timestamp to datetime
    data_time = datetime.utcfromtimestamp(data['time'])

    # Compare with current time
    current_time = datetime.utcnow()
    time_diff = current_time - data_time

    # Convert little-endian byte encoding to float
    byte_string = bytes(data['value'])
    value_float = struct.unpack('<f', byte_string)[0]

    discard_reasons = []

    if time_diff.total_seconds() > 3600:
        discard_reasons.append("Old Data")
        logger.warning("Data is older than 1 hour. Discarding.")

    if {'system', 'suspect'} & set(data.get('tags', [])):
        discard_reasons.extend(data['tags'])
        logger.warning(f"Data contains {', '.join(data['tags'])} tag(s). Discarding.")

    if discard_reasons:
        value = DiscardedValue(value=value_float, timestamp=data_time, reasons=discard_reasons)
    else:
        value = Value(timestamp=data_time, value=value_float)

    value.save()
    logger.warning("Data processed and stored successfully.")
