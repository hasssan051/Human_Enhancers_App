# Putative_Enhancers_App
 Web Application to query the HERD database.

 **Disclaimer**: Since the HERD database is too large to share, I have decided to keep hosting it on my local server. Therefore if you need to use the Search functionality of this web application you will have to let me know by email so that I can start my local server and you can connect to it. 
 **My Email**: hcysz1@nottingham.edu.my

 ## Create virtual environment to run application in

 If you have conda then use the command:

 ```conda env create -f environment.yml```

 If otherwise you want to make use of pip then use the following command to create the virtual environment:

 ```pip install -r requirements.txt ```

## Running the application

To run the application simply go to the project directory Putative_Enhancers_App using command line, whilst running the virtual environment created above, and then type in 

``` flask run ```

The application is configured to run with configuration object Config_FYP which can be found in config.py

### A user called John Doe has already been created if you want to test the User account functionality of the application
A user with the following information is already stored inside the users.db database:
- email: johndoe@gmail.com
- password: 123456789

These details can be used to log in to this application. We also have premade queries which can be used to fill in the search form and searched