import requests

def list_datasets(is_based_on=None, limit=20, offset=0):
    """
    Fetch datasets from the ONS API.

    Parameters:
    - is_based_on (str, optional): A population type to filter datasets. Applicable to Census 2021 datasets only.
    - limit (int, optional): Maximum number of items to return. Default is 20, maximum is 1000.
    - offset (int, optional): Starting index of the items array to return. Default is 0.

    Returns:
    dict: The response containing datasets.
    """
    url = "https://api.beta.ons.gov.uk/v1/datasets"
    params = {
        "is_based_on": is_based_on,
        "limit": limit,
        "offset": offset
    }

    # Handle 404 response with an error exception
    try:
        # Code that might raise an exception
        response = requests.get(url, params=params)
        if response.status_code == 404:
            print(response.json())
            raise Exception("404: Not found")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    return response.json()

