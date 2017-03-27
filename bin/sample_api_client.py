from http import client
import json


class SampleApiClient(object):

    def __init__(self, base_url):
        """
        An Api Client that accesses to resources under specific url.
        :param base_url: root url of API server that contains several resources (String)
        """
        self.base_url = base_url

    def get(self, resource, key='id', value=None):  # Specify key and value to filter todos.
        """
        An method to get entry of specific resources that satisfy following searching option.
        :param resource: a relative path from base_url that correspond to resource you want to access.(String)
        :param key: a attribute key of resource you want to filter by. default: id (String)
        :param value: a value of an attribute you want to filter by. (String)
        :return: filtered_data: a result of operation. (Array of Dictionary)
        """

        # create connection, and get raw data from API server
        conn = client.HTTPConnection(self.base_url, port=80)

        conn.request(method='GET', url=('/' + resource))
        response = conn.getresponse()

        raw_body = response.read()
        json_body = json.loads(raw_body.decode(encoding='utf-8'))

        # filter if value is specified.
        if value is not None:
            filtered_data = []
            for entry in json_body:
                if entry[key] == value:
                    filtered_data.append(entry)
        else:
            filtered_data = json_body

        return filtered_data

