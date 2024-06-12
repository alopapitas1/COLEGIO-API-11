from flask import jsonify,Flask
from app.controllers.user_controller import user_bp
from app.controllers.estudiante_controller import estudiante_bp
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager
from app.database import db

app=Flask(__name__)

app.config["JWT_SECRET_KEY"]="clave secreta aqui"
SWWAGER_URL="/api/docs"
API_URL="/static/swagger.json"

swagger_bp=get_swaggerui_blueprint(SWWAGER_URL,API_URL,config={"app_name":"IDS"})
app.register_blueprint(swagger_bp,url_prefix=SWWAGER_URL)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///cole.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db.init_app(app)
jwt=JWTManager(app)

app.register_blueprint(user_bp,url_prefix="/api")
app.register_blueprint(estudiante_bp,url_prefix="/api")

with app.app_context():
    db.create_all()
    
if __name__=="__main__":
    app.run(debug=True)