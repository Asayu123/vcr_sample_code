from unittest import TestCase
from bin.sample_api_client import SampleApiClient
# Test Case Definition Starts from here.


class TestSampleApiClient(TestCase):

        def test_get_todo_by_title(self):

            client = SampleApiClient(base_url='jsonplaceholder.typicode.com')
            # a free online REST service that produces some fake JSON data.

            result = client.get(resource='todos', key='title', value="delectus aut autem")

            expected = [
                {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
              }
            ]

            self.assertEqual(expected, result)
