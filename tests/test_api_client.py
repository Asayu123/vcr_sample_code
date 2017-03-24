import vcr
from unittest import TestCase

from bin.sample_api_client import SampleTodoApiClient

# Instantiate VCR in order to Use VCR in test scenario.

vcr_instance = vcr.VCR(  # Following option is often used.
    cassette_library_dir='vcr_sample_code/tests/vcr/cassettes/',  # A Location to storing VCR Cassettes
    decode_compressed_response=True,  # Store VCR content (HTTP Requests / Responses) as a Plain text.
    serializer='json',  # Store VCR Record as a JSON Data
)

# Test Case Definition Starts from here.


class TestApiClient(TestCase):

        def test_todo_filter(self):

            test_target = SampleTodoApiClient()
            test_method = test_target.get_todo

            result = test_method(obj_id=1)

            expected = {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": False
              }

            self.assertEqual(result, expected)
