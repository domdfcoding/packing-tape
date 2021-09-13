#############
shippinglabel
#############

.. start short_desc

**Utilities for handling packages.**

.. end short_desc

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/shippinglabel/latest?logo=read-the-docs
	:target: https://shippinglabel.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/shippinglabel/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/shippinglabel/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/shippinglabel/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/shippinglabel/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/shippinglabel/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/shippinglabel/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/shippinglabel/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.herokuapp.com/github/domdfcoding/shippinglabel/badge.svg
	:target: https://dependency-dash.herokuapp.com/github/domdfcoding/shippinglabel/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/shippinglabel/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/shippinglabel?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/shippinglabel?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/shippinglabel
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/shippinglabel
	:target: https://pypi.org/project/shippinglabel/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/shippinglabel?logo=python&logoColor=white
	:target: https://pypi.org/project/shippinglabel/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/shippinglabel
	:target: https://pypi.org/project/shippinglabel/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/shippinglabel
	:target: https://pypi.org/project/shippinglabel/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/shippinglabel?logo=anaconda
	:target: https://anaconda.org/domdfcoding/shippinglabel
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/shippinglabel?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/shippinglabel
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/shippinglabel
	:target: https://github.com/domdfcoding/shippinglabel/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/shippinglabel
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/shippinglabel/v1.0.0
	:target: https://github.com/domdfcoding/shippinglabel/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/shippinglabel
	:target: https://github.com/domdfcoding/shippinglabel/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/shippinglabel
	:target: https://pypi.org/project/shippinglabel/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``shippinglabel`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install shippinglabel

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install shippinglabel

.. end installation
