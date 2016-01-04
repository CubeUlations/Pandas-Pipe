# -*- coding:utf-8 -*-
from setuptools import setup

setup(
    name='pandas_pipe',
    version='0.1',
    url='',
    license='',
    author='siredvin',
    author_email='',
    description='',
    setup_requires=[
        'pytest-runner', 'pandas'
    ],
    tests_require=[
        'pytest'
    ],
    packages=['pandas_pipe'],
    # scripts=['bin/wcss2xml.py'],
    # entry_points={
    #    'console_scripts': [
    #        'wcss2xml = wcss2xml:main']
    #}
)
