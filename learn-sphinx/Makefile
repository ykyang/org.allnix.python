init:
	pip install -r requirements.txt

test:
	nosetests tests

html:
	sphinx-apidoc -f -o docs . tests setup.py
	make -C docs html
