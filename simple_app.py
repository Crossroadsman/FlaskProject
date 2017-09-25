from flask import Flask

from flask import request # global object

# Create a new Flask instance (passing the current namespace to the Flask initializer)
app = Flask(__name__)

# Create a route
# Note this uses 'pie syntax' to implement a decorator
# A decorator is a way of wrapping a function (here `app.route('/')`) around another function
# (here `index()`) in order to modify the latter's behaviour.
# It replaces the latter function with the result of calling the former function and passing the latter function to it.
@app.route('/')
def index(name='Default Person'):
    
    # request is a global object and represents the query string (if any) included in the url
    # the components of the query string are in a dictionary-like structure
    # and we can access these using the .get(key, default=None) method
    # 
    # Here, if there is a 'name' argument, we take that, otherwise we get the existing name variable
    # and put that into the name variable.
    #
    # So if we access the page 127.0.0.1:localhost without a query string, we'll get 'Hello Default Person'
    # If we access the page 127.0.0.1:localhost/?name=SpecialPerson, we'll get 'Hello SpecialPerson'
    name = request.args.get('name', name)
    return "Hello {}".format(name)

# run the app
# `debug=True`: automatically restart the server if there is an error
# `port=8000`: listen on port 8000 (a common port for web servers)
# `host='0.0.0.0': listen on all addresses that can reach this app
app.run(debug=True, port=8000, host='0.0.0.0')


