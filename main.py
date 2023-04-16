from flask import Flask, render_template, request

app = Flask(__name__)

# example JSON data
json_data = {
    "opportunity_name": ["Volunteer at Animal Shelter", "Tutor High School Students", "Community Garden Helper",
                         "Food Bank Assistant", "Fundraising Event Organizer", "Beach Cleanup Crew",
                         "Hospitality Volunteer", "Disaster Relief Aid", "Senior Caregiver"],
    "time_commitment": ["Half Day", "Full Day", "Full Day", "Multiple Weeks", "Multiple Weeks", "Full Day",
                        "Multiple Weeks", "Multiple Weeks", "Multiple Weeks"],
    "org_name": ["Animal Rescue", "High School Tutoring Program", "Community Garden Association", "Regional Food Bank",
                 "Non-Profit Fundraising Group", "Ocean Conservancy", "Local Hospitality Program",
                 "Disaster Relief Organization", "Elder Care Facility"]
}


@app.route("/discover_opportunities")
def index():
    # extract data from JSON
    opportunities = json_data["opportunity_name"]
    time_commitments = json_data["time_commitment"]
    org_names = json_data["org_name"]

    # create list of dicts for each item
    items = []
    for i in range(len(opportunities)):
        items.append({
            "opportunity_name": opportunities[i],
            "time_commitment": time_commitments[i],
            "org_name": org_names[i]
        })

    # pagination setup
    page = int(request.args.get('page', 1))
    per_page = 4
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    # create list of items for current page
    current_items = items[start_idx:end_idx]

    # render template with current items and pagination info
    if len(items) % per_page == 0:
        number_of_pages = int(len(items)/per_page)
    else:
        number_of_pages = int(len(items)/per_page) + 1
    number_of_pages = 9
    page_range = [x for x in range(1, number_of_pages + 1)]
    return render_template("discover_opportunities.html", opportunities=current_items, page=page, per_page=per_page, num_pages=number_of_pages, page_range=page_range)


if __name__ == '__main__':
    app.run(debug=True)
