# README

## Set Up

Ensure you have ruby 3.4.3 installed (on Mac OS in particular, it's recommended you use rbenv) and docker running.

Start the postgres database in docker with:

```bash
docker compose up -d
```

The user and password are both postgres, the database name is `weird_salads_rails_development`, and it's listening on port 6679 (to try avoid conflict in case you have another postgres server running). In short:

```bash
postgresql://postgres:postgres@localhost:6679/weird_salads_rails_development
```

Install dependencies with:

```bash
# In the same directory as this README
bundle install --gemfile Gemfile
```

To start serving the web app, run:

```bash
bin/rails server
```

You should now be able to access the web app on http://localhost:3000, and can leave this running while you develop, as it'll autoload any changes you make.

For details on all the stuff in here, see the [rails documentation on the directory structure](https://guides.rubyonrails.org/getting_started.html#directory-structure).

## Adding models

You can generate a database migration with:

```bash
bin/rails generate model ModelName column_name:column_type
# e.g.
# bin/rails generate model Staff name:string location:integer
```

This will create a database migration in `db/migrate`, an ActiveModel model in `app/models/model_name.rb`, and tests/fixtures for the model.

You can run the migration with:

```bash
bin/rails db:migrate
# or db:rollback to undo
```

For more details on migrations, see [the docs](https://guides.rubyonrails.org/getting_started.html#creating-a-database-model).

## Placeholder view

You'll find a placeholder view using the Staff model, which serves only as an example. Feel free to delete, modify, expand, or do whatever else you like with it.

To generate a starting point for a new controller, you can run:

```ruby
bin/rails generate controller ControllerName path_name
```

See more in the [rails docs](https://guides.rubyonrails.org/getting_started.html#controllers-actions).

## What next?

Up to you! Refer back to the briefing doc.

Feel free to replace or extend this README or add a separate documentation file of your own for your notes.
