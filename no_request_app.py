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

# We can add a second route, but note that the first route applies first
# If we load the site localhost:8000/1
#
# It will call index with the name '1'
#
# This route is only called when there are /-separated components or uri
# 
# Note also that the route does not do any type-conversion, so even though we are passing ints, they are handled as strings
# Accordingly, to make the add function work as expected, we need to do type conversion
@app.route('/<num1>/<num2>')
def add(num1, num2): # note that the parameter names here must match the names in the wrapper
   
    try:
        num1_int = int(num1)
        num2_int = int(num2)
    except ValueError:
        return "This would be better if you used numbers, but we can concatenate strings:\n{} + {} = {}".format(num1, num2, num1 + num2)
    else:
        return "{} + {} = {}".format(num1, num2, num1_int + num2_int)

# This works similarly to the add function, but we move the type checking into the route instead of the view
# Note that the route only matches if the url components can be validated as the specified type.
# Accordingly, if there isn't another route that can handle a url structured `/mult/x/y` where x or y are not ints
# Then the server will return a 404
#
# Note also that there can't be a gap between the type signature `int:` and the variable name `num1`
@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1, num2):
    return "{} x {} = {}".format(num1, num2, num1 * num2)

@app.route('/num/check/<float:num>')
@app.route('/num/check/<int:num>')
def numcheck(num):
    num_type = None
    if type(num) == int:
        num_type = 'int'
    elif type(num) == float:
        num_type = 'float'
    else:
        num_type = "unknown type: {}".format(type(num))
    return "route determined that {} is a number, specifically a {}.".format(num, num_type)


# run the app
# `debug=True`: automatically restart the server if there is an error
# `port=8000`: listen on port 8000 (a common port for web servers)
# `host='0.0.0.0': listen on all addresses that can reach this app
app.run(debug=True, port=8000, host='0.0.0.0')


