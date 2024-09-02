from app import db

class DadosEscola(db.Model):
    __tablename__ = 'DadosEscola'
    
    CO_MUNICIPIO_ESC = db.Column(db.Integer, primary_key=True)
    NO_MUNICIPIO_ESC = db.Column(db.String(255))
    CO_UF_ESC = db.Column(db.Integer)
    SG_UF_ESC = db.Column(db.String(2))
    TP_DEPENDENCIA_ADM_ESC = db.Column(db.Integer)
    TP_LOCALIZACAO_ESC = db.Column(db.Integer)
    TP_SIT_FUNC_ESC = db.Column(db.Integer)
