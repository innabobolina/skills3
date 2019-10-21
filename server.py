from flask import Flask, redirect, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# ------------------------------
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# ------------------------------
# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE
# ------------------------------
# http://0.0.0.0:5000
# ------------------------------
@app.route("/")
def index():
    """Return homepage if a user hasn't entered their name already."""

    if 'name' in session:
        return redirect("/top-melons/")
    else:
        return render_template("homepage.html")

# ------------------------------
# http://0.0.0.0:5000/top-melons/
# ------------------------------
@app.route("/top-melons/")
def top_melons():
    """Return the page displaying the most loved melons."""

    if 'name' in session:
        return render_template("top-melons.html",
                               melons=MOST_LOVED_MELONS)
    else:
        return redirect("/")
    # redirect to homepage if there's no name stored in the session

# ------------------------------
@app.route("/get-name")
def get_name():
    """Add user's name to the session and redirect to top-melons page."""

    session['name'] = request.args.get("user")
    #get user's name from the form submitted and add to the session

    return redirect("/top-melons/")

# ------------------------------
# http://0.0.0.0:5000/thank-you/
# ------------------------------
@app.route("/thank-you/")
def thank_you():

    return render_template("thank-you.html")

# ------------------------------
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
