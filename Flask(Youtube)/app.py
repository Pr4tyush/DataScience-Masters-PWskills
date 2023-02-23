
from flask import Flask
#this below line create a WsGI Application
app=Flask(__name__)

@app.route('/')
# this decorator will take this function to homepage

def welcome():
    return "Hello My name is Pratyush and I am in BTECH 3rd year"

@app.route('/personal')
def personal():
    return "I am 6 feet tall boy"



if __name__ == "__main__":
    app.run(debug=True)
#debugger option will restart the server automatically
