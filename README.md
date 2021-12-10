# Flask_App
Python Flask Mini App | SQLite | SQLAlchemy

# FlaskApplication
Basic  flask application for managing users

![github-small](https://i.ibb.co/9p08PZb/bout.png)



# STACK INFORMATION 
The app is written in Python on top of the Flask micro-framework. The Front-End was written in Html, Php and Flask Boostrap. SQlite was implemented as the database of choice, in conjunction with the SQLAlchemy ORM to simplify CRUD operations.

# LIST OF FEATURES 
The following are the main high-level features available through the app

* Users can register and login 
* Users can modifie his own informations
* Users can display other users informations 

# How to use use this repo
* Fork this repo and rename it 
* Read "Instructions for development" below (modify as necessary for your app)

# Instructions for development

Clone the repository:


```
git clone https://github.com/DORGAA/FlaskApplication.git
```
Set up a Virtualenv environment (or alternatively use conda ):

```
cd /FlaskApplication
Virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

Initialise the sqlite database:

```
cd /app
python3
from app import db
db.create_all()
```

In your terminal go to the app folder /app and set Environment variable configs as :

 * SECRET_KEY 
 * SQLALCHEMY_DATABASE_URI
 * SQLALCHEMY_TRACK_MODIFICATIONS 
 

```
export MYAPP_CONFIG="config.DevConfig"
```
set application secret key: 

```
export SECRET_KEY="ChooseAsecretKey"
```
run app: 

```
flask run 
```


