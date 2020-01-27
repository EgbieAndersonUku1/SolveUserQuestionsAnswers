

# Ask a question and have it  answered by an expert
The url for the app is https://lit-island-38001.herokuapp.com

## Project description
The project is a website that allows a user to ask any question or questions to a series of experts once the user has been registered. Once the question has been asked the user can select an expert to direct that question to. The expert can then log into their account view the question and answer that question or questions.

The account has** three main accounts** the Admin, expert and regular user account. 

The admin account has certain privelidges that are not available for the other three accounts.

Admin account:
1. Can create any user and assigned that account to either a expert or regular user
1.  can view the number of **users** on the system on the **user tab navigation bar** in order to see the following inforation

  1.  See whether the account is an expert or normal user account. 
	1. See if the user is logged in or not
	1. Changing an existing account to either expert or regular user by clicking on the link table
1.  When the **search** parameter is used which is only visible to the admin account the admin is able to see a lot more information regarding the user and do a lot more 

Able to see:
	1. Username
	1. User ID
	1. Encrypted password
	1. The date the user joined the system
	1. Whether the account is active or deactivated. By clicking on the link in the table the admin is able to disable the user account which prevents them from logging in. The same click activates the account if it is deactivated.

Expert Account:
1. The expert user account cannot ask any questions but can view a list questions directed at him or her. He or she is then able to answer any of these questions that was put to them by the regular user

Regular account
1. The regular user account has the power to ask any question and then select an expert to answer it.

All accounts have the ability to change their passwords

## Technologies used
Python 3.6
Flask
HTML
JavaScript
Bootstrap
Sqlite3

## Test users on the system to play with:
Admin user
Login name is Admin
Password is admin1234

Expert user
Login: expertuser
password: expert1234

Regular user
Login: sam
password: 12345678



## How to run this in your local system
1. Create a virtual environment optional
1. Create a **name** for your directory
1. Go into your new directory
1. Clone the repository by using the command git clone https://github.com/EgbieAndersonUku1/SolveUserQuestionsAnswers.git .
1. Type the command "**pip install -r requirements.txt**" (making sure you are in the root directory) this will install all the dependencies on your virtual environment
The full stop at end copies all the folder and directories and sub-directories into the your chosen directory without creating the based folder
1. Run the command ***python create_tables.py*** to create the database
1. Run the command **python create_test_users.py** this will create two users accounts an expert and an admin account. This is especially important because it is the only way to create and admin account because whey you register a new account it will automatically be assigned as a regular account unless you go into the database and change it to one.
1. Next run the command** flask run**
1. Open a browser of your choice and type in **http://127.0.0.1:5000** and watch app go



