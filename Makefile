install:
	pip3 install --upgrade setuptools wheel twine

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

clean:
	rm -rf dist build speak2mary.egg-info
