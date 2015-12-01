import os
from setuptools import setup, find_packages
from pandas_validator import (
    __version__,
    __license__,
    __author__,
    __author_email__,
)

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()
CHANGES = open(os.path.join(BASE_PATH, 'CHANGES.rst')).read()

__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='pandas_validator',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url='https://github.com/c-bata/pandas-validator',
    description='Validate the pandas objects such as DataFrame and Series.',
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(exclude=['test*']),
    install_requirements=['pandas'],
    keywords='pandas validator',
    license=__license__,
    include_package_data=True,
    test_suite='pandas_validator',
)

