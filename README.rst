================
pandas-validator
================

.. image:: https://travis-ci.org/c-bata/pandas-validator.svg
    :target: https://travis-ci.org/c-bata/pandas-validator

.. image:: https://badge.fury.io/py/pandas_validator.svg
    :target: http://badge.fury.io/py/pandas_validator

.. image:: https://readthedocs.org/projects/pandas-validator/badge/?version=latest
    :target: https://readthedocs.org/projects/pandas-validator/?badge=latest
    :alt: Documentation Status

Validates the pandas object such as DataFrame and Series.
And this can define validator like django form class.

.. code-block:: python

    import pandas as pd
    import pandas_validator as pv

    class SampleDataFrameValidator(pv.DataFrameValidator):
        row_num = 5
        column_num = 2
        label1 = pv.IntegerColumnValidator('label1', min_value=0, max_value=10)
        label2 = pv.FloatColumnValidator('label2', min_value=0, max_value=10)

    validator = SampleDataFrameValidator

    df = pd.DataFrame({'label1': [0, 1, 2, 3, 4], 'label2': [5.0, 6.0, 7.0, 8.0, 9.0]})
    validator.is_valid(df)  # True.

    df = pd.DataFrame({'label1': [11, 12, 13, 14, 15], 'label2': [5.0, 6.0, 7.0, 8.0, 9.0]})
    validator.is_valid(df)  # False.

    df = pd.DataFrame({'label1': [0, 1, 2], 'label2': [5.0, 6.0, 7.0]})
    validator.is_valid(df)  # False


Getting Started
===============

Installation
------------

::

    $ pip install pandas_validator

Usage
-----

Please see the following demo written by ipython notebook.

* `Demo in Japanese <https://github.com/c-bata/pandas-validator/blob/master/example/pandas_validator_example_ja.ipynb>`_
* `Demo in English <https://github.com/c-bata/pandas-validator/blob/master/example/pandas_validator_example_en.ipynb>`_

Documentation
=============

The latest documentation is hosted at ReadTheDocs.

http://pandas-validator.readthedocs.org

Requirements
============

* Traget Python version is 2.7, 3.4
* pandas

License
=======

This software is licensed under the MIT License.


Resources
=========

* `Github <https://github.com/c-bata/pandas-validator>`_
* `PyPI <https://pypi.python.org/pypi/pandas_validator>`_
