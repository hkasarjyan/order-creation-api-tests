import pytest
import json
import allure
import os
from utils.api_client import APIClient

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the absolute path to the JSON file
data_file_path = os.path.join(BASE_DIR, "data/test_data_negative.json")

# Load test data
with open(data_file_path) as f:
    test_data = json.load(f)

# Fixture for resetting API state
@pytest.fixture(scope="session", autouse=True)
def reset_api():
    with allure.step("Resetting API state"):
        APIClient.reset()


@allure.feature("Order Creation API")
@allure.story("Negative Cases")
@pytest.mark.parametrize("payload", test_data["invalid_orders"])
def test_invalid_order_creation(payload):
    with allure.step(f"Testing invalid order creation: {payload}"):
        response = APIClient.post("/orders/create", payload)
        assert response.status_code == 400
        assert "error" in response.json()
