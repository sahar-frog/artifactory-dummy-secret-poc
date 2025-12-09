import os
import requests

ARTIFACTORY_URL = "https://shredder.jfrog.io/artifactory/api/system/ping"
TOKEN = os.getenv("cmVmdA7kG2q9tQf8Xx1BzE4mR0sLpH3uVaC6wJ9NdS2yTgK5rQh8UuP0cMfB7DnZ")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

try:
    response = requests.get(ARTIFACTORY_URL, headers=headers, timeout=10)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
