import requests
import os

def ensure_data_folders(dataset_id):
    # Check if the 'data' folder exists in the current directory
    data_path = os.path.join(os.getcwd(), 'data_onsapi')
    if not os.path.exists(data_path):
        os.makedirs(data_path)
        print(f"'data' folder created at: {data_path}")
    else:
        print(f"'data' folder already exists at: {data_path}")

    # Check if a folder with the dataset's id exists within the 'data' folder
    dataset_path = os.path.join(data_path, dataset_id)
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
        print(f"Folder for dataset id '{dataset_id}' created at: {dataset_path}")
    else:
        print(f"Folder for dataset id '{dataset_id}' already exists at: {dataset_path}")
