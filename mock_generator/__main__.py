import datetime
import random

import dateutil.parser
import requests
from requests.auth import HTTPBasicAuth

from mock_generator import parse_args


if __name__ == '__main__':
    args = parse_args()
    print(args)
    url = '{server}/api/user/{user_id}/installation/{installation_id}/reports'.format(server=args.server,
                                                                                      user_id=args.user_id,
                                                                                      installation_id=args.installation_id)
    from_time = dateutil.parser.parse(args.from_time)
    to_time = dateutil.parser.parse(args.to_time)
    reports_interval = datetime.timedelta(minutes=10)
    current_time = from_time
    while current_time < to_time:
        data = {
            'timestamp': int(current_time.timestamp()),
            'version': '1.0.0',
            'upUsage': random.random(),
            'downUsage': random.random(),
            'upQuality': random.random(),
            'downQuality': random.random(),
            'providerId': args.provider_id,
            'ip': args.ip,
        }
        print(data)
        response = requests.post(url, json=data, auth=HTTPBasicAuth(args.username, args.password))
        if response.status_code not in (200, 204):
            print(response)
        current_time = current_time + reports_interval
