"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from sqlalchemy import distinct

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# The returned value of this query is <class 'flask_sqlalchemy.BaseQuery'>, which means
# it is a saved query without results. I assigned the variable "ford" to this query
# and typed "print ford" into the console. The result was a SQL "looking" query (SELECT
# brands.brand_id AS brands_brand_id etc.). If I wanted results of the query, I would need
# to include a fetching word at the end, including .all(), .first(), etc.



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table binds a relationship between tables during a many-to-many join. Unlike a
# middle table, it does not have any real-world values. The name of the table is usually a
# mash-up of the names of the tables it is linking together, and binds two or more tables together
# based on their primary keys.



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').one()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = db.session.query(Model).distinct(Model.name).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = db.session.query(Brand).filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get any model whose brand_id is not "for."
q8 = db.session.query(Model).filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model = db.session.query(Model.name, Brand.name, Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for name, bname, headquarters in model:
        print "Model name: %s \n Brand name: %s \n Brand headquarters: %s" % (name, bname, headquarters)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    model = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()

    for model_name, model_name, model_year in model:
        print "Brand name: %s \n Model name: %s \n Model year: %s" % (model_name, model_name, model_year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_obj = db.session.query(Brand).filter(Brand.name.like(('%{}%').format(mystr))).all()

    if len(brand_obj) == 0:
        print "This string is not in the database. Please check your capitalization."
    else:
        return brand_obj


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    model_obj = db.session.query(Model).filter(Model.year > start_year, Model.year < end_year).all()

    if len(model_obj) == 0:
        print "Please enter a year between 1909 and 1964"
    else:
        return model_obj
