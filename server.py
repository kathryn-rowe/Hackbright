from flask import Flask, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
import secret_key


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = secret_key.secret_key


@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Sends user to Application Form."""

    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", jobs=jobs)


@app.route("/application-success", methods=["POST"])
def application_success():
    """Returns a response that acknowledges their application"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    applicant = first_name + " " + last_name
    job_choice = request.form.get("open_position")
    salary_requirement = request.form.get("salary_required")

    flash("Congratulations, you've applied to work for the FBI")

    return render_template("application-response.html",
                            applicant=applicant,
                            job_choice=job_choice,
                            salary_requirement=salary_requirement)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
