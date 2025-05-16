# Base Maps Project

A mapping application with PostgreSQL/PostGIS backend and React frontend.

## Project Structure

- `/backend` - Python FastAPI backend with SQLAlchemy and PostGIS
- `/frontend` - React TypeScript frontend
- `docker-compose.yml` - Docker setup for development

## Features

- PostgreSQL database with PostGIS extension for spatial data
- FastAPI backend with SQLAlchemy ORM
- JWT authentication
- React frontend with routing
- Docker containers for development

## CRUD Endpoints

The API provides endpoints for managing:

- Features (spatial features with geometry)
- Settings
- Roles
- Users
- Layers
- Datamaps
- Networks
- Applications
- PickLists
- Datasources
- Notifications
- Usage statistics

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Setup and Run

1. Clone the repository:
   ```
   git clone <repository-url>
   cd base_maps
   ```

2. Start the development environment:
   ```
   docker-compose up -d
   ```

3. Access:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/api/docs

### Development

Design decisions and architectural choices are documented in:
- Frontend: `/frontend/prompts/design_decisions.md`
- Backend: `/backend/prompts/design_decisions.md`

## License

[MIT License](LICENSE)