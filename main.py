from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route("/discover_opportunities")
def discover():
    # extract data from JSON
    with open('static/opportunities.json') as f:
        items = json.load(f)['opportunities']
    # pagination setup
    page = int(request.args.get('page', 1))
    per_page = 5
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    # create list of items for current page
    current_items = items[start_idx:end_idx]

    # render template with current items and pagination info
    if len(items) % per_page == 0:
        number_of_pages = int(len(items)/per_page)
    else:
        number_of_pages = int(len(items)/per_page) + 1

    page_range = [x for x in range(1, number_of_pages + 1)]
    return render_template("discover_opportunities.html", opportunities=current_items, page=page, per_page=per_page, num_pages=number_of_pages, page_range=page_range)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
