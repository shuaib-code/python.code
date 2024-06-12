import requests

# Server details
server_url = 'http://shuaibcode.pythonanywhere.com/send-data'

# Data to send
data = {'msg': 'Hello, server!'}

# Send POST request to server
response = requests.post(server_url, json=data)

# Check response
if response.status_code == 200:
    print("Data sent successfully.")
else:
    print("Error:", response.text)
