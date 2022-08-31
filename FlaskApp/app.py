from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('pages/enterForm.html' )

@app.route('/about_your_beer')
def success(): 
    return render_template('pages/aboutBeer.html')

@app.route('/tableu')
def tableu(): 
    return render_template('pages/tableuPage.html')

@app.route('/database_verification')
def database(): 
    return render_template('pages/databaseVerification.html')

if __name__ == "__main__":
    app.run(debug=True)  