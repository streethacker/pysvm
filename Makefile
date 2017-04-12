help:
	@echo 'Makefile for pysvm                       '
	@echo '                                         '
	@echo 'Usage:                                   '
	@echo '    make install    install as a package '

requirements:
	pip install -r requirements.txt

requirements-dev:
	pip install -r requirements-dev.txt

install: requirements
	python setup.py install --record install.record
	@echo
	@echo "Install finished"

test: requirements-dev
	python setup.py install --record install.record
	@echo
	@echo "Install finished"

dev: requirements-dev
	python setup.py install --record install.record
	@echo
	@echo "Install finished"
