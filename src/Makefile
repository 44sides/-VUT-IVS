# PROJECT MAKEFILE - WINDOWS
# IVS 2020
# VUT FIT
# authors:
# 	Daniel Pátek (xpatek08)
#	Gergel Marek (xgerge01)
#	Tverdokhlib Vladyslav (xtverd01)
#	Poposki Vasil (xpopos00)	

PY=python
RM=del
RMDIR=rmdir /S/Q

.PHONY: all test run clean

# All target is empty -> python project doesnt have to be compiled
all: run ; 

#todo make archive
pack: ; 

#todo clean generated files
clean: 
	if exist __pycache__ $(RMDIR) __pycache__
	if exist .cache $(RMDIR) .cache
	if exist gui/__pycache__ $(RMDIR) gui\__pycache__

# Test math library using pytest
# Testing only works on Linux (Ubuntu, WSL)
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

