"""Build the i2ClusterSSH package."""
from setuptools import setup, find_packages
import os

VERSION = "0.0.2"


def read(fname):
    """Utility function to read the README file.

    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='i2ClusterSSH',
    version=VERSION,
    url='https://github.com/jamesduffy/i2ClusterSSH',
    author='James Duffy',
    author_email='james@duffy.xyz',
    packages=find_packages(),
    install_requires=[
        'Click>=7.0',
        'boto3>=1.9.24',
    ],
    long_description=read('README.md'),
    entry_points={
        'console_scripts': [
            'i2cluster=i2ClusterSSH:cli',
        ]
    },
    test_suite='tests',
)
