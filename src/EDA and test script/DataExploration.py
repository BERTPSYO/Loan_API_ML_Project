



import requests
import json  # Import the 'json' module

# Define the URL of your Flask app
url = 'http://localhost:9696/predict'  # Update with the actual URL

# Sample data as a Python dictionary
sample_data = {
    "Amount Requested": 90000.0,
    "Debt-To-Income Ratio": 150.0,
    "employment Length": 10,
    "policy_code": 1,
    "risk_score": 800
}

# Serialize the Python dictionary into a JSON string
sample_data_json = json.dumps(sample_data)

# Send a POST request to your Flask app with JSON data
response = requests.post(url, data=sample_data_json, headers={'Content-Type': 'application/json'})

# Check the response
if response.status_code == 200:
    result = response.json()
    accepted_pred = result['accepted_pred']
    if accepted_pred[0] == 1:
        print("The loan should be authorized")
    else :
        print("The loan should be denied")
    
else:
    print(f"Request failed with status code: {response.status_code}")


