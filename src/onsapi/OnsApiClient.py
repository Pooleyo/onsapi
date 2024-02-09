from . import OnsDatasetList
import requests

class OnsApiClient:

    def list_datasets(self, is_based_on=None, limit=20, offset=0):
        """
        Fetch datasets from the ONS API.

        Parameters:
        - is_based_on (str, optional): A population type to filter datasets. Applicable to Census 2021 datasets only.
        - limit (int, optional): Maximum number of items to return. Default is 20, maximum is 1000.
        - offset (int, optional): Starting index of the items array to return. Default is 0.

        Returns:
        dict or None: The response containing datasets if successful, None otherwise.
        """
        url = "https://api.beta.ons.gov.uk/v1/datasets"
        params = {
            "is_based_on": is_based_on,
            "limit": limit,
            "offset": offset
        }

        try:
            response = requests.get(url, params=params)

            # Successful response
            if response.status_code == 200:
                return OnsDatasetList.parse_obj(response.json())

            # Not found or other client-side errors
            elif response.status_code == 404:
                print("Error 404: Not found. The requested asset could not be found.")
                return None

            # Server errors
            elif response.status_code >= 500:
                print(f"Server error ({response.status_code}): The server encountered an error processing your request.")
                return None

            # Other HTTP errors
            else:
                print(f"HTTP error ({response.status_code}): An unexpected HTTP error occurred.")
                return None

        except requests.exceptions.RequestException as e:
            # Handle network-related errors e.g., DNS failure, refused connection, etc
            print(f"Network exception occurred: {e}")
            return None

        except Exception as e:
            # General exception catch to handle any unforeseen errors
            print(f"An error occurred: {e}")
            return None
