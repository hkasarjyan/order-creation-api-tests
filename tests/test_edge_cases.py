import pytest
import json
import allure
import os
from utils.api_client import APIClient

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the absolute path to the JSON file
data_file_path = os.path.join(BASE_DIR, "data/test_data_edge.json")

# Load test data
with open(data_file_path) as f:
    test_data = json.load(f)

# Fixture for resetting API state
@pytest.fixture(scope="session", autouse=True)
def reset_api():
    with allure.step("Resetting API state"):
        APIClient.reset()


@allure.feature("Order Creation API")
@allure.story("Edge Cases")
@pytest.mark.parametrize("payload", test_data["edge_orders"])
def test_edge_order_creation(payload):
    with allure.step(f"Testing edge case order creation: {payload}"):
        response = APIClient.post("/orders/create", payload)
        assert response.status_code in [201, 400]
