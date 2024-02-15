from onsapi import OnsApiClient, OnsDataset

class TestOnsApiClient:
    
    def setup_method(self, method):
        self.client = OnsApiClient()

    def test_list_datasets(self):
        # Tests if a list of OnsDataset is returned
        datasets = self.client.list_datasets(limit=1000)
        
        # Assert that datasets is not None
        assert datasets is not None, "Expected datasets to be a list, got None"
        
        # Assert that datasets is a list
        assert isinstance(datasets, list), "Expected datasets to be a list"
        
        # Optionally, if you want to check that the list is not empty
        assert len(datasets) > 0, "Expected datasets list to be non-empty"
        
        # Assert that each item in datasets is an instance of OnsDataset
        # This assumes you have a way to verify an item is an OnsDataset, like isinstance or checking a specific attribute
        for dataset in datasets:
            assert isinstance(dataset, OnsDataset), f"Expected each dataset to be an instance of OnsDataset, got {type(dataset)}"

