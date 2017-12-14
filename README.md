# BookAnEntertainer App  - DJANGO App that works with PayPal

## Overview

### Steps to take before you run
    - Log in to https://developer.paypal.com/
    - For testing, ensure you have a PAYPAL Personal and Business accounts set up as they will be needed to make purchases
    - Download ngrok.exe to suit your platform from ngrok. Save it to your app's route folder
    - Open cmd prompt and navigate to app's route folder
    ..- RUN NGROK by typing 'ngrok http 8000
    ..- Can view requests in browser @ http://127.0.0.1:4040
    - In settings.py copy the https forwarding address setting from the running ngrok console. 
    ..- We need to add the address to the ALLOW_HOSTS list
    ..- Also set PAYPAL_NOTIFY_URL with the same address 
    ....- E.G. PAYPAL_NOTIFY_URL = 'https://9f37a350.ngrok.io/to-ngrok-or-not-to-ngrok/
    ....- The '/to-ngrok-or-not-to-ngrok/' corresponds to the PAYPAL route defined in <app>/urls.py as 
    ......- url(r'^to-ngrok-or-not-to-ngrok/', include(paypal_urls)),
    
