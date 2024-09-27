# app.py (Flask Backend)
from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio credentials (ensure these are properly set in your environment for security)
ACCOUNT_SID = 'ACdc2208c4d94c873c20e2ae447f6eb22d'
AUTH_TOKEN = '932ee0b809d8b65650acbe6332b20719'
TWILIO_PHONE_NUMBER = '+18559710461'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/send_sms', methods=['POST'])
def send_sms():
    data = request.json
    phone_number = data.get('phone_number')
    message = data.get('message')

    if phone_number and message:
        try:
            message = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            return jsonify({"status": "success", "message_sid": message.sid}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    return jsonify({"status": "error", "message": "Missing data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
