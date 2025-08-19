from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is the home fumction'

@app.route('/allow/<int:id>')
def allow(id):
    if id<25:
        return 'you have been allow because you id number is '+str(id)
    return 'not allow the employee'

if __name__=='__main__':
    app.run(debug=True)