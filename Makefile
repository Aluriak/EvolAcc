all:
	python3 -m evolacc

verif:
	pylint evolacc/__main__.py

uml: 
	pyreverse evolacc/__main__.py -o doc/uml.png
