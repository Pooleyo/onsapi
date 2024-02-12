### Installation

You can install this package using pip.

```
pip install onsapi
```

### Example usage

You can get a list of all datasets available on the ONS API.

```
from onsapi import OnsApiClient

client = OnsApiClient()
datasets = client.list_datasets()
```

Information about each dataset can be pretty printed to the command line.

```
selection = datasets[0]
print(selection)
```

You can load a dataset as a dataframe.

```
selection.download_csv()
df = selection.load_as_df()
```