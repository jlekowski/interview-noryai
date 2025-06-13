# Running the app
Go to FastAPI starter folder
```sh
cd fastapi-vite-react
```
Build containers
```sh
docker compose run --build backend alembic upgrade head
```
Run the application (sample data provided for `APP_LOCATION_ID=1` env var)
```sh
APP_LOCATION_ID=1 docker compose up --watch --build
```

# Use the application
* Open http://localhost:5173/ in a browser
* Select a staff member (any)
* Select an item to be sold (with the sample data only `Radiohead` is available).
* When clicked, data refreshes
  * `Radiohead` is not available (one more would be available if ingredient `208` for location `1` in `stock` table is increased by at least `0.01`)


# Resetting the stock
When the container is running, this command recreates `stock` table (`stock_data.csv` can be updated to get different stock)
```sh
docker exec -t -i fastapi-vite-react-backend-1 uv run alembic downgrade -2
docker exec -t -i fastapi-vite-react-backend-1 uv run alembic upgrade head
```

# AI tools used
**ChatGPT**, mainly for the sample data from CSV.
I hadn't worked with `SQLAlchemy` before, so that was the quickest way to have a code using this ORM.

# Tech chosen
I used `FastAPI` because it felt interesting and challenging. I didn't feel strong with any of the startpoints, and I didn't want to spend time on PHP as I wouldn't have learned anything.

I used Postgres to follow the startpoint stack (it would probably be my first choice anyway).

# Functionality chosen
I focused on the "Sell items" requirement. This is something staff can use from day one. They can see what can be sold and what not.
Next would be "Accept deliveries", as it currently bases on the initial data input.

I ignored for now due to time constraints:
* validation (only basic location_id check is performed, and not even everywhere)
* modifiers (normally I'd ask a PM how important this is)
* staff role
* Better UI/UX (finding items, showing "logged in" staff, number of items available, etc.)

With more time I would:
* make the code more consistent
* log stock changes (time and staff)
* set proper DB indexes and constraints
* unignore modifiers (I'd ask for an explanation how important they are)
