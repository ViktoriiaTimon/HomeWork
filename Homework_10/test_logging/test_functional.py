import logging

from .test_homework_10 import log_event

import pytest

class TestUserLogging():

    @pytest.mark.parametrize("username, status, expected_level",
    [
        ("Tom", "success", logging.INFO),
        ("Tom", "expired", logging.WARNING),
        ("Tom", "failed", logging.ERROR),
        ("Tom", None, logging.ERROR),
        ("Tom", " ", logging.ERROR),
    ])

    def test_logging_levels(self, username, status, expected_level):
        log_event(username, status) == expected_level
