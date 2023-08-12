from app.Database import db,BaseModelMixin

class Users(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    roll_id= db.Colum(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    def __init__(self, first_name, email, roll_id):
        self.first_name = first_name
        self.email = email
        self.roll_id = roll_id

    def __repr__(self):
        return f'User({self.email})'
    
    @classmethod
    def find_by_email(cls,email): #CLS hace referencia a Users
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_roll_id(cls, roll_id):
        return cls.query.filter_by(roll_id=roll_id).first()