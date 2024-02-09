import pandas as pd
from pydantic import BaseModel
from typing import Optional, List
import requests
import os

class OnsDataset(BaseModel):
    id: str
    title: str
    description: str
    contacts: list
    links: dict
    methodologies: Optional[List]
    next_release: str
    #qmi: str
    related_datasets: Optional[List]
    release_freqeuncy: Optional[str]
    state: str


    def download_csv(self):
        # Ensure the data folders for this dataset exist
        data_path = os.path.join(os.getcwd(), 'data_onsapi')
        if not os.path.exists(data_path):
            os.makedirs(data_path)
            print(f"'data' folder created at: {data_path}")
        else:
            print(f"'data' folder already exists at: {data_path}")

        dataset_path = os.path.join(data_path, self.id)
        if not os.path.exists(dataset_path):
            os.makedirs(dataset_path)
            print(f"Folder for dataset id '{self.id}' created at: {dataset_path}")
        else:
            print(f"Folder for dataset id '{self.id}' already exists at: {dataset_path}")
        
        # Extract the latest version link for the CSV
        latest_version_link = self.links["latest_version"]["href"]

        try:
            # Fetch the metadata from the latest version link
            metadata_response = requests.get(latest_version_link)
            metadata_response.raise_for_status()  # Check for HTTP request errors
            metadata = metadata_response.json()
            
            # Extract the CSV download link from the metadata
            csv_download_link = metadata["downloads"]["csv"]["href"]
            
            # Download the CSV file
            csv_response = requests.get(csv_download_link)
            csv_response.raise_for_status()  # Check for HTTP request errors
            
            # Define the full path for the CSV file to be saved
            csv_file_path = os.path.join(dataset_path, f"{self.id}.csv")
            
            # Write the content of the CSV response to a file
            with open(csv_file_path, 'wb') as csv_file:
                csv_file.write(csv_response.content)
            print(f"CSV file successfully downloaded and saved to: {csv_file_path}")
        except Exception as e:
            print(f"Failed to download CSV file: {e}")


    def load_as_df(self):
        # Define the path to the expected CSV file
        csv_file_path = os.path.join(os.getcwd(), 'data_onsapi', self.id, f"{self.id}.csv")
        
        # Check if the CSV file exists
        if os.path.exists(csv_file_path):
            # Load the CSV into a pandas DataFrame
            dataframe = pd.read_csv(csv_file_path)
            return dataframe
        else:
            # Raise an error if the file does not exist
            raise FileNotFoundError(f"The CSV file for dataset id '{self.id}' does not exist. Please download the dataset using the download_csv method before attempting to load it.")

    def __str__(self):
        return (
            f"OnsDataset:\n"
            f"  Title: {self.title}\n"
            f"  Id: {self.id}\n"
            f"  Description: {self.description}\n"
            f"  Contacts: {self.contacts}\n"
            f"  Links: {self.links}\n"
            f"  Methodologies: {self.methodologies}\n"
            f"  Next release: {self.next_release}\n"
            f"  Related datasets: {self.related_datasets}\n"
            f"  Release freqeuncy: {self.release_freqeuncy}\n"
            f"  State: {self.state}\n"
        )
