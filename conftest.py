from api.jsonplaceholder_api import JsonPlaceholderApi
import pytest 

@pytest.fixture(scope='session')
def public_api():
    return JsonPlaceholderApi()