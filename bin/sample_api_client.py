from http import client
import json


class SampleApiClient(object):

    def __init__(self, url):
        self.base_url = url
        pass

    def get_todo(self, title=None):  # Specify title option to filter todos by title.

        conn = client.HTTPConnection(self.base_url, port=80)

        conn.request(method='GET', url='/todos')
        response = conn.getresponse()

        raw_body = response.read()
        json_body = json.loads(raw_body.decode(encoding='utf-8'))

        filtered_data = []  # filter by title
        for entry in json_body:
            if entry['title'] == title:
                filtered_data.append(entry)

        return filtered_data

