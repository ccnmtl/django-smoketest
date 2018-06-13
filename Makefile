test:
	rm -rf ve
	virtualenv ve
	./ve/bin/pip install .
	./ve/bin/pip install flake8
	./ve/bin/flake8 smoketest --max-complexity=9
	./ve/bin/python runtests.py

clean:
	rm -rf ve
	find . -name '*.pyc' -exec rm {} \;
