
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='extract_autosome',
    version='0.0.1',
    description='extract_autosome package for Python-Guide.org',
    long_description=readme,
    author='Ryan Culligan',
    author_email='rrculligan@gmail.com',
    url='https://github.com/TheCulliganMan/extract_autosome',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
