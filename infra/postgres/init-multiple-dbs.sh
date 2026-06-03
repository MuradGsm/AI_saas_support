#!/bin/bash
set -e

create_db() {
  local db=$1
  echo "Creating database: $db"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE $db;
EOSQL
}

create_db "auth_db"
create_db "chat_db"
create_db "ai_db"
create_db "notification_db"
