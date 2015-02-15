all:
	python -m evolacc --universe_size=6,6 --genomes=GolCell

al:
	python3 -m evolacc


tt:
	python3 unittests.py

verif:
	pylint evolacc/__main__.py

uml: 
	pyreverse evolacc/__main__.py -o doc/uml.png

