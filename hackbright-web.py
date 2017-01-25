from flask import Flask, request, render_template, redirect
from flask.ext.sqlalchemy import SQLAlchemy
import hackbright

db = SQLAlchemy()


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///melondb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

app = Flask(__name__)

connect_to_db(app)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)


@app.route("/new-student")
def new_student():
    """Sends user to page to add new student."""

    return render_template("new-student.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    github = request.form.get('github')

    QUERY = """
            INSERT INTO students (first_name, last_name, github)
            VALUES (:fname, :lname, :github)
            """

    db.session.execute(QUERY, {'fname': fname,
                               'lname': lname,
                               'github': github})

    db.session.commit()

    return render_template('student-add-confirmation.html',
                           fname=fname,
                           lname=lname,
                           github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
