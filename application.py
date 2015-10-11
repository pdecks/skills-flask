from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def show_app_form():
    """Show the application form"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def show_app_response():
    """Show the application response"""
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job_title = request.form.get("job-title")

    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           job_title=job_title)

if __name__ == "__main__":
    app.run(debug=True)
