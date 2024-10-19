import os
from dotenv import load_dotenv
import connexion
from src.database.db import Base, engine
# from src.auth_handlers.token_manager import basic_auth, bearer_auth
from flask_jwt_extended import JWTManager


load_dotenv()


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Initialized the db")


app = connexion.App(__name__, specification_dir='apisvc/openApi/')
app.add_api('openapi.yaml')
app.app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app.app)
