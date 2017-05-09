"""Models and database functions for Kate's project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions

class Species(db.Model):
    """Species of birds."""

    __tablename__ = "species"

    taxonomic_num = db.Column(db.String(20), nullable=False, primary_key=True, unique=True)
    category = db.Column(db.String(64), nullable=True)
    common_name = db.Column(db.String(100), nullable=True)
    scientific_name = db.Column(db.String(100), nullable=True)

    def __repr__(self):

        return "<Common name=%s Taxanomic number=%s global_id=%s>" % (self.common_name, self.taxonomic_num, self.global_id)


class SamplingEvent(db.Model):
    """Checklist of bird observation."""

    __tablename__ = "sampling_event"

    global_id = db.Column(db.Integer, Foreign_key=)
    sampling_event_id = db.Column(db.Integer, primary_key=True, unique=True)

    def __repr__(self):

        return "<County=%s latitude=%d, longitude=%d>" % (self.county, self.latitude, self.longitude)


class Observation(db.Model):
    """Bird sighting observation."""

    __tablename__ = "observation"

    global_id = db.Column(db.Integer, primary_key=True, unique=True)
    sampling_event_id = db.Column(db.Integer, db.ForeignKey('sampling_event.sampling_event_id'), nullable=False)
    observation_date = db.Column(db.DateTime, nullable=False)
    taxonomic_num = db.Column(db.String(20), db.ForeignKey('species.taxonomic_num') nullable=True)
    observation_count = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    all_species_report = db.Column(db.String(10), nullable=False)

    species = db.relationship("Species")

    sampling_event = db.relationship("SamplingEvent")

    def __repr__(self):

        return "<Global id=%s Date=%s>" % (self.global_id, self.observation_date)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ebird_data'
    app.donfig['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."