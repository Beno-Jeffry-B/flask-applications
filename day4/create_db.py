from app import app , db 

def create_database():
    with app.app_context():
        db.create_all()



create_database()