import requests

# Server details
server_url = 'http://127.0.0.1:5000/send-data'  # Update with your server URL

msg = str(input("enter your secret key"))

# Data to send
data = {'key': msg}

# Send POST request to server
response = requests.post(server_url, json=data)

# Check response
if response.status_code == 200:
    print("Data sent successfully.")
else:
    print("Error:", response.text)
