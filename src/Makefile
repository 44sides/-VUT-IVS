# PROJECT MAKEFILE
# IVS 2020
# VUT FIT
# authors:
# 	Daniel Pátek (xpatek08)
#	Gergel Marek (xgerge01)
#	Tverdokhlib Vladyslav (xtverd01)
#	Poposki Vasil (xpopos00)	

PY=python
RM=rm -rf

.PHONY: test gui run

# All target is empty -> python project doesnt have to be compiled
all: ; 

#todo make archive
pack: ; 

#todo clean generated files
clean: 
	$(RM) *.pyc __pycache__ .cache gui/__pycache__

# Test math library using pytest
test:
	pytest tests/ --tb=line

#todo generate doxygen documentation
doc: ; 

# Run the project
run:
	$(PY) main.py

# todo Run the profile program
profile:
	;

