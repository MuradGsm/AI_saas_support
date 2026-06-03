.PHONY: up down logs ps restart

# Поднять всю инфраструктуру
up:
	docker compose up -d

# Остановить всё
down:
	docker compose down

# Посмотреть статус
ps:
	docker compose ps

# Логи конкретного сервиса (make logs service=postgres)
logs:
	docker compose logs -f $(service)

# Перезапустить конкретный сервис (make restart service=postgres)
restart:
	docker compose restart $(service)

# Полный сброс (удалить контейнеры + volumes = все данные!)
reset:
	docker compose down -v
