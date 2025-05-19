# FastAPI + Vite + React Weird Salads

This folder contains a FastAPI backend with a Vite+React frontend as a starting point.

To immediately start running:
1. Start up the docker compose stack. The frontend will be available at [http://localhost:5173/](http://localhost:5173/).
2. Any changes in the frontend or backend code should be picked up by the containers automatically.

```sh
docker compose run --build backend alembic upgrade head
docker compose up --watch --build
# Go to http://localhost:5173/
```

# Notes

- If you want to swap in a different frontend then feel free to do so, the Vite + React frontend is an example.
- If you want to use a Javascript or Typescript backend consider using the [vite-react-express](../vite-react-express/) example instead.
- See the [backend README.md](./backend/README.md) and the [frontend README.md](./frontend/README.md) for further notes.

# Before Submitting

It's recommended you reset and test your solution from scratch before submitting. The easiest path is probably via Docker:
```sh
# Delete all the application data
docker compose down --volumes
# Re-run the migrations from scratch
docker compose run --build backend alembic upgrade head
# Start the application
docker compose up --watch --build
# Check it works correctly
```
