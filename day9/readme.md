## Database migration from SQLite to MySQL
#### But why ?

* reason is  On platforms like Render, your deployed app runs on temporary storage... So Any changes made to the DB file during runtime will be lost when the app restarts or scales.

Thats Why  we had this issue earlier : when we make a new commit DB data is lost

* Solution : MySQL is server-based → Data persists and supports many users at once.


## Step 1: Create a Free PostgreSQL Database on Render
Wait a few seconds — Render will give you a DATABASE URL that looks like:
postgres://username:password@dpg-xxxxx/renderdb

## Step 2: Update Your Flask App to Use the PostgreSQL URL
Create a .env file in the root directory inside with `DATABASE_URL=postgres://username:password@dpg-xxxxx/renderdb`

Install required packages:`pip install python-dotenv psycopg2-binary`

Update your app.py:
```
    load_dotenv()

    uri = os.getenv("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://")  # Required fix

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

```


## step3 : Migrate Old Data from SQLite to PostgreSQL (opt)

This is a one-time migration process:

* Export all rows from your SQLite database
* Connect to the PostgreSQL database
* Insert the rows into the PostgreSQL database

(refer data_migration.py)



