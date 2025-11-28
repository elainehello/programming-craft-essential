/# PostgreSQL Database Setup

## Starting the Database Container

Run this command in the **root directory** of the project (where `docker-compose.yml` is located):

```bash
docker compose up -d
```

The `-d` flag runs the PostgreSQL container in **detached mode** (background), which means:

- The container runs independently without blocking your terminal
- You can continue using your terminal for other commands
- The database remains running until explicitly stopped
- Perfect for development workflow as it keeps the database available

## Managing the Container

```bash
# Check if container is running
docker compose ps

# View container logs
docker compose logs db

# Stop the specific container
docker stop postgres-dev-moviesdb

# Stop the container using compose
docker compose down

# Stop and remove all data (careful!)
docker compose down -v
```
