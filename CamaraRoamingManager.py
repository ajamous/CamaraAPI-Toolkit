import requests
import os
import argparse
import logging
import json
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the CAMARA API Base URL and OAuth details from environment variables
CAMARA_API_BASE_URL = os.getenv('CAMARA_API_BASE_URL', 'http://localhost:9091/device-status/v0')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')  # You need to obtain this token from your OAuth server

# Standard headers to include with every request
HEADERS = {
    'Authorization': f'Bearer {OAUTH_TOKEN}',
    'Content-Type': 'application/json'
}

# Function definitions for each API endpoint
def get_current_roaming_status(phone_number):
    endpoint = f"{CAMARA_API_BASE_URL}/roaming"
    payload = {"device": {"phoneNumber": phone_number}}
    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()

def create_device_status_subscription(subscription_detail, webhook):
    endpoint = f"{CAMARA_API_BASE_URL}/subscriptions"
    payload = {
        "subscriptionDetail": subscription_detail,
        "webhook": webhook
    }
    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()

def retrieve_subscription_list():
    endpoint = f"{CAMARA_API_BASE_URL}/subscriptions"
    response = requests.get(endpoint, headers=HEADERS)
    return response.json()

def retrieve_subscription(subscription_id):
    endpoint = f"{CAMARA_API_BASE_URL}/subscriptions/{subscription_id}"
    response = requests.get(endpoint, headers=HEADERS)
    return response.json()

def delete_subscription(subscription_id):
    endpoint = f"{CAMARA_API_BASE_URL}/subscriptions/{subscription_id}"
    response = requests.delete(endpoint, headers=HEADERS)
    return response.status_code == 204

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description='CAMARA API Client Script')
    # Add arguments to the parser
    parser.add_argument('--phone', type=str, help='Phone number to check roaming status for')
    parser.add_argument('--create', action='store_true', help='Create a new device status subscription')
    parser.add_argument('--list', action='store_true', help='List all device status subscriptions')
    parser.add_argument('--retrieve', type=str, help='Retrieve a specific device status subscription')
    parser.add_argument('--delete', type=str, help='Delete a specific device status subscription')
    parser.add_argument('--subscription_detail', type=str, help='Subscription detail for creating a subscription')
    parser.add_argument('--webhook', type=str, help='Webhook information for creating a subscription')

    # Parse the arguments
    args = parser.parse_args()

    try:
        if args.phone:
            logging.info(f"Getting roaming status for phone number: {args.phone}")
            status = get_current_roaming_status(args.phone)
            print(status)
        
        if args.create:
            if not args.subscription_detail or not args.webhook:
                logging.error("Both subscription_detail and webhook are required for creating a subscription.")
                return
            logging.info("Creating new device status subscription")
            create_response = create_device_status_subscription(json.loads(args.subscription_detail), json.loads(args.webhook))
            print(create_response)
        
        if args.list:
            logging.info("Listing all device status subscriptions")
            subscriptions = retrieve_subscription_list()
            print(subscriptions)
        
        if args.retrieve:
            logging.info(f"Retrieving subscription with ID: {args.retrieve}")
            subscription = retrieve_subscription(args.retrieve)
            print(subscription)
        
        if args.delete:
            logging.info(f"Deleting subscription with ID: {args.delete}")
            deleted = delete_subscription(args.delete)
            print("Subscription deleted successfully." if deleted else "Failed to delete subscription.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
