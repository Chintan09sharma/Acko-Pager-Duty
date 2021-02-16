
import pytest
import requests
from dummy.settings import TEST_BASE_URL
# Create your tests here.

def test_create_team():
    data = {"team": {"name": "claims"}, "developers": [{"name": "Chintan", "phone_number":"9999999999"}, {"name": "somebody", "phone_number": "9111111111"}]}
    url = TEST_BASE_URL+'mine/create_team/'
    response = requests.post(url=url, json=data)
    response_data =response.text
    assert response.status_code == 200


def test_post_alert():
    data = {"team_id": 1}
    url = TEST_BASE_URL+'mine/post_alert/'
    response = requests.post(url=url, json=data)
    response_data = response.text
    assert response.status_code == 200