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

.PHONY: all test run clean doc profile

# All target is empty -> python project doesnt have to be compiled
all: run ; 

#todo make archive for submitting
pack: doc createfolder zipfolder; 

#create folder for zipping
createfolder: 
	if not exist ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo mkdir ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo
	if not exist ..\..\xpatek08_xgerge01_xtverd01_xpopos00\doc mkdir ..\..\xpatek08_xgerge01_xtverd01_xpopos00\doc
	if not exist ..\..\xpatek08_xgerge01_xtverd01_xpopos00\installer mkdir ..\..\xpatek08_xgerge01_xtverd01_xpopos00\installer
	xcopy "..\..\ivsproject" "..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo" /e /k /c /r /y /i /h
	xcopy "..\..\ivsproject\doc" "..\..\xpatek08_xgerge01_xtverd01_xpopos00\doc" /e /k /c /r /y /i /h
	xcopy "..\..\ivsproject\installer" "..\..\xpatek08_xgerge01_xtverd01_xpopos00\installer" /e /k /c /r /y /i /h
	if exist ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo\installer $(RMDIR) ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo\installer
	if exist ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo\doc $(RMDIR) ..\..\xpatek08_xgerge01_xtverd01_xpopos00\repo\doc

#zip the folder
zipfolder:
	cd ..\.. && 

# Clean all files that doesnt have to be submitted
#REMOVE PYTHON CACHE
clean: 
	if exist __pycache__ $(RMDIR) __pycache__
	if exist .cache $(RMDIR) .cache
	if exist gui/__pycache__ $(RMDIR) gui\__pycache__
	if exist documentation $(RMDIR) documentation

# Test math library using pytest
# Testing only works on Linux (Ubuntu, WSL) - using pytest
test:
	pytest tests/ --tb=line

# generate doxygen documentation at doc folder (html and pdf)
# Only works on Linux (Ubuntu, WSL) - due to absence of doxygen in Windows Powershell
doc: Doxyfile
	cd .. && rm -rf doc;
	cd .. && mkdir doc 
	doxygen $^
	rm -rf documentation/latex
	cp -a documentation/. ../doc
	rm -rf documentation

# run the calculator
run: main.py
	$(PY) $^

# run the program for profiling with some input
profile: standart_deviation.py 
	$(PY) $^ <..\profiling\data10.txt

