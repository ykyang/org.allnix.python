**<h1>Learn Python from Scratch</h1>**

- [Basic Stuff](#basic-stuff)
  - [Create a script](#create-a-script)
  - [Create a new package](#create-a-new-package)
  - [Develop local package](#develop-local-package)
  - [Resources](#resources)
  
# Basic Stuff

## Create a script
Create `hello.py` in `learnall/` for "Hello World".

## Create a new package
Create the following 
* package directory `learnall/learnall/` 
* and `learnall/learnall/__init__.py`

where `__init__.py` tells `python` this directory is a package.

## Develop local package
Develop the package and use it by install as editable.  In `learnall/`, not `learnall/learnall/`,
```sh
activate py38
pip install -e ./
```
Now `learnall` is accessable in the `py38` environment.  See [Structuring Your Project](https://docs.python-guide.org/writing/structure/).

## Resources
* [Minimal Structure](https://python-packaging.readthedocs.io/en/latest/minimal.html)
* [Structuring Your Project](https://docs.python-guide.org/writing/structure/)
* [Learning Python](https://docs.python-guide.org/intro/learning/)