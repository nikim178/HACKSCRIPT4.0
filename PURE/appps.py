from flask import Flask, render_template,request
import numpy as np
import subprocess as sp
import pickle

# model = pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('home.html')

@app.route("/prediction")
def user():
    return render_template('prediction.html')

@app.route("/home2")
def home2():
    # co=0
    # ozone=0
    # no2 =0
    # pm=0

    # aqipre=0

    # if request.menthod=='POST':
    #     aqi= 40
    #     aqicat = 0
    #     co = request.form['co']
    #     ozone = request.form['ozone']
    #     no = request.form['no']
    #     pm = request.form['pm']

    # arr = np.array([[aqi,aqicat,co,ozone,no,pm]])
    # aqipre = model.predict(arr)



    # aqipre = model.predict(arr)
    return render_template('home2.html') #industry page

def main():
    return render_template('home.html')


if __name__=="__main__":
    app.run()