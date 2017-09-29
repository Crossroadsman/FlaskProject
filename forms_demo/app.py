import json

import flask

from options import DEFAULTS # Note that we can import variables as well as classes




app = flask.Flask(__name__)

cookie_name = 'avatar'



def get_saved_data():
    """reads a cookie, if one is set, and then converts the json-formatted cookie data to a valid python object, which is then returned"""
    cookie_data = None
    try:
        cookie_data = flask.request.cookies.get(cookie_name)
    except:
        print("Failed to get cookie")
        print("leaving cookie_data blank")

    try:
        data = json.loads(cookie_data)
    except TypeError:
        print("Failed to convert cookie data from json string to python object")
        print("This is what the cookie data looked like:")
        print(cookie_data)
        print("making `data` an empty dict")
        data = {}
    
    return data

    

@app.route('/')
def index():
    saved_data = get_saved_data()
    context = {'saves' : saved_data}

    return flask.render_template('index.html', **context)



@app.route('/builder')
def builder():
    saved_data = get_saved_data()
    context = {'saves' : saved_data,
               'options' : DEFAULTS}
    
    return flask.render_template('builder.html', **context)



# Here we are creating a route and a method to handle a user submitting the call to action button on the index page
#
# We have dedicated a uri (`/save`) to identify this action
# Note that we are also restricting access to this view to only http POST methods
@app.route('/save', methods=['POST'])
def save():

    form_items = flask.request.form.items() # this object is not exactly a dictionary, it is 'immutablemultidict'
    form_items_dict = dict(form_items)

    existing_data = get_saved_data() # from the cookie
    existing_data.update(form_items_dict) # add/update any newer data from the form into the existing_data

    name = existing_data['name']

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
    response = flask.make_response( flask.redirect( flask.url_for('builder') ) )

    # make the cookie:
    # `.dumps(x)` ('dumps' means dump a json-formatted string) where x is a valid python object (dict/tuple(and list)/str/int/float/True/False/None)
    cookie_data = json.dumps(existing_data)


    ## (the first argument is the cookie name
    #  the second argument is the json object whose data to store in the cookie)
    response.set_cookie(cookie_name, cookie_data )

    return response

app.run(debug=True, host='0.0.0.0', port=8000)
