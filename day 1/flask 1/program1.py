from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Hello route was hit!")  # so we can see in terminal
    return "hello"

if __name__ == '__main__':
    print("Starting Flask app in debug mode...")
    app.run(debug=True)








