from models import db, Users

def run():
    db.session.add( Users(
        first_name = 'Jak',
        last_name = 'Atak',
        username = 'FiteBak',
        password = 'Protecc123',
        email = 'Conekt33@gmail.com'
    ))
    db.session.add( Users(
        first_name = 'Tom',
        last_name = 'Bradley',
        username = 'NotBrady',
        password = 'tom355',
        email = 'T.Bradley@gmail.com'
    ))
    db.session.add( Users(
        first_name = 'Micheal',
        last_name = 'Jackson',
        username = 'Mjpop',
        password = 'pop1989',
        email = 'KingOfPop@gmail.com'
    ))
    db.session.add( Users(
        first_name = 'Beth',
        last_name = 'McChair',
        username = 'Sitting246',
        password = 'lazydog36',
        email = 'LazyBeth@gmail.com'
    ))
    db.session.add( Users(
        first_name = 'Kim',
        last_name = 'Tallmen',
        username = 'Money388',
        password = 'rich4ever100',
        email = 'RichKim@gmail.com'
    )) 
    db.session.add( Users(
        first_name = 'Joanne',
        last_name = 'Scammer',
        username = 'Innocent335',
        password = 'creditcardinfo123',
        email = 'JoS@gmail.com'
    )) 
    db.session.add( Users(
        first_name = 'victor',
        last_name = 'jordan',
        username = 'jajaboo',
        password = 'sucka1232',
        email = 'victorjordan@23.com'
    ))
    db.session.commit()
    return 'seeds ran successfully'