Sphinx Documentation
====================
Initialize docs/ directory:

.. code-block:: bash

    sphinx-quickstart

Edit docs/conf.py to enable

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

Edit Makefile to add html task:

.. code-block:: makefile

    html:
	    sphinx-apidoc -o docs . tests setup.py
	    make -C docs html

Follow `An idiot’s guide to Python documentation with Sphinx and ReadTheDocs <https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/>`_
to add README.rst to Sphinx document.