# insta-clone

## Description
insta-clone is a Django web application that emulates the basic functionalities of the Instagram application such as posting a picture, commenting on it, following and unfollowing a user account, and updating a user profile.

## User Stories
- Sign up to the application. 
- sign in to the application to start using.
- Upload my pictures to the application
- see my profile and all the posts
- follow other users.
- comment on other users posts.

## Live site
(https://igappclone.herokuapp.com/)

## Technologies used
* Django Framework - used to create the application. 
* Heroku - used to deploy the application. 

## Set up and installation
#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python as default handler
    `virtualenv -p /usr/bin/python venv && source venv/bin/activate`
For windows users use this to activa your environment
   ` source venv/Scripts/active`    
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <DBNAME>;
####  .env file
Create .env file and add the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<DBNAME>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations gallery
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

## Known Bugs
The user is unable to like a post.

## Contact Information
If you have any questions feel free to contact me.

## License
* MIT LICENSE
* Copyright (c) 2022 Joyce Njoroge