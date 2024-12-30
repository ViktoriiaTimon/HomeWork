import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth
import os

BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"

LOG_FILE = "test_search.log"

log_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    force = True,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="class")
def authorized_session():
    session = requests.Session()
    logger.info(f"Attempting to authenticate user {USERNAME}")
    auth_response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if auth_response.status_code == 200:
        access_token = auth_response.json().get("access_token")
        logger.info(f'Successful authorization. Token: {access_token}')
        session.headers.update({'Authorization': f'Bearer {access_token}'})
        yield session
    else:
        logger.error(f'Error: {auth_response.json()}')
        pytest.fail('Failed authentication')
    session.close()

@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 10),
    ("price", 1),
    ("year", 0),
    ("non_existing_field", 5),
    ("price", 100)
])
def test_get_cars(authorized_session, sort_by, limit):
    params = {"sort_by": sort_by, "limit": limit}
    response = authorized_session.get(f'{BASE_URL}/cars', params=params)

    logger.info(f'Request was sent: sort_by={sort_by}, limit={limit}')
    logger.info(f'Response status code: {response.status_code}')

    assert response.status_code == 200, f'Error: {response.json()}'

    cars = response.json()
    if limit > 0:
        assert len(cars) <= limit, f'The limit is {limit}'
        if sort_by in ["price", "year", "engine_volume"] and len(cars) > 1:
            sorted_cars = sorted(cars, key=lambda x: x.get(sort_by))
            assert cars == sorted_cars, f'The data was not sorted by {sort_by}'
        else:
            logger.warning(f'The incorrect field sort_by={sort_by}')
    else:
        assert len(cars) == 0, 'The empty list is expected'

    logger.info(f'Server response is {cars}')

    for handler in logging.root.handlers:
        handler.flush()

    if os.path.exists(log_path):
        with open(log_path, 'r') as log_file:
            content = log_file.read()
            if content:
                logger.info("Log file updated successfully.")
            else:
                logger.warning("Log file is still empty.")
