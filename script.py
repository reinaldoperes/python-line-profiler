import os
import requests


@profile  # Decorator used by line_profiler
def file_io_operations(file_name: str, content: str) -> None:
    """
    Performs file I/O operations: writing and reading from a file.

    Args:
        file_name (str): The name of the file to create and read.
        content (str): The content to write into the file.

    Returns:
        None
    """
    # Writing to a file
    with open(file_name, "w") as file:
        for _ in range(1000000):  # Simulate multiple write operations
            file.write(content)

    # Reading from the file
    with open(file_name, "r") as file:
        data = file.readlines()
        print(f"Read {len(data)} lines from the file '{file_name}'.")

    # Cleanup: Removing the created file
    os.remove(file_name)


@profile  # Decorator used by line_profiler
def fetch_data_from_api(endpoint: str, params: dict) -> dict:
    """
    Makes a GET request to an API endpoint and returns the response data.

    Args:
        endpoint (str): The API endpoint URL.
        params (dict): Query string parameters.

    Returns:
        dict: The JSON response from the API.
    """
    # Sending the GET request to the API
    response = requests.get(endpoint, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        print(f"Data received: {data}")
        return data
    else:
        print(f"API call failed with status code: {response.status_code}")
        return {}


def main():
    """
    Main function to execute I/O and API operations.
    """
    # Testing file I/O operations
    print("Starting file I/O operations...")
    file_io_operations("example.txt", "Test line\n")

    # Testing API call
    print("Starting API call...")
    fetch_data_from_api("https://jsonplaceholder.typicode.com/posts", {"userId": 1})


if __name__ == "__main__":
    main()
