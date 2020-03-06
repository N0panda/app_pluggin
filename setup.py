""" Setup """

import re
from setuptools import setup, find_packages

with open('README.md', 'rb') as f:
    DESCRIPTION = f.read().decode('utf-8')

with open('app-module/__init__.py') as f:
    VERSION = re.search('^__version__\s*=\s*\'(.*)\'', f.read(), re.M).group(1)

DEPENDENCIES = [
    'timeflux @ git+https://github.com/timeflux/timeflux'
]

setup(
    name='brain_game_ressources',
    packages=find_packages(),
    version=VERSION,
    description='Needed features for Brain_game',
    long_description=DESCRIPTION,
    author='Thomas yohan',
    author_email='contact@timeflux.io',
    url='https://timeflux.io',
    install_requires=DEPENDENCIES
)
