import requests

# Replace 'api_endpoint' with the URL of the API you're using
api_endpoint = 'https://api.example.com/endpoint'

# Replace 'dataset_file' with the path to your local dataset file
dataset_file = 'path/to/your/dataset.csv'

# Open the dataset file and read its contents
with open(dataset_file, 'r') as f:
    dataset_data = f.read()

# Set the API key and any other required headers
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

# Send a POST request to the API with the dataset data
response = requests.post(api_endpoint, headers=headers, data=dataset_data)

# Check the response status code to make sure the request was successful
if response.status_code == 200:
    print('Dataset uploaded successfully!')
else:
    print('Error uploading dataset:', response.text)