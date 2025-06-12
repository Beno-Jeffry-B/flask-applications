## Database migration from SQLite to MySQL
#### But why ?

* reason is  On platforms like Render, your deployed app runs on temporary storage... So Any changes made to the DB file during runtime will be lost when the app restarts or scales.

Thats Why  we had this issue earlier : when we make a new commit DB data is lost

* Solution : MySQL is server-based → Data persists and supports many users at once.