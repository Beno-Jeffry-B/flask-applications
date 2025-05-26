## DAY 4

#### Data Bases and Models

Here, we are gonna learn SQLAlchemy

* SQLAlchemy is NOT a database.
* It is a Python toolkit and Object Relational Mapper (ORM) that allows you to work with databases using Python code instead of raw SQL.

     instead of :
    > `SELECT * FROM users WHERE age > 18;`
    
     we write this:
    > `session.query(User).filter(User.age > 18).all()`


##### But why ?
 * SQLAlchemy is database-independent. 
 * You can write your Python code once using SQLAlchemy, and switch between databases without changing your application logic.

#### SQLite3

##### we use Sqlite3 in the projects reason is because:

* SQLite is a lightweight, file-based relational database. Unlike MySQL or PostgreSQL, it doesn't need a server running in the background.

* Normally we devople and test locally using Sqlite because before production we have less traffic so , Great for local development .

* later we switch to MySQL/PostgreSQL for production without changing much code.

