###############################################################################
# RUNNING
###############################################################################
gol:
	python -m evolacc --factories=GolFactory --universe_size=20,20 --steps_at_start=20 --watchers=GolWatcher

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
