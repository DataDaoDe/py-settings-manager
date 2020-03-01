from setuptools import find_packages, setup

def read_file(filename: str):
    with open(filename, 'r') as fp:
        data = fp.read()
    return data

setup(
    name = 'settings-manager',
    version = '0.1.0',
    author = 'John Faucett',
    author_email = 'jwaterfaucett@gmail.com',
    description = 'A settings manager for python applications',
    long_description = read_file('./README.md'),
    long_description_context_type = 'text/markdown',
    url = 'https://github.com/DataDaoDe/py-settings-manager',
    packages = find_packages(),
    classifiers = [

    ],
    python_requires = '>= 3.6'
)