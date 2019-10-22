from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class case(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    case_name = db.Column(db.String(64))
    case_steps = db.Column(db.String(64))
    case_type = db.Column(db.String(64))
    case_id = db.Column(db.String(64))
    default_result = db.Column(db.String(64),default=True)
    __tablename__ = 'case'
    def __init__(self, title):
        self.case_name = title
    def save(self):
        db.session.add(self)
        db.session.commit()



class case_list(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    case_name = db.Column(db.String(64))
    case_steps = db.Column(db.String(64))
    case_type = db.Column(db.String(64))
    case_id = db.Column(db.String(64))
    default_result = db.Column(db.String(64),default=True)
    __tablename__ = 'case_list'
    def __init__(self, case_type):
        self.case_type = case_type
    def save(self):
        db.session.add(self)
        db.session.commit()