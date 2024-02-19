import requests
import struct
import logging
from celery import shared_task
from django.utils import timezone
from datetime import datetime
from .models import Value

logger = logging.getLogger(__name__)


@shared_task
def consumer():
    # Request data
    response = requests.get('http://data_server:28462')
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        # Convert time from UNIX Timestamp to datetime
        data_time = datetime.utcfromtimestamp(data['time'])
        # Compare with current time
        current_time = datetime.utcnow()
        time_diff = current_time - data_time

        if time_diff.total_seconds() < 3600:
            if 'system' not in data['tags'] and 'suspect' not in data['tags']:
                byte_string = bytes(data['value'])
                # Convert little-endian byte encoding to float
                value_float = struct.unpack('<f', byte_string)[0]

                # Create and save Value object
                value = Value(timestamp=data_time, value=value_float)
                value.save()
                logger.warning("Data processed and stored successfully.")
            else:
                logger.warning(f"Data contains {', '.join(data['tags'])} tag(s). Ignoring.")
        else:
            logger.warning("Data is older than 1 hour. Discarding.")