from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "this is home directory"

@app.route('/myName/<name>')
def myName(name):
    return "my name is "+name

if __name__=='__main__':
    app.run(debug=True)
