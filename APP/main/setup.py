def create_dbs():
    from manage import db
    from APP.models import User, Categories, Pitches, Votes, Comments

    print("Creating The Data Base")
    db.create_all()
