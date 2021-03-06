SHELL=/bin/bash

.PHONY: docker

docker:
	docker-compose up

test:
	docker-compose run web pytest -n 4 --nomigrations --cov=. --cov-report=html

local:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/local.txt; \
	)

clean:
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -f */migrations/0*.py
	sudo rm -rf htmlcov/
	sudo rm -f .second_run
	docker-compose down -v

cleanall:
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm */migrations/*.py
	sudo rm -rf htmlcov/
	sudo rm -f .second_run
	docker-compose down -v --rmi local
