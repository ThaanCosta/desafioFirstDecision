from flask import request, jsonify, current_app, Blueprint
from app import app, db
from app.models import DadosEscola

main = Blueprint('main', __name__)

@main.route('/dados_escola', methods=['GET'])
def get_all_dados_escola():
    dados = DadosEscola.query.all()
    return jsonify([dado.to_dict() for dado in dados]), 200

@main.route('/dados_escola/<int:co_municipio_esc>', methods=['GET'])
def get_dados_escola(co_municipio_esc):
    dado = DadosEscola.query.get_or_404(co_municipio_esc)
    return jsonify(dado.to_dict()), 200

@main.route('/dados_escola', methods=['POST'])
def create_dados_escola():
    data = request.get_json()
    try:
        novo_dado = DadosEscola(
            CO_MUNICIPIO_ESC=data['CO_MUNICIPIO_ESC'],
            NO_MUNICIPIO_ESC=data['NO_MUNICIPIO_ESC'],
            CO_UF_ESC=data['CO_UF_ESC'],
            SG_UF_ESC=data['SG_UF_ESC'],
            TP_DEPENDENCIA_ADM_ESC=data['TP_DEPENDENCIA_ADM_ESC'],
            TP_LOCALIZACAO_ESC=data['TP_LOCALIZACAO_ESC'],
            TP_SIT_FUNC_ESC=data['TP_SIT_FUNC_ESC']
        )
        db.session.add(novo_dado)
        db.session.commit()
        return jsonify(novo_dado.to_dict()), 201
    except Exception as e:
        current_app.logger.error(f"Error creating DadosEscola: {e}")
        db.session.rollback()
        return jsonify({"error": "Erro ao criar registro"}), 400

@main.route('/dados_escola/<int:co_municipio_esc>', methods=['PUT'])
def update_dados_escola(co_municipio_esc):
    data = request.get_json()
    dado = DadosEscola.query.get_or_404(co_municipio_esc)
    try:
        dado.NO_MUNICIPIO_ESC = data.get('NO_MUNICIPIO_ESC', dado.NO_MUNICIPIO_ESC)
        dado.CO_UF_ESC = data.get('CO_UF_ESC', dado.CO_UF_ESC)
        dado.SG_UF_ESC = data.get('SG_UF_ESC', dado.SG_UF_ESC)
        dado.TP_DEPENDENCIA_ADM_ESC = data.get('TP_DEPENDENCIA_ADM_ESC', dado.TP_DEPENDENCIA_ADM_ESC)
        dado.TP_LOCALIZACAO_ESC = data.get('TP_LOCALIZACAO_ESC', dado.TP_LOCALIZACAO_ESC)
        dado.TP_SIT_FUNC_ESC = data.get('TP_SIT_FUNC_ESC', dado.TP_SIT_FUNC_ESC)
        
        db.session.commit()
        return jsonify(dado.to_dict()), 200
    except Exception as e:
        current_app.logger.error(f"Error updating DadosEscola: {e}")
        db.session.rollback()
        return jsonify({"error": "Erro ao atualizar registro"}), 400

@main.route('/dados_escola/<int:co_municipio_esc>', methods=['DELETE'])
def delete_dados_escola(co_municipio_esc):
    dado = DadosEscola.query.get_or_404(co_municipio_esc)
    try:
        db.session.delete(dado)
        db.session.commit()
        return jsonify({"message": "Registro deletado com sucesso"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting DadosEscola: {e}")
        db.session.rollback()
        return jsonify({"error": "Erro ao deletar registro"}), 400

def init_app(app):
    app.register_blueprint(main)
