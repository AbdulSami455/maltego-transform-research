import requests

# Define the API endpoint and parameters
url = "https://ws-public.interpol.int/notices/v1/un"
params = {
    "name": "Ahmed al-Sharaa",
    "unResolution": "1267",
    "page": 1,
    "resultPerPage": 200
}

headers = {
    "accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("Response Data:")
    print(response.json())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
    print("Response Content:")
    print(response.text)
