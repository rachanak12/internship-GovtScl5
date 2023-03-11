from flask import Flask,render_template
from contact_form import ContactForm
app=Flask(__name__)
app.config['SECRET_KEY']="VeGdV^Fs8950"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    form=ContactForm()
    return render_template('contact.html',form-form)

if __name__== "__main__":
    app.run(debug=True)