from config import db,app
from models import *
from auth.views import auth_bp


with app.app_context():
    db.create_all()
    if not User.query.filter(User.username == 'admin').first():
        user = User(
            username='admin',
            password='1234',
        )
        db.session.add(user)
        db.session.commit()


@app.route('/')
def hello():
    return '<h1>Pag. inicial, links a register y login</h1>'



app.register_blueprint(auth_bp, url_prefix='/auth')
