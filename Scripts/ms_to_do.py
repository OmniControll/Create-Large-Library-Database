import requests

# The endpoint URL
url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"

# The data for the request
data = {
    "client_id": "",
    "scope": "https://graph.microsoft.com/.default",
    "client_secret": "",
    "grant_type": "password",
    "username": "",
    "password": "",
}
# Send the request
response = requests.post(url, data=data)

# Print the full response
print(response.text)

# Get the access token from the response
access_token = response.json().get('access_token')
