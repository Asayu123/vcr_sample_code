from http import client


class SampleTodoApiClient(object):

    url = 'https://jsonplaceholder.typicode.com'  # a free online REST service that produces some fake JSON data.

    def __init__(self):
        raise NotImplementedError

    def get_todo(self, obj_id=None): # Specify obj_id option to filter todos by user obj_id.
        raise NotImplementedError
