
from flask import Flask,redirect,render_template,request,url_for
from numpy import integer
from wtforms import Form,StringField,SubmitField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

"initialising the application "

app=Flask(__name__)

#database creation
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

# initialisation of database
# with app.app_context():
#     db.create_all()

#database Columns
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key="True",nullable="False")
    content=db.Column(db.String(200),nullable="False")

    def __repr__(self):
        return '<Task %r>' % self.id

# app.app_context().push()
# db.create_all()
# app.app_context().pop()


#home page
@app.route("/",methods=["GET","POST"])
def homepage():
    return render_template('home.html')  
 

#Our story page
@app.route("/our_story",methods=["GET","POST"])
def ourStoryPage():
    return render_template('our_story.html')

#Shops page
@app.route("/shops/",methods=["GET","POST"])
def shopsPage():
    return "This is a shop page"

#Corporate gift page
@app.route("/corporate_gifts",methods=["GET","POST"])
def corporateGifts():
    return render_template("corporate_gifts.html")


#login page
@app.route("/login",methods=["GET","POST"])
def loginPage():
    if request.method == 'POST':
        # Check which form was submitted
        if 'signup' in request.form:
            # Handle signup form submission
            # Extract form data (username, email, password, etc.)
            # Validate data and store in the database
            # Redirect to a success page or login page
            return redirect(url_for('login'))
        elif 'login' in request.form:
            # Handle login form submission
            # Validate credentials and log the user in
            # Redirect to the user's profile or homepage
            
            return redirect(url_for("homepage"))
    return render_template('login.html')  # Render the main page template




# #register page
@app.route("/register",methods=["GET","POST"])
def registerPage():
    return render_template('footer.html')


#user profile page
@app.route("/profile",methods=["GET","POST"])
def profilePage():
    return "This is a user profile page"

#local localmenu page
@app.route("/menu",methods=["GET","POST"])
def localMenu():
    return render_template("menu.html")

#order page
@app.route("/order",methods=["GET","POST"])
def orderPage():
    return "This is an order page"

#corporate gift order page
@app.route("/gift_order",methods=["GET","POST"])
def giftOrder():
    return "This is an order page"





if __name__=="__main__":

    app.run(debug=True)
    



