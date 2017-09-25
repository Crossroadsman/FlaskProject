from flask import Flask

# Create a new Flask instance (passing the current namespace to the Flask initializer)
app = Flask(__name__)

# Create a route
# Note this uses 'pie syntax' to implement a decorator
# A decorator is a way of wrapping a function (here `app.route('/')`) around another function
# (here `index()`) in order to modify the latter's behaviour.
# It replaces the latter function with the result of calling the former function and passing the latter function to it.
@app.route('/')
def index():
    return "Hello, world"

# run the app
# `debug=True`: automatically restart the server if there is an error
# `port=8000`: listen on port 8000 (a common port for web servers)
# `host='0.0.0.0': listen on all addresses that can reach this app
app.run(debug=True, port=8000, host='0.0.0.0')


