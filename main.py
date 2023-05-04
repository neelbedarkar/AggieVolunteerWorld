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

    remote = request.args.get('remote', default=None, type=str)
    if remote and remote != "":
        remote = 1 if remote == "on" else 0
        print(remote)
        items = [x for x in items if remote == x['remote']]

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


@app.route('/logout', methods=['GET'])
def logout():
    location = request.args.get('forward', default=None, type=str)
    session.pop("username", None)
    session.pop("logged_in", None)
    session.pop("email", None)
    if location:
        return redirect(url_for('login'))
    return render_template("index.html", message="Logged out", testimonials=testimonials)


@app.route('/help')
def help():
    return render_template("help.html")


@app.route('/login_action', methods=['POST'])
def login_action():
    if "signup" not in session or not session["signup"]:
        return render_template("login.html", message="You must sign up first")
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
    with open('static/orgs.json') as f:
        orgs = json.load(f)['organizations']
    post_opportunities = request.form.get('post-opportunities')
    post_opportunities2 = request.form.get('post-opportunities2')
    if post_opportunities or post_opportunities2:
        session['type'] = "org"
        return render_template('sign_up_questions_both.html', orgs=orgs)
    else:
        session['type'] = "vol"
        return render_template('sign_up_questions_volunteer.html', orgs=orgs)



@app.route('/signup_2')
def signup_2():
    with open('static/orgs.json') as f:
        orgs = json.load(f)['organizations']
    return render_template("sign_up_questions_both.html", orgs=orgs)


@app.route('/submit_profile_all', methods=['POST'])
def submit_profile_all():
    data = request.form.to_dict()
    if 'first-name' in data and 'last-name' in data:
        session['first_name'] = data['first-name']
        session['last_name'] = data['last-name']
    if 'volunteer-experience' in data and 'type' in session and session['type']=='vol':
        print(data)
    session["logged_in"] = True
    session["signup"] = True
    return 'Success'


@app.route('/set_org', methods=['POST'])
def set_org():
    org_id = request.form.get('org_id')
    print(org_id)
    with open('static/orgs.json') as f:
        orgs = json.load(f)['organizations']
    session['org'] = orgs[int(org_id)]
    session["logged_in"] = True
    session["signup"] = True
    return 'Org ID received: ' + org_id

# "org_id": "1",
#     "org_name": "Ocean Conservancy",
#     "org_city": "Galveston",
#     "org_leader": "Jane Doe",
#     "org_logo_path": "/static/images/logo1.png",
#     "org_description": "Ocean Conservancy is dedicated to protecting the ocean and its inhabitants. We organize beach cleanups, advocate for sustainable fishing practices, and promote ocean conservation worldwide.",
#     "org_leader_email": "jane.doe@oceanconservancy.org"

@app.route('/submit_org_all', methods=['POST'])
def submit_org_all():
    org_info= {"org_name":request.form['input-org-name'],
    "org_city":request.form['input-org-city'],
    "org_leader": session['first_name'] + " " + session['last_name'],
    "org_logo_path" : "/static/images/logo10.png",
    "org_description":  request.form['input-org-description']}
    input_org_state = request.form['input-org-state']
    session['org'] = org_info
    print(org_info)
    session["signup"] = True
    session["logged_in"] = True
    return "Success"


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return render_template("404.html")


@app.route('/post_opportunities')
def post_opp():
    if "signup" not in session or not session["signup"]:
        return render_template("login.html", message="You must sign up first")
    if 'logged_in' not in session or not session['logged_in']:
        return render_template("login.html", message="You must sign up/login first")
    if 'type' not in session:
        return render_template("login.html", message="You must sign up first")
    elif session['type'] != "org":
        return render_template("post_opp_disallow.html")
    else:
        return render_template("post_opp.html")


@app.route('/post_opp_submit', methods=['POST'])
def post_opp_submit():
    form_data = request.form.to_dict()
    print(form_data)
    return "Success"



if __name__ == '__main__':
    app.run(debug=True)
