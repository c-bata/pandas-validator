================
pandas-validator
================

.. image:: https://travis-ci.org/c-bata/pandas-validator.svg
    :target: https://travis-ci.org/c-bata/pandas-validator

.. image:: https://badge.fury.io/py/pandas_validator.svg
    :target: http://badge.fury.io/py/pandas_validator

Validates the pandas object such as DataFrame and Series.
And this can define validator like django form class.

.. code-block:: python

    class SampleDataFrameValidator(validators.DataFrameValidator):
        row_num = 5
        column_num = 2
        label1 = validators.IntegerColumnValidator('label1', min_value=0, max_value=10)
        label2 = validators.FloatColumnValidator('label2', min_value=0, max_value=10)


Getting Started
===============

1. Installation

::

    $ pip install pandas_validator

2. Usage

Please see the following demo written by ipython notebook.

* `Demo in Japanese <https://github.com/c-bata/pandas-validator/blob/master/example/pandas_validator_example_ja.ipynb>`_
* `Demo in English <https://github.com/c-bata/pandas-validator/blob/master/example/pandas_validator_example_en.ipynb>`_

License
=======

This software is licensed under the MIT License.


Resources
=========

* `Github <https://github.com/c-bata/pandas-validator>`_
* `PyPI <https://pypi.python.org/pypi/pandas_validator>`_
