from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    rowid = db.Column(db.Integer,primary_key=True)
    ID = db.Column(db.Integer,unique=True,nullable=False)
    name_client = db.Column(db.String(200),nullable=False)
    age = db.Column(db.Integer)
    country = db.Column(db.String(200))
    score = db.Column(db.Float)

    def __str__(self):
        return "ID: {}. Nombre: {}. Edad: {}. País: {}. Score: {}.\n".format(
            self.ID,
            self.name_client,
            self.age,
            self.country,
            self.score
        )
    def serialize(self):
        return {
            "rowid": self.rowid,
            "ID":self.ID,
            "name_client": self.name_client,
            "age": self.age,
            "country": self.country,
            "score": self.score
        }
    def create(var_ID,var_name,var_age,var_country,var_score):
        client = Client(
            ID=var_ID,
            name_client=var_name,
            age = var_age,
            country= var_country,
            score= var_score
            )
        
        return client.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self

        except:

            return False
    
