import connexion
from src.database.db import Base, engine


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Initialized the db")


app = connexion.App(__name__, specification_dir='apisvc/openApi/')
app.add_api('openapi.yaml')


if __name__ == '__main__':
    init_db()
    app.run()
