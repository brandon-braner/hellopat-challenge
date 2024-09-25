.PHONY: up docker frontend backend down check

check: 
	@which docker > /dev/null 2>&1 || { echo >&2 "Docker is required but not installed. Aborting."; exit 1; } 
	@which npm >/dev/null 2>&1 || { echo >&2 "npm is required but not installed. Aborting."; exit 1; } 
	@which poetry >/dev/null 2>&1 || { echo >&2 "Poetry is required but not installed. Aborting."; exit 1; }
docker: check
	@echo "Starting Docker containers..."
	docker compose up -d

frontend: check
	@echo "Starting frontend..."
	cd frontend && nohup npm run dev > logs//dev.log 2>&1 &
	@echo "Dev server is running in the background. Check frontend/logs/dev.log for output. App is running at http://localhost:3000"

backend: check
	@echo "Starting backend..."
	cd backend && nohup poetry run uvicorn main:app --reload > logs/uvicorn.log 2>&1 &
	@echo "Uvicorn running in background. Check backend/logs/uvicorn.log for output. App is running at http://localhost:8000"
up: check docker backend frontend

down: 
	@echo "Stopping the application..." 
	docker compose down 
	-pkill -f "uvicorn main:app"
	-pkill -f "npm run dev"
	@echo "Application stopped"
