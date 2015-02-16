gol:
	python -m evolacc --factory=GolFactory

save_config:
	python3 -m evolacc --save_config


tt:
	python3 unittests.py

verif:
	pylint evolacc/__main__.py

uml: 
	pyreverse evolacc/__main__.py -o doc/uml.png

