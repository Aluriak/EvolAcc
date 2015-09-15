###############################################################################
# RUNNING
###############################################################################
gol:
	python -m evolacc --simulations=gol --steps=20

ggol:
	# test of use of global watcher
	python -m evolacc --simulations=gol --steps=20 --watchers=ImageGenerator

genalg:
	python -m evolacc --simulations=genalg --steps=20

save_config:
	python3 -m evolacc --save_config




###############################################################################
# TESTS
###############################################################################
tt:
	python3 unittests.py



###############################################################################
# TOOLS
###############################################################################
verif:
	pylint evolacc/__main__.py

uml: 
	pyreverse  -AS -o png evolacc -p EvolAcc
	mkdir -p doc/diagrams
	mv packages_* classes_* doc/diagrams/
