from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('res.html')



#result checker html page
@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        math = float(request.form['math'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        



if __name__ == '__main__':
   app.run(debug=True)