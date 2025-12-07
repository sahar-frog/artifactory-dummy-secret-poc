import os
import requests

ARTIFACTORY_URL = "https://shredder.jfrog.io/artifactory/api/system/ping"
TOKEN = os.getenv("cmVmdGtuOjAxOjE3OTYwMzQ1MjM6a1hQbE5qR3d6U2hYbU9jR1Z0dWJ6cE1Qd0k=")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

try:
    response = requests.get(ARTIFACTORY_URL, headers=headers, timeout=10)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.RequestException as e:
    print("Error:", e)
