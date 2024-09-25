.PHONY: up docker frontend backend down

docker:
	@echo "Starting Docker containers..."
	docker compose up -d

frontend:
	@echo "Starting frontend..."
	cd frontend && npm run dev

backend:
	@echo "Starting backend..."
	cd backend && poetry run uvicorn main:app --reload

up: docker backend frontend

down:
	@echo "Stopping the application..."
	docker compose down
	pkill -f "uvicorn main:app"
	pkill -f "npm run dev"
	@echo "Application stopped"
