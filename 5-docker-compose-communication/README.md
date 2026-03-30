# Module 5 - Docker Compose: Inter-Service Communication

**Goal**: Learn how services communicate in Docker Compose using DNS service discovery and networks.

## Background

Docker Compose creates a default network for all services. Each service can reach other services by their **service name** (e.g., `redis`). Docker provides built-in DNS that automatically resolves service names to container IPs.

## Steps

1. Examine the `docker-compose.yml` file to see how networks are defined:
   - `frontend` network: used by the web service
   - `backend` network: used by both web and redis services

2. Build and start the services:
   ```shell
   docker compose up --build -d
   ```

3. Verify both services are running:
   ```shell
   docker compose ps
   ```

4. **Test connectivity to Redis** from the web container:
   ```shell
   docker compose exec web python test_connection.py
   ```

5. **Inspect the networks** Docker Compose created:
   ```shell
   docker network ls
   docker network inspect 5-docker-compose-communication_frontend
   docker network inspect 5-docker-compose-communication_backend
   ```

6. **Verify DNS resolution** - the service name `redis` resolves to the Redis container IP:
   ```shell
   docker compose exec web nslookup redis
   ```

7. **Try a connection from Redis to web** (this will fail because Redis is only on `backend` network):
   ```shell
   docker compose exec redis nslookup web
   ```

8. **Cleanup**:
   ```shell
   docker compose down
   ```

## Key Concepts

- **Service Discovery**: Containers can reach each other by service name (DNS)
- **Network Isolation**: Services on different networks cannot communicate
- **Bridge Networks**: Docker Compose creates bridge networks by default
- **Internal Access**: Services can communicate using internal ports without exposing them to the host

## Bonus

Try modifying `docker-compose.yml` to add a new service `logger` on the `backend` network only. Can the logger communicate with both `web` and `redis`? Can it communicate with the host machine?
