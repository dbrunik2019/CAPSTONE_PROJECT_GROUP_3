from flask import Flask, render_template, url_for
from lightgbm import LGBMClassifier
import pickle 
import numpy as np 
app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('pages/enterForm.html' )

@app.route('/about_your_beer')
def success(): 
    return render_template('pages/aboutBeer.html')

#import Flask
from flask import Flask, render_template, request
@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        
        #get form data
        Original_gravity = float(request.form.get('Original_gravity'))
        Final_gravity = float(request.form.get('Final_gravity'))
        Alcohol_content = float(request.form.get('Alcohol_content'))
        SRM = float(request.form.get('SRM'))
        IBU = float(request.form.get('IBU'))
        
        #Load the pickled model
        model_from_pickle = pickle.load(open('lightgmb.pkl','rb'))

        #predict   
        test_data = [Original_gravity,Final_gravity,Alcohol_content,SRM,IBU]
        prediction = model_from_pickle.predict_proba([test_data])

        print(prediction)
        return render_template('pages/aboutBeer.html',prediction = prediction)
    pass



@app.route('/tableu')
def tableu(): 
    return render_template('pages/tableuPage.html')

@app.route('/database_verification')
def database(): 
    return render_template('pages/databaseVerification.html')

if __name__ == "__main__":
    app.run(debug=True)  



