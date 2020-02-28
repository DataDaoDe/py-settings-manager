import pytest
import os
from settings_manager.yaml import load_yaml_file_data
from settings_manager.manager import SettingsManager

project_root = os.path.join(os.path.dirname(os.path.dirname(__file__)))
data_root = os.path.join(project_root, 'tests/data')

def test_load_json_file():
    yaml_file_path = os.path.join(data_root, 'yaml_settings/myenv.yml')
    res = load_yaml_file_data(yaml_file_path)

    assert len(res.keys()) == 3
    assert res['app_name'] == 'testing-123'
    assert res['something_new'] == 'Something Nice!'
    assert res['database']['host'] == 'google.com'

def test_load_json_file_with_envvars():
    yaml_file_path = os.path.join(data_root, 'yaml_settings/myenv_with_envvars.yml')
    res = load_yaml_file_data(yaml_file_path)

    test_envvar_value = os.getenv('TEST_ENVVAR')
    assert test_envvar_value != None

    assert len(res.keys()) == 4
    assert res['app_name'] == 'testing-123'
    assert res['something_new'] == 'Something Nice!'
    assert res['database']['host'] == 'google.com'
    assert res['test_envvar'] == test_envvar_value


def test_load_yaml_settings_for_env():

    sm = SettingsManager(
        'myenv_with_envvars',
        'yml',
        os.path.join(data_root, 'yaml_settings')
    )

    sm.load()
    
    res = sm.settings()

    test_envvar_value = os.getenv('TEST_ENVVAR')
    assert test_envvar_value != None

    assert len(res.keys()) == 4
    assert res['app_name'] == 'testing-123'
    assert res['something_new'] == 'Something Nice!'
    assert res['database']['host'] == 'google.com'
    assert res['test_envvar'] == test_envvar_value


def test_load_json_settings_for_env_with_base_merge():
    sm = SettingsManager(
        'myenv',
        'yml',
        os.path.join(data_root, 'yaml_settings'),
        merge_base=True
    )

    sm.load()

    res = sm.settings()

    test_envvar_value = os.getenv('TEST_ENVVAR')
    assert test_envvar_value != None

    assert len(res.keys()) == 4
    assert res['app_name'] == 'testing-123'
    assert res['something_new'] == 'Something Nice!'
    assert res['database']['host'] == 'google.com'
    assert res['random_number'] == 100