from flask import Flask

app = Flask(__name__)

def hello_world():
    return 'hello world3'

# Another way to adding the url by using add_ur_rule() function 
'''
1. '/' → the URL path (what you type in the browser).

2. 'hello' → the endpoint name (Flask’s internal reference to this route).

3. hello_world → the function that runs when someone visits that route.
'''
app.add_url_rule('/','hello',hello_world)

if __name__=='__main__':
    app.run(debug=True)
