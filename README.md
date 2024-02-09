### Installation

You can install this package using pip:

```
pip install onsapi
```

### Example usage

To get a list of all the available datasets:
```
from onsapi import OnsApiClient

client = OnsApiClient()
list_of_datasets = client.list_datasets()

for dataset in list_of_datasets.items:
    print(dataset)
```

To load a certain dataset as a dataframe: 

```
selected_dataset = list_of_datasets[0]

selected_dataset.download_csv()

df = selected_dataset.load_as_df()
```