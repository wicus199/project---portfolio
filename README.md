# My Project Portfolio

This is my project portfolio site to showcase my work. It was recently converted
to a flask application to be able to use relational databases further down the 
line. 

## Installing the Application

It is highly recommended to create a Python 3 virtual environment inside the directory
where the repository will be cloned. Python3 was used for this project

To install the application, do the following:
* Clone the repository to a location on your machine
* Create and activate the virtual environment inside this directory
* Inside the virtual environment, install flask using `pip3 install flask`
* Set the `FLASK_APP` environment variable using `export FLASK_APP=portfolio.py`
* Run the application using `flask run`. This will host the application on `localhost`
* Visit the page in your browser using `https://localhost:5000/`