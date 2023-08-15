# Maths Adventurer : whats it all about?

## Background
High school maths olympiad is well-respected in my home country, South Africa. I have participated in competitive math for nearly 7 years now. However, the problem is that access to good quality training and resources is not available to all, which is reflected in the poor representativeness of the South African International Maths Olympiad Team. The main reason being that there is just not enough black talent invited to training/selection camps. In order to fix this system of elitism and help bring the love for solving maths problems to all of South Africa I wanted to design a resource portal that acts as a digital training hub and guide to lower the entry point into olympiad math for all talented learners of colour. By just knowing the best online textbooks and resources, a manageable pathway can be pursued by those enthusiastic enough.

## Distinctiveness and Complexity
Maths Adventurer is a concept product that I created. I have specifically used the extended metaphor of exploring a new mountainous region in order to escape the boring environment of a math textbook. The contrast of vibrant colors and colorful images gives learners a friendly welcoming. Furthermore, the consistent use of bootstrap and flexbox allows for mobile-repsonsive display and guarantees a fair experience irrespective of device. The specific use case of this digital training hub allows for a new and distinct client base especially within South Africa where nothing like this exists as of today.  The website has a variety of complex functionalities of which I will briefly go over. Both unsigned and signed-in users will have access to the resources and competition catalogs. These are built using django models to ensure scalability. If a user signs in he/she will have the additional perk of being able to save competitions to a watchlist to view on their profile page. They can also add milestones of their choice and update the current status of them to track their performance throughout the academic year. Watchlist and status updates are updated instantly on the front-end through java-script code. Lastly, all users can access a calendar with dynamically added competition events. I used the FullCalendar API plug-in to allow for a neat display as well as the ability for users to see more details of the events by clicking on them. 

There is a central layout page so to remain consistent for every view of the website and allow users to quickly switch to various tabs. Each tab on the navigation panel on the top of the window has its own functionality. The logo image will go to the home view (index.html) when clicked. The profile tab (for signed-in users) allows users to view and customize their milestones and competition wathlist. The Competitions, Resources and Calendar tab allows the user to respectively view all competitions, resources and events on the calendar. 

There are severl Maths Competitions in South Africa (more than 15). It was approprate for me to desing a model for each Competition. The model contains fields that would be helpful for the user and for categorising it. In the resource tab there is also 


## Overview of files
There is only one django app: MathsAdventurer
1. Static files:
- **Styles.css** has the all the basic css properties that are applied to many html elements. In particular it allows for a consistent color scheme.
- **Milestone.js** relates to the milestone functionality on the user's profile page. There is a server API request to update the status of the milestone. 
- **Competition.js** relates competition template and allows for the filter functionality per grade  as well as a server API request to update the user's competition watchlist. 
- **calendar.js** makes use of the FullCalendar API plug-in and allows for an interactive click event with a fetch call for the event's specific details in the database. 

2. layout.html: 
    The general template layout of all the html pages, which extends it.

3. index.html: 
    Home page with statically created content that gives an overview of the mission and offerings of the platform. 

4. profile.html: 
    User can view their milestones and competition watchlist if they are logged in.

5. competitions.html: 
    Catalog of all competitions and allows user to filter them by grade.(no log in needed)

6. resource_topics.html: 
    The front gate for all resources and separates the resources into five fixed topics to allow for users to easily access their needs.

7. resources.html: 
    Accessed through **resource_topics.html** and has numerous links to online pdfs and handouts of the different mathematical theory. It also has three difficulties (valley, slope, summit)

8. archive.html:
    Accessed through **profile.html** and automatically stores milestones from previous years so that the user can look back at his/her progress. 

9. calendar.html:
    A container div for the FullCalendar calendar object.

10. error.html:
    A template for an error message to correct users on how to use the website properly.

11. register.html:
    Allows a new user to register and takes the user to the home page signed in once successfully registered. 

12. login.html:
    A sign-in page to allow the user to enter his/her username and password and gain access to their profile page after signing in.

13. requirements.txt
    Contains a list of all the necessary plug-ins to be downloaded in order fully leverage all the capabilities of the app. Only Full Calendar is present.

14. models.py
- **User** is the built-in user model that stores the personal information and logging credentials of each user. 
- **Competition** represents a maths competition and incorporates the details that an admin can manually add. The many-to-many field *users_watching* represents the competition watchlist for each signed-in user. This will be edited from the competition tab where users can add/remove from their list with a corresponding server API call. 
- **Event** relates to one competition. It represents the date that a single round of the competition is written. It is used as a single instance of the competition on the calendar tab. All events are loading using the FullCalendar api call to the database. 

15. admin.py
    Registers and customizes the display of all the models in the '/admin' url path and uses the Django built-in admin feature to add/edit/delete records. 

## How to run my application
Download the necessary requirements in the **requirements.txt** file. This is only FullCalendar. The other downloads are accessible on the head div of **layout.html**, which includes meta tags, bootstrap scripts, and FullCalendar scripts.[Link to Full Calendar](https://fullcalendar.io/docs/view-api). Then the application can be run in a local environment with the usual 
python manage.py (makemigrations MathsAdventurer/migrate/runserver) commands. Note that there is data pertaining to the various models already in the database. 


 
