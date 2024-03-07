# Flask M-Pesa API Integration
This is a demo for integrating the M-Pesa api with a Flask application

### Prerequisites
- python 3
- pipenv:- for managing python dependancies

### How to setup
1. Run the following command to set up dependancies
    ```
    pipenv install && pipenv shell
    ```
2. set up M-Pesa environment variables in a .env file
    
    - FLASK_MPESA_CONSUMER_KEY = < copy paste the key here >
    - FLASK_MPESA_CONSUMER_SECRET = < copy paste the secret here >
    - FLASK_MPESA_BUSINESS_SHORTCODE = < copy paste the short code here >
    - FLASK_MPESA_PASSKEY = < copy paste the passkey here >