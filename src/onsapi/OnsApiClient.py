import requests
from . import OnsDataset, OnsDataList

class OnsApiClient:

    def list_datasets(self, is_based_on=None, limit=20, offset=0):
        url = "https://api.beta.ons.gov.uk/v1/datasets"
        params = {"is_based_on": is_based_on, "limit": limit, "offset": offset}

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                datasets_json = response.json()['items']  # Assuming 'items' is the key containing datasets
                ons_data_list = OnsDataList(datasets=[OnsDataset(**dataset) for dataset in datasets_json])
                return ons_data_list
            elif response.status_code == 404:
                print("Error 404: Not found. The requested asset could not be found.")
                return None
            elif response.status_code >= 500:
                print(f"Server error ({response.status_code}): The server encountered an error processing your request.")
                return None
            else:
                print(f"HTTP error ({response.status_code}): An unexpected HTTP error occurred.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Network exception occurred: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        