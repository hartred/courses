This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).


##To Handle with Flask you need

First step:
1. Install virtualenv 

###`python3 -m pip install --user virtualenv`

2. SetUp virtualenv 

###`python3 -m virtualenv venv`

3. Activate env 

###`source venv/bin/activate`

Second step:
1. Choose system interprenter or choose existed from 

###`venv/bin/`

2. Install all requirements 

###`pip3 install -r requirements.txt`


Third step:
1. You should create database:

### `user:postgres`

2. if need:

### `password:12345678`

### `db_name:flask_dropbox`

###Try to handle without this step, maybe it should work!
3. Go to python console and run 
###`from app.extensions import db`
### `db.create_all()`
4. To migrate all this piece of scum 
### `flask db migrate` 
### `flask db upgrade`

Try to get up server:
1. At this moment as author thinks, you can start your flask/or not
 ###`flask run`

-------------------------------------------------

### React setUp
1. First step is `cd/react/dropbox_react`
2. Here you should 
###`npm install` 
better under `sudo su`


### `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

P.S Артем, извиняюсь за отсутствие работы из под docker-compose.