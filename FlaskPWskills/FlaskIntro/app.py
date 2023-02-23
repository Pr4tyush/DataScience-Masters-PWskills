from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "<p>Hello Everyone My name is Pratyush!!</p>"

@app.route("/contact")
def contact():
    return "<p>Connect me through Linkedin</p>"

@app.route("/test")
def test():
    return "Hello"

@app.route("/test1")
def test1():
    data = request.args.get('x')
    return "This is my data input form my url {}".format(data)



if __name__ == "__main__":
    app.run(host = "0.0.0.0")
