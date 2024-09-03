import requests

# Replace with your Minikube IP
minikube_host = 'localhost'

# Define the URLs for your services
url_world = f'http://{minikube_host}/world'
url_hello = f'http://{minikube_host}/hello'


def fetch_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP error codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while requesting {url}: {e}")
        return None


def main():
    # Fetch responses from both services
    hello_response = fetch_response(url_hello)
    world_response = fetch_response(url_world)

    # Check if both responses were successful
    if hello_response is not None and world_response is not None:
        combined_response = f"{hello_response} {world_response}"
        print(combined_response)
    else:
        print("Failed to fetch one or both responses.")


if __name__ == "__main__":
    main()
