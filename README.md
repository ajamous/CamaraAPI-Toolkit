# CamaraAPI-Toolkit
A collection of client scripts for quick testing and integration with the CAMARA API Standard


## CamaraRoamingManager

`CamaraRoamingManager.py` is a Python script for interacting with the CAMARA API to manage and check the roaming status of devices and to handle subscription events related to device roaming status.

## Prerequisites

- Python 3.6 or higher
- `requests` library installed (install via `pip install requests`)
- An OAuth 2.0 token for authentication with the CAMARA API (Refer to CAMARA API documentation on how to obtain this)

### Configuration

Before running the script, set the following environment variables:

- `CAMARA_API_BASE_URL`: The base URL of the CAMARA API.
- `OAUTH_TOKEN`: Your OAuth 2.0 token for authorization.

You can set these directly in your environment, or use a `.env` file in the same directory as the script with the following content:

```env
CAMARA_API_BASE_URL=http://api.example.com/device-status/v0
OAUTH_TOKEN=your_oauth_token_here
```

If using a `.env` file, make sure the `python-dotenv` package is installed:

```sh
pip install python-dotenv
```

### Usage

Run the script from the command line, providing the necessary arguments for the action you want to perform.

#### Check Roaming Status

```sh
python3 CamaraRoamingManager.py --phone +1234567890
```

#### Create a New Device Status Subscription

```sh
python CamaraRoamingManager.py --create --subscription_detail '{"type":"org.camaraproject.device-status.v0.roaming-status","device":{"phoneNumber":"+1234567890"}}' --webhook '{"notificationUrl":"https://your-webhook-url.com/callback","notificationAuthToken":"your_auth_token"}'
```

### List All Device Status Subscriptions

```sh
python3 CamaraRoamingManager.py --list
```

#### Retrieve a Specific Device Status Subscription

```sh
python3 CamaraRoamingManager.py --retrieve "subscription_id_here"
```

#### Delete a Specific Device Status Subscription

```sh
python3 CamaraRoamingManager.py --delete "subscription_id_here"
```

### Support

For support and further assistance, please contact support@telecomsxchange.com or refer to the [CAMARA API documentation](https://github.com/camaraproject/).


