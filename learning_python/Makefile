init:
	pip install -r requirements.txt

test:
	nosetests tests

html:
	sphinx-apidoc -o docs . tests setup.py
	make -C docs html

clean:
	make -C docs clean