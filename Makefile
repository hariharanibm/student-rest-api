db-start:
	docker compose up -d postgres

migrate:
	flask db upgrade

test:
	pytest

lint:
	flake8 app/

docker-build:
	docker build -t student-api:1.0.0 .

api-start:
	docker compose up -d api

start:
	make db-start
	sleep 10
	make migrate
	make docker-build
	make api-start
