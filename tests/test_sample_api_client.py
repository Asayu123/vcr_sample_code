from unittest import TestCase
from bin.sample_api_client import SampleApiClient
# Test Case Definition Starts from here.


class TestApiClient(TestCase):

        def test_todo_filter(self):

            client = SampleApiClient(url='jsonplaceholder.typicode.com')
            # a free online REST service that produces some fake JSON data.

            result = client.get_todo(title="delectus aut autem")

            expected = [
                {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
              }
            ]

            self.assertEqual(expected, result)
