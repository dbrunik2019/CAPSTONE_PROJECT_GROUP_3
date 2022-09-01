from flask import Flask, render_template, request
import pickle 
import numpy as np 
import static.data.style_family_data as beer_data
app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('pages/enterForm.html' )

@app.route('/no_data_available')
def missing(): 
    return render_template('pages/noBeerDataAvailable.html')

@app.route('/about_your_beer')
def success(): 
    return render_template('pages/aboutBeer.html')


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
        test_data = [Original_gravity, Final_gravity, Alcohol_content, SRM, IBU]
        prediction = model_from_pickle.predict_proba([test_data])
        [new_list] = prediction
        confidence = round(max(new_list) * 100)
        style_family_id = new_list.argmax() 
        beer_name = beer_data.name[style_family_id]
        beer_overall = beer_data.overall_impression[style_family_id]
        beer_smell = beer_data.aroma[style_family_id]
        beer_taste = beer_data.flavor[style_family_id]
        beer_look = beer_data.appearance[style_family_id]
        beer_img = beer_data.img[style_family_id]
        print(style_family_id)
        return render_template(
            'pages/aboutBeer.html', 
            beer_name = beer_name, 
            beer_overall = beer_overall, 
            beer_smell = beer_smell, 
            beer_taste = beer_taste, 
            beer_look = beer_look,
            beer_img = beer_img,
            confidence = confidence
            ) 
    pass

@app.route('/tableu')
def tableu(): 
    return render_template('pages/tableuPage.html')

@app.route('/database_verification')
def database(): 
    return render_template('pages/databaseVerification.html')

if __name__ == "__main__":
    app.run()  



