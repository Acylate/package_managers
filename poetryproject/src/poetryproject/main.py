import requests

def main():
    response = requests.get("https://google.com/")
    print(response.status_code)

