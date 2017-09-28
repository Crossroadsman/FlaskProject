import json

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

    form_items = flask.request.form.items() # this object is not exactly a dictionary, it is 'immutablemultidict'
    form_items_dict = dict(form_items)
    name = form_items_dict['name']

    if name == None:
        print("You forgot to add a name")
    else:
        print("{} is a nice name. I like it.".format(name))

    # Previously we created the response in the return statement
    # But we need the response to send the cookie, so we need to move
    # the response creation out of the return statement
    #
    # `redirect` is used to redirect to another url
    # in this case, the url that is derived by following the `index` function
    response = flask.make_response( flask.redirect( flask.url_for('index') ) )

    # make the cookie:
    # `.dumps(x)` ('dumps' means dump a json-formatted string) where x is a valid python object (dict/tuple(and list)/str/int/float/True/False/None)
    cookie_data = json.dumps(form_items_dict)

    ## (the first argument is the cookie name
    #  the second argument is the json object whose data to store in the cookie)
    response.set_cookie('avatar', cookie_data )

    return response

app.run(debug=True, host='0.0.0.0', port=8000)
