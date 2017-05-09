"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session)
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Ratings, Movies, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    # a = jsonify([1,3])
    return render_template("homepage.html")


@app.route("/movies")
def movies_list():

    movies = Movies.query.order_by(Movies.title).all()
    return render_template("movies_list.html", movies=movies)


@app.route("/movie_info/<movie_id>")
def get_movie_info(movie_id):

    # users = User.query.all()
    #user_id = request.args.get("user_id")
    movies = Movies.query.filter(Movies.movie_id == movie_id).first()
    ratings = movies.ratings

    return render_template("movie_info.html", movies=movies, ratings=ratings)


@app.route("/users")
def user_list():

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/user_info/<user_id>")
def get_user_info(user_id):

    # users = User.query.all()
    #user_id = request.args.get("user_id")
    user = User.query.filter(User.user_id == user_id).first()
    movies = db.session.query(Ratings).filter_by(user_id=user_id).all()

    return render_template("user_info.html", user=user, movies=movies)


@app.route("/register", methods=["GET"])
def show_register_form():

    return render_template("register_form.html")


@app.route("/register", methods=["POST"])
def register_process():

    username = request.form.get("username")
    password = request.form.get("password")
    age = request.form.get("age")
    zipcode = request.form.get("zipcode")

    emails = User.query.filter(User.email == username).first()

    if emails is None:
        email = username
        new_user = User(email=email,
                        password=password,
                        age=age,
                        zipcode=zipcode)

        db.session.add(new_user)

        db.session.commit()
        user_id = new_user.user_id
        session["logged_in"] = username

        # print "We just create the user"
        flash("Thank you for registering")
    else:
        flash("You've already registered. Please log-in.")

    return redirect("/user_info/" + str(user_id))


@app.route("/login", methods=["GET"])
def show_login():

    return render_template("sign_in.html")


@app.route("/login", methods=["POST"])
def login_process():

    username = request.form.get("username")
    password = request.form.get("password")

    emails = User.query.filter(User.email == username).first()

    if emails is None:
        flash("No such email address. Please register")
        return redirect('/register')

    elif emails.password != password:
        flash("Incorrect password.")
        return redirect("/login")
    else:
        session["logged_in"] = username
        user_id = emails.user_id
        flash("Logged in.")
        return redirect("/user_info/" + str(user_id))


@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["logged_in"]
    flash("Logged out.")
    return redirect("/")

@app.route("/rating", methods=["POST"])
def rating_process():

    movie_id = request.args.get("movie_id")
    score = request.form.get("rating")
    #Use the session to find the user_id

    movie = Movies.query.filter(Movies.movie_id == movie_id).first()

    rating = Ratings(user_id=user_id,
                         movie_id=movie_id,
                         score=score)

        # We need to add to the session or it won't ever be stored
        db.session.add(rating)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)



    app.run(port=5000, host='0.0.0.0')
