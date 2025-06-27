# 20250624 lab
Challenge:

- Create a new django project and call it: Project_two
- Create a new Django App: ”AppTwo”
- Create an Index View that returns: <em>My Second App </em>
- Link this view to the urls.py file

# 20250625 lab

Complete the following task:
- Create a templates directory and connect it to the settings.py file
- Create a new view called help and use url mapping to render it for any page with the extension /help
- Add template tags to return “Help Page”


# 20250626 lab: Models
 
Create a new model called UserProfile. This model should represent a profile for someone who visited a webpage. It should have the following fields:

- webpage: A ForeignKey to the Webpage model.
- username: A CharField (max length 100).
- email: An EmailField.
- comment: A TextField, optional.
- timestamp: A DateTimeField that stores the time the user visited (set auto_now_add=True).
- Update __str__() so it returns "username | webpage".
- Run makemigrations and migrate.
- Register the model in admin.py and verify that you can add UserProfiles from the admin interface.


# 20250627 lab: Models-Templates-Views

- Start a new project
- Add a new model called User. It should have these fields:
  - First Name
  - Last Name
  - Email
- Make sure you make the migrations!
- Then create a script that will populate your database with fake Users.
- Then confirm the populating through the Admin interface.
- Then Create a view for your website for the domain extension /users
- This /users page will be an HTML list of the user names and emails.
- You will use template tags to generate this content from the User model.
- Remember to change your urls.py files to deal with the changes to the /users extension!