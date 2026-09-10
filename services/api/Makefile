
RUN_CMD_DOCKER_RUN := docker compose run $(DOCKER_EXEC_ARGS) --rm api

init: build

build:
	docker compose --file docker-compose.yml up

deps:
	$(POETRY_CMD) install --extras "api-only-dependencies"

start:
	docker compose  --file docker-compose.yml up --detach

stop:
	docker compose down

format:
	$(PY_RUN_CMD) isort --atomic --apply
	$(PY_RUN_CMD) black .
	$(RUN_CMD) prettier --write openapi.yml