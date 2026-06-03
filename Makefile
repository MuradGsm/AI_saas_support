.PHONY: up down logs ps restart

up:
	docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f $(service)

restart:
	docker compose restart $(service)

reset:
	docker compose down -v
