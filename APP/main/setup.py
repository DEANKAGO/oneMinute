def create_dbs():
    from manage import db
    from APP.models import User

    print("Creating The Data Base")
    db.create_all()