import pytest
from config.config import API_TOKEN

@pytest.fixture(scope="session", autouse=True)
def validate_api_token():
    if not API_TOKEN or API_TOKEN.strip() == "":
        pytest.exit(
            "ERROR: The API_TOKEN is not set or is empty.\n"
            "Please set it as an environment variable (export API_TOKEN=<your_token>)\n"
            "or define it directly in config/config.py (!!not recommended for security reasons!!).",
            returncode=1
        )
