from flask import Flask ,redirect,url_for

app = Flask(__name__)

@app.route('/')

def welcome():
    return "Hello World"

#dynamically changed

@app.route("/sucess/<int:score>")
def sucess(score):
    return "The person has passed and marks is: "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has fail and marks is: "+str(score)

#result checker
@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks<50:
        result ="Fail"
    else :
        result = "Passed!"
    # return result
    return redirect(url_for(result,score=marks))


if __name__  == "__main__":
    app.run(debug=True)