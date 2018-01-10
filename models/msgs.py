from db import db

class MsgModel(db.Model):
    __tablename__ = 'msgs'
    mid = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String)

    def __init__(self, mid,  msg):
        self.mid = mid
        self.msg = msg

    def json(self):
        return {'mid': self.mid, 'msg': self.msg}

    @classmethod
    def find_by_mid(cls, mid):
        return cls.query.filter_by(mid=mid).first() #SELECT * from __tablename__(ie items) WHERE mid=mid LIMIT 1
                                                            #This is also returning a MsgModel object that has self.mid and self.msg
    #method for both PUT and POST
    def save_to_db(self):
        db.session.add(self) #session is the collection of objects we can write to the database
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self) #delete the self object
        db.session.commit()
