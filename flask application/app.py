from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #decorator - execute the below fn automatically
def index():
    return 'hello world from flask !!!!'

@app.route('/homepage')
def home():
    return render_template('homepage.html')
    
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/enquiry')
def enquiry():
    return render_template('enquiry.html')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)

