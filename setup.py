import os
from setuptools import setup

__author__ = 'Masashi Shibata <contact@c-bata.link>'
__version__ = '0.3.0'

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()
CHANGES = open(os.path.join(BASE_PATH, 'CHANGES.rst')).read()

setup(
    name='pandas_validator',
    version=__version__,
    author=__author__,
    author_email='contact@c-bata.link',
    url='https://github.com/c-bata/pandas-validator',
    description='Validate the pandas objects such as DataFrame and Series.',
    long_description=README + '\n\n' + CHANGES,
    package=['pandas_validator'],
    install_requirements=['pandas'],
    keywords=['pandas', 'validator'],
    license='MIT License',
    include_package_data=True
)
