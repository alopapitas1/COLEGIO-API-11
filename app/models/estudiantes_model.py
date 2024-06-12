from app.database import db

class Estudiante(db.Model):
    __tablename__="estudiantes"
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50),nullable=False)
    edad=db.Column(db.Integer,nullable=False)
    peso=db.Column(db.Float(), nullable=False)
    bueno=db.Column(db.Boolean, nullable=False)
    
    def __init__(self, nombre,edad,peso,bueno):
        self.nombre=nombre
        self.edad=edad
        self.peso=peso
        self.bueno=bueno
        
    def update(self,nombre=None,edad=None,peso=None,bueno=None):
        if nombre is not None:
            self.nombre=nombre
        if edad is not None:
            self.edad=edad
        if peso is not None:
            self.peso=peso
        if bueno is not None:
            self.bueno=bueno
        db.session.commit()
        
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Estudiante.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Estudiante.query.get(id)
    
    