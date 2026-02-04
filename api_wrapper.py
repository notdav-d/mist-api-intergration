import os
import requests
from dotenv import load_dotenv


# Load secrets from .env when this modile is imported
load_dotenv()

API_TOKEN = os.getenv("MIST_API_TOKEN")
ORG_ID = os.getenv("MIST_ORG_ID")

BASE_URL = "https://api.mist.com/api/v1"
endpoint =  f"/self"
headers = {
	"Authorization": f"Token {API_TOKEN}", 
	"Content-Type": "application/json"
}

def mist_get(endpoint: str, params: dict= None):
	"""
	Generic GET wrapper for Mist API

	endpoint: string after the base URL (example: f"/orgs/{ORG_ID}/devices")
	params: optional query parameters as a dict

	"""

	url = f"{BASE_URL}{endpoint}"
	resp = requests.get(url, headers=headers, params=params)
	resp.raise_for_status() #raiser an error if request failed
	return resp.json()

# Query the endpoint, store response in a dictionary
resp = mist_get(endpoint)
data = resp.get("identity", [])


print(f"Successfully queried {endpoint} API endpoint as {resp.get('email', 'unknown user')}")


