import os

def pytest_sessionstart(session):
    # create needed environment variables
    os.environ['TEST_ENVVAR'] = 'something'

def pytest_sessionfinish(session, exitstatus):
    # delete artificially created environment variables
    del os.environ['TEST_ENVVAR']