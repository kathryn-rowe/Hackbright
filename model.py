from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""

    game1 = Game(name="Twilight Struggle", description="A long game about the Cold War")
    game2 = Game(name="Teslestrations", description="A game about drawing and describing the drawing")
    game3 = Game(name="Duck Duck Goose", description="A child's game about water fowl")

    db.session.add_all([game1, game2, game3])
    db.session.commit()


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
 