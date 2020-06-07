all: clean init doc setup pycache

init:
	@echo "Entering setup"
	@echo "Generating virtual environment"
	virtualenv -p python3 venv
	venv/bin/python3 -m pip install -r requierements.txt

setup:
	venv/bin/python3 Setup_GUI.py

clean:
	@echo "Entering clean"
	@echo "Cleaning"
	rm -rvf __pycache__
	rm -rvf venv
	rm -rvf doc/build

pycache:
	@echo "Removing __pycache__"
	rm -rvf __pycache

doc:
	@echo "Generating documentation"
	venv/bin/sphinx-build -M html doc/source doc/build
