from flask import Flask, current_app, request, send_from_directory, make_response
from flask_cors import CORS;
from mpesa_payment import MpesaPayment
import json, os
from os import environ
from dotenv import load_dotenv, dotenv_values

app = Flask(__name__)

if environ.get("ENVIRONMENT") == "PRODUCTION":
    load_dotenv()
    app.config.from_mapping(dotenv_values())

CORS(app, origins="*")

@app.route("/")
def index():
    return send_from_directory("static-site", "index.html")

@app.route("/pay", methods=["POST"])
def pay():
    body = request.get_json()
    mpesa = MpesaPayment(app.config, body["phone_number"])
    
    #First request which is authorization
    authorization = json.loads(mpesa.authorization())    
    access_token = authorization["access_token"]
    
    # Second requres to initialize payment
    callback_url = f"{request.host}/confirm_payment" \
        if environ.get("ENVIRONMENT") == "PRODUCTION" \
            else "https://picpazz.com"
            
    payment_response = mpesa.stk_push( access_token, 
                            amount=1, callback_url=callback_url,
                            reference="0020023", description="Test payment")
    
    return make_response( json.loads(payment_response), 200 )

@app.route("/confirm_payment")
def confirm_payment():
    print(request.get_json)
    return "Thank you"

if __name__ == "__main__":
    app.run(port=5005)