from flask import Flask,request,render_template
import pickle
import pandas as pandas
from flask_cors import cross_origin
from sklearn.ensemble import RandomForestClassifier


app=Flask(__name__)
model = pickle.load(open("new.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
	if request.method=="POST":


		#input
		Pregnancies=int(request.form["Pregnancies"])

		Glucose=int(request.form["Glucose"])

		BP=int(request.form["BP"])

		SkinThick=int(request.form["SkinThick"])

		Insulin=int(request.form["Insulin"])

		BMI=float(request.form["BMI"])

		DPI=float(request.form["DPI"])

		Age=int(request.form["Age"])


		prediction=model.predict([[Pregnancies,Glucose,BP,SkinThick,Insulin,BMI,DPI,Age]])


		if (prediction==0):
			return render_template("home.html",prediction_text="You are at lower risk of having diabetes")

		else:
		    return render_template("home.html",prediction_text="You are at higher risk of having Diabetes")	



	


if __name__=="__main__":
	app.run(debug=True)


