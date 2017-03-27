from http import client
import json


class SampleApiClient(object):

    def __init__(self, url):
        self.base_url = url

    def get_todo(self, key='id', value=None):  # Specify key and value to filter todos.

        conn = client.HTTPConnection(self.base_url, port=80)

        conn.request(method='GET', url='/todos')
        response = conn.getresponse()

        raw_body = response.read()
        json_body = json.loads(raw_body.decode(encoding='utf-8'))

        filtered_data = []  # filter logic
        for entry in json_body:
            if entry[key] == value:
                filtered_data.append(entry)

        return filtered_data

