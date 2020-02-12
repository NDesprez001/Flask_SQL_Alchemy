from models import db, Jobs

def ex_run():
    db.session.add(Jobs(
        job_name = "Food Runner",
        job_place = "BigEats Resturaunt",
        job_pay = "$30 per hour"
    ))
    db.session.add(Jobs(
        job_name = "Pro Sleeping",
        job_place = "Insomni.co",
        job_pay = "$80 per hour"
    ))
    db.session.commit()
    return 'Almost there'