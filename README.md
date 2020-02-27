## Settings Manager

Settings Manager is designed to handle settings in python projects.

It makes the assumption you are working with environments and building applications.

The API consists of 2 functions `load()` to load the application settings and `settings()` to get access to a dict of the application settings.

## Usage

You can put environment variables in your yaml config files and they will be loaded from the environment when the file is loaded. Calls to get environment variables like `os.getenv()` also work in python config files. Only json config files cannot contain environment variables.

**Examples**

```yaml
app:
    secret_key: ${SECRET_KEY}
    google_client_id: ${GOOGLE_CLIENT_ID}
```

```python
SECRET_KEY = os.getenv('SECRET_KEY')
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
```

### JSON Config Files


Imagine you are working on a project with the following structure:

```
myapp/
  app.py
config/
  settings/
    test.json
    dev.json
    prod.json
```

```python
from settings_manager.manager import SettingsFile

sm = SettingsFile(
        environment = 'test', 
        filetype = 'json'
        settings_dir = '/path/to/project/root/config/settings'    
)

sm.load()

# view settings dictionary
sm.settings() # { 'secret-key' : 'h390h2g3', ... }
```

### YAML Config Files


Imagine you are working on a project with the following structure:

```
myapp/
  app.py
config/
  settings/
    test.yaml
    dev.yaml
    prod.yaml
```

Your yaml files can have `.yml` or `.yaml` file extensions.

```python
from settings_manager.manager import SettingsFile

sm = SettingsFile(
        environment = 'test', 
        filetype = 'yaml'
        settings_dir = '/path/to/project/root/config/settings'    
)

sm.load()

# view settings dictionary
sm.settings() # { 'secret-key' : 'h390h2g3', ... }
```

### Python Config Files


Imagine you are working on a project with the following structure:

```
myapp/
  app.py
config/
  settings/
    test.py
    dev.py
    prod.py
```

```python
from settings_manager.manager import SettingsFile

sm = SettingsFile(
        environment = 'test', 
        filetype = 'python'
        settings_dir = '/path/to/project/root/config/settings'
        python_settings_module = 'config.settings'    
)

sm.load()

# view settings dictionary
sm.settings() # { 'secret-key' : 'h390h2g3', ... }
```

## TODOS

1. Add ability to merge configs when there is a `base` config file.