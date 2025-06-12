## Project Directory Stucture


  ```
project/
├── run.py (Starting point of the app)
└── package/
    ├── __init__.py  ( Creates and configures the Flask app , If you're using a database like SQLAlchemy, you’d initialize it here too.)
    ├── routes.py    ( Contains all your route Definitions)
    ├── models.py    ( Define your database models )
    ├── instance/
        |___Database.db  ( auto-created by SQLAlchemy)
    ├── templates/
    │   └── base.html
    └── static/
        ├── assets/
        ├── js/
        └── css/

      
  ```