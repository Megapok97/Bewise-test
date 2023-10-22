# Bewise-test

### Create file `.env`  
```
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=database_name
POSTGRES_PORT=5432
POSTGRES_HOST=postgres
```

### Build and run the Docker containers
```
docker-compose up -d --build
```

### Open swagger
```
localhost:8080/docs
```

### Stop the Docker containers
```
docker-compose down
```