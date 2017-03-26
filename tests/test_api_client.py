import vcr

from unittest import TestCase
from bin.sample_api_client import SampleApiClient

# Instantiate VCR in order to Use VCR in test scenario.

vcr_instance = vcr.VCR(  # Following option is often used.
    cassette_library_dir='tests/vcr/cassettes/',  # A Location to storing VCR Cassettes
    decode_compressed_response=True,  # Store VCR content (HTTP Requests / Responses) as a Plain text.
    serializer='json',  # Store VCR Record as a JSON Data
)

# Test Case Definition Starts from here.


class TestApiClient(TestCase):
        @vcr_instance.use_cassette
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
