# BookAnEntertainer App  - DJANGO App that works with PayPal

## Overview

### What this app is for?
This app allows you to search fr and book entertainment for your event

### What does it do?
This app will allow users:
-   Search for entertainers by Type and location
-   Read their profile
-   View their gallery
-   Listen to their recordings
-   View their videos
-   Book the entertainer

### How does it work
There are 2 types of users: General and Entertainer
Entertainers must register in order to create a profile.
General Users can search the site but must be registered and logged in in order to make bookings or leave Reviews
Reviews are made via Fisqus plugin
This app talks to an API to filter out entertainers by type and location. Users can then click into individial profiles

##  Features


### Existing Features
-   Home Page
-   Search Page
-   Profile Page
-   Login Page
-   User Registration Page
-   Entertainer Registration Page
-   Paypal payments

### Features Left to Implement
-   Pagination on the search page
-   Contact form on Entertainer Profile

##  Tech Used
- [DJango](https://www.djangoproject.com/)
    I used Django for the Backend. It facilitated modelling of the entertainers and users. I also created an API that 
    the search page could communicate 
- [Python](https://www.python.org/)
    Django uses Python
- [Bootstrap](http://getbootstrap.com/)
	- We use **Bootstrap** to give our project a simple responsive layout. I used version 4
- [Paypal](https://developer.paypal.com/)
    - Paypal Sandbox is used in order to facilitate test payments
- [Disqus](https://disqus.com/)
    - Disqus is used to facilitate Reviews to entertainers
- [JQuery](https://jquery.com/)
    - JQuery is used to allow a responsive front end and to talk to the API 
- [GITHUB](https://github.com/)
    - Facilitates code sharing and version control

### Getting the code up and running
1. Log in to https://developer.paypal.com/
2. For testing, ensure you have a PAYPAL Personal and Business accounts set up as they will be needed to make purchases
3. Download ngrok.exe to suit your platform from ngrok. Save it to your app's route folder
4. Open cmd prompt and navigate to app's route folder
   1.If running locally, open cmd or Pycharm terminal, tell manage.py that you want to run in developer environment each time you do a command involving manage.py
        1. E.G. Type 'python manage.py runserver --settings=settings.dev'
   2.RUN NGROK by typing 'ngrok http 8000'
        1. Can view requests in browser @ http://127.0.0.1:4040
   3. In settings.py copy the https forwarding address setting from the running ngrok console. 
      1. We need to add the address to the ALLOW_HOSTS list
      2. Also set PAYPAL_NOTIFY_URL with the same address 
         1. E.G. PAYPAL_NOTIFY_URL = 'https://9f37a350.ngrok.io/to-ngrok-or-not-to-ngrok/
         2. The '/to-ngrok-or-not-to-ngrok/' corresponds to the PAYPAL route defined in <app>/urls.py as 
         3. url(r'^to-ngrok-or-not-to-ngrok/', include(paypal_urls)),
5. Run the program with command 'python manage.py runserver'    
