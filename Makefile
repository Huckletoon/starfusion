all: build run

build:
	docker-compose build starfusion

run:
	docker-compose run starfusion