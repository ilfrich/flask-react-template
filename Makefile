SHELL:=/bin/bash
include .env


start:
	python3 runner.py

dev:
	IS_DEBUG=1 python3 runner.py

install-deps:
	pip3 install -r requirements.txt
	npm install

clean:
	rm -f _logs/*.log*
	rm -f static/*.hot-update.js*

check-lint:
	find . -name '*.py' | while read file; do \
	    pycodestyle $$file; \
	done; \

lint:
	find . -name '*.py' | while read file; do \
	    pycodestyle $$file; \
	    if [[ $$? != 0 ]]; then exit $$?; fi \
	done; \

frontend:
	npm run hot-client

build:
	npm run build