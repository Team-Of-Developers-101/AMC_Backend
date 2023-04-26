from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool


db = SQLAlchemy(
    engine_options={
        "pool_pre_ping": True,  # re-connects if connection is not alive
        "pool_size": 10,  # no. of conns that will be persisted in the pool
        "poolclass": QueuePool
    }
)


def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    with app.app_context():
        db.create_all()
