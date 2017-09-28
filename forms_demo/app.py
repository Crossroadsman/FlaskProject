import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

# Here we are creating a route and a method to handle a user submitting the call to action button on the index page
#
# We have dedicated a uri (`/save`) to identify this action
# Note that we are also restricting access to this view to only http POST methods
@app.route('/save', methods=['POST'])
def save():

    name = flask.request.args.get('name', None)

    if name == None:
        print("You forgot to add a name")
    else:
        print("{} is a nice name. I like it.".format(name))

    # `redirect` is used to redirect to another url
    # in this case, the url that is derived by following the `index` function
    return flask.redirect(flask.url_for('index'))

app.run(debug=True, host='0.0.0.0', port=8000)
