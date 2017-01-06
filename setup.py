import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.rst')).read()
CHANGES = open(os.path.join(BASE_PATH, 'CHANGES.rst')).read()

__author__ = 'Masashi Shibata <contact@c-bata.link>'
__version__ = '0.5.0'
__license__ = 'MIT License'
__author_email__ = 'contact@c-bata.link'
__url__ = 'https://github.com/c-bata/pandas-validator'
__description__ = 'Validate the pandas objects such as DataFrame and Series.'
__classifiers__ = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='pandas_validator',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    description=__description__,
    long_description=README + '\n\n' + CHANGES,
    packages=find_packages(exclude=['test*']),
    install_requires=['pandas'],
    keywords='pandas validator',
    license=__license__,
    include_package_data=True,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    test_suite='pandas_validator',
)
