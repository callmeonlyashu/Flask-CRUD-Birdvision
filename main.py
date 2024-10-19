import os
from dotenv import load_dotenv
import connexion
from src.database.db import Base, engine
from flask_jwt_extended import JWTManager
import logging

log = logging.getLogger(__name__)
from src.logging.logging_config import setup_logging

# Initialize logging
setup_logging()

load_dotenv()


def init_db():
    Base.metadata.create_all(bind=engine)
    log.info("Initialized the db")


log.info("Initializing app")

app = connexion.App(__name__, specification_dir='apisvc/openApi/')
app.add_api('openapi.yaml')
app.app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app.app)
