from .test_homework_10 import log_event

import pytest

class TestUserLogging():

    def test_success_loging(self):
        log_event(username = 'Tom', status = "success")

    def test_expired_password(self):
        log_event(username = 'Tom', status = "expired")

    def test_failed(self):
        log_event(username='Tom', status = "failed")

    def test_none_data(self):
        log_event(username='Tom', status = None)

    def test_empty_data(self):
        log_event(username='Tom', status = "")