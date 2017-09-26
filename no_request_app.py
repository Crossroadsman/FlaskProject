from flask import Flask

# In this version we are not using requests because we are not handling a query string.
# Instead we are using Flask to process the text trailing the `/` to determine what should
# be put into the response.

# Create a new Flask instance (passing the current namespace to the Flask initializer)
app = Flask(__name__)

# Create a route
# Note this uses 'pie syntax' to implement a decorator
# A decorator is a way of wrapping a function (here `app.route('/')`) around another function
# (here `index()`) in order to modify the latter's behaviour.
# It replaces the latter function with the result of calling the former function and passing the latter function to it.
#
# We can have multiple decorators for a single function.
# Flask is designed to be able to handle multiple routes (using multiple decorators) with a single view
#
# In the second decorator we have created a capture group, called `name`.
# What this means is that Flask will take whatever the string after the `/` is and put it into the `name` variable.
@app.route('/')
@app.route('/<name>')
def index(name='Default Person'):
    
    # In this version, if the provided uri is just `/` then index gets called without a specified name value
    # and gets the default one from the function signature.
    #
    # If, instead, the uri has some value after the `/` then that value gets put into the name local variable which is passed into
    # the index function that the route is wrapping.
    return "Hello {}.".format(name)

# run the app
# `debug=True`: automatically restart the server if there is an error
# `port=8000`: listen on port 8000 (a common port for web servers)
# `host='0.0.0.0': listen on all addresses that can reach this app
app.run(debug=True, port=8000, host='0.0.0.0')


