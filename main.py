from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

import json

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-real-secret-key'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



with app.app_context():
    with open('static/testimonials.json') as f:
        testimonials = json.load(f)['testimonials']

@app.route("/discover_opportunities", methods=['GET'])
def discover():
    # extract data from JSON
    with open('static/opportunities.json') as f:
        items = json.load(f)['opportunities']
    # pagination setup
    location = request.args.get('location', default=None, type=str)
    if location and location != "" and location != "Filter Location":
        items = [x for x in items if location in x['location']]

    search = request.args.get('search', default=None, type=str)
    if search and search != "":
        items = [x for x in items if
                 search in x['description'] or search in x['opportunity_name'] or search in x['org_name']]

    cause = request.args.get('cause', default=None, type=str)
    if cause and cause != "":
        items = [x for x in items if cause in x['cause']]

    time_commitment = request.args.get('time_commitment', default=None, type=str)

    if time_commitment and time_commitment != "":
        if time_commitment == "full-day":
            time_commitment_val = "Full Day"
        elif time_commitment == "half-day":
            time_commitment_val = "Half Day"
        else:
            time_commitment_val = "Less than 2 hours"
        items = [x for x in items if time_commitment_val in x['time_commitment']]

    duration = request.args.get('duration', default=None, type=str)
    if duration and duration != "":
        items = [x for x in items if duration in x['duration']]

    page = int(request.args.get('page', 1))
    per_page = 5
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    # create list of items for current page
    current_items = items[start_idx:end_idx]

    # render template with current items and pagination info
    if len(items) % per_page == 0:
        number_of_pages = int(len(items) / per_page)
    else:
        number_of_pages = int(len(items) / per_page) + 1

    page_range = [x for x in range(1, number_of_pages + 1)]
    return render_template("discover_opportunities.html", opportunities=current_items, page=page, per_page=per_page,
                           num_pages=number_of_pages, page_range=page_range)


@app.route("/")
def index():
    return render_template("index.html", testimonials=testimonials)


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop("logged_in", None)
    session.pop("email", None)
    return render_template("index.html", message="Logged out", testimonials=testimonials)


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/login_action', methods=['POST'])
def login_action():
    email = request.form.get('login-email-1', None)
    if not email:
        email = request.form.get('login-email-2', None)
    session["email"] = email
    session["logged_in"] = True
    return render_template("index.html", message="Logged In!", testimonials=testimonials)


@app.route('/signup_action', methods=['POST'])
def signup_action():
    email = request.form.get('signup-email', None)
    if not email:
        email = request.form['signup2-email']
    session["email"] = email
    session["logged_in"] = True
    return render_template("index.html", message="Signed Up!", testimonials=testimonials)

@app.route('/signup_2')
def signup_2():
    return render_template("sign_up_questions.html", message="Logged In!", testimonials=testimonials)


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
