# CamaraNumberVerification.py

import requests
import os
import argparse
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the API base URL and OAuth token from environment variables
API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com/number-verification/v0')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')

# Headers with the OAuth token
HEADERS = {
    'Authorization': f'Bearer {OAUTH_TOKEN}',
    'Content-Type': 'application/json'
}

# Function to verify a phone number
def verify_phone_number(phone_number):
    endpoint = f"{API_BASE_URL}/verify"
    payload = {
        "phoneNumber": phone_number  # Or "hashedPhoneNumber" if using hashed format
    }
    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()

# Function to get the device phone number associated with the token
def get_device_phone_number():
    endpoint = f"{API_BASE_URL}/device-phone-number"
    response = requests.get(endpoint, headers=HEADERS)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description='CAMARA Number Verification API Client')
    parser.add_argument('--verify', type=str, help='Verify the phone number')
    parser.add_argument('--get-number', action='store_true', help='Get the device phone number associated with the token')

    args = parser.parse_args()

    if args.verify:
        result = verify_phone_number(args.verify)
        print(result)

    if args.get_number:
        result = get_device_phone_number()
        print(result)

if __name__ == '__main__':
    main()
