import logging
from .test_homework_10 import log_event
import pytest


class TestUserLogging:
    @pytest.mark.parametrize("username, status, expected_level",
                             [
                                 ("Tom", "success", 'INFO'),
                                 ("Tom", "expired", 'WARNING'),
                                 ("Tom", "failed", 'ERROR'),
                             ])
    def test_logging_levels(self, username, status, expected_level):
        log_event(username, status)

        file_log = "login_system.log"
        with open(file_log, mode='r') as f:
            line = f.readlines()
            last_log = line[-1].strip()

        log_content = f"Login event - Username: {username}, Status: {status} - {expected_level}"

        assert log_content in last_log, f"{log_content} not found in the last log: {last_log}"

