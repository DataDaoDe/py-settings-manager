import pytest
import os
from settings_manager.json import load_json_file_data
from settings_manager.manager import SettingsManager

project_root = os.path.join(os.path.dirname(os.path.dirname(__file__)))
data_root = os.path.join(project_root, 'tests/data')

def test_load_json_file():
    json_file_path = os.path.join(data_root, 'json_settings/myenv.json')
    res = load_json_file_data(json_file_path)

    assert len(res.keys()) == 2
    assert res['language'] == 'German'

def test_load_json_settings_for_env():

    sm = SettingsManager(
        'myenv',
        'json',
        os.path.join(data_root, 'json_settings')
    )

    sm.load()

    assert len(sm.settings().keys()) == 2
    assert sm.settings()['language'] == 'German'
    assert sm.get_property('google_keys.client_id') == 1234


def test_load_json_settings_for_env_with_base_merge():
    sm = SettingsManager(
        'myenv',
        'json',
        os.path.join(data_root, 'json_settings'),
        merge_base=True
    )

    sm.load()

    assert len(sm.settings().keys()) == 3
    assert sm.settings()['language'] == 'German'
    assert sm.settings()['database_url'] == 'http://localhost:9292'
    assert sm.settings()['google_keys']['client_id'] == 1234
    assert sm.settings()['google_keys']['client_secret'] == 'foobar'
    assert 'placeholder' in sm.settings()['google_keys'].keys()