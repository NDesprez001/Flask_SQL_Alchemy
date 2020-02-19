from models import db, Jobs

def ex_run():
    
    db.session.commit()
    return 'Almost there'