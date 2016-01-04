from setuptools import setup

setup(
    name='Pandas-Pipe',
    version='0.45',
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
