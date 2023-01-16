from config import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email = db.Column(db.String(255, collation='NOCASE'))
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'))
    last_name = db.Column(db.String(100, collation='NOCASE'))
    username = db.Column(db.String(100))
    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))




# crear tablas:
# votos; listas, padrones