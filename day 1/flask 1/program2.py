from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("hello function is called")
    return "hello world hi2"


if __name__=='__main__':
    app.run(debug=True)
