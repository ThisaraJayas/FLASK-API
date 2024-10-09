from api import app, db #api other file

with app.app_context():
    db.create_all()  #this will create db