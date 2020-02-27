from typing import (
    Dict,
    Any
)

from importlib import import_module
import re

CONFIG_VAR_RE  = re.compile(r"^[A-Z_]+$")

def load_python_file_data(module_path: str) -> Dict[str, Any]:

    mod = import_module(module_path)
    mod_dict = mod.__dict__

    settings = {}

    for k in mod_dict.keys():
        if CONFIG_VAR_RE.match(k):
            settings[k] = mod_dict[k]

    return settings