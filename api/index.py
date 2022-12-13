from flask import Flask, render_template, redirect, url_for, request
from time import sleep
import threading
import func 

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        password = request.form['pwd']

        if user == 'ayham' and password == '1234':
            return redirect(url_for("work_page"))
        else:
            return "Invalid credential, <a href='/login'>Try again</a>"
    else:
        return render_template("page2.html")

@app.route("/page3")
def work_page():

    return render_template('page3.html')

    
@app.route("/running")
def f1():
    threading.Thread(target=func.strt).start()
    return render_template("base.html")


if __name__  == '__main__':
    app.run(debug = True, host='0.0.0.0', port=5000)