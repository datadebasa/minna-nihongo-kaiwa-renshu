# MinnaKaiwa - Minna no Nihongo Practice Platform
# Makefile untuk development dan deployment

.PHONY: help install dev build run test clean docker-build docker-run docker-stop

# Default target
help:
	@echo "MinnaKaiwa - Minna no Nihongo Practice Platform"
	@echo ""
	@echo "Available commands:"
	@echo "  install     - Install dependencies"
	@echo "  dev         - Run development server"
	@echo "  build       - Build Docker image"
	@echo "  run         - Run with Docker Compose"
	@echo "  test        - Run tests"
	@echo "  clean       - Clean up files"
	@echo "  docker-build- Build Docker image"
	@echo "  docker-run  - Run with Docker"
	@echo "  docker-stop - Stop Docker containers"
	@echo "  deploy      - Deploy to production"

# Install dependencies
install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Installing Vercel CLI..."
	npm install -g vercel

# Run development server
dev:
	@echo "Starting development server..."
	vercel dev

# Alternative development server
dev-flask:
	@echo "Starting Flask development server..."
	cd api && python index.py

# Build Docker image
build:
	@echo "Building Docker image..."
	docker build -t minnakaiwa .

# Run with Docker Compose
run:
	@echo "Starting MinnaKaiwa with Docker Compose..."
	docker-compose up -d

# Run tests
test:
	@echo "Running tests..."
	python -m pytest tests/ -v

# Clean up files
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage

# Docker commands
docker-build:
	@echo "Building Docker image..."
	docker build -t minnakaiwa .

docker-run:
	@echo "Running MinnaKaiwa with Docker..."
	docker run -p 5000:5000 minnakaiwa

docker-stop:
	@echo "Stopping Docker containers..."
	docker-compose down

# Production deployment
deploy:
	@echo "Deploying to production..."
	vercel --prod

# Development with production profile
dev-prod:
	@echo "Starting production-like environment..."
	docker-compose --profile production up -d

# Logs
logs:
	@echo "Showing logs..."
	docker-compose logs -f

# Shell access
shell:
	@echo "Opening shell in container..."
	docker-compose exec minnakaiwa bash

# Health check
health:
	@echo "Checking application health..."
	curl -f http://localhost:5000/ || echo "Application is not responding"

# Backup audio files
backup-audio:
	@echo "Backing up audio files..."
	tar -czf audio-backup-$(shell date +%Y%m%d).tar.gz api/static/assets/

# Restore audio files
restore-audio:
	@echo "Restoring audio files..."
	@read -p "Enter backup file name: " backup_file; \
	tar -xzf $$backup_file -C .

# Update dependencies
update-deps:
	@echo "Updating dependencies..."
	pip install --upgrade -r requirements.txt

# Format code
format:
	@echo "Formatting code..."
	black api/
	autopep8 --in-place --recursive api/

# Lint code
lint:
	@echo "Linting code..."
	flake8 api/
	pylint api/

# Security check
security:
	@echo "Running security checks..."
	safety check
	bandit -r api/

# Performance test
perf-test:
	@echo "Running performance tests..."
	ab -n 1000 -c 10 http://localhost:5000/

# Database (if needed in future)
db-init:
	@echo "Initializing database..."
	# Add database initialization commands here

db-migrate:
	@echo "Running database migrations..."
	# Add migration commands here

# Help for specific commands
help-install:
	@echo "install: Install Python dependencies and Vercel CLI"

help-dev:
	@echo "dev: Start development server with Vercel"
	@echo "dev-flask: Start Flask development server directly"

help-docker:
	@echo "docker-build: Build Docker image"
	@echo "docker-run: Run application with Docker"
	@echo "docker-stop: Stop Docker containers"

help-deploy:
	@echo "deploy: Deploy to Vercel production"
	@echo "dev-prod: Start production-like environment locally" 