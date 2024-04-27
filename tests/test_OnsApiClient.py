from onsapi import OnsApiClient, OnsDataset, OnsDataList


class TestOnsApiClient:
    
    def setup_method(self, method):
        self.client = OnsApiClient()

    def test_list_datasets(self):
        # Tests if a list of OnsDataset is returned
        datasets = self.client.list_datasets(limit=1000)
        
        # Assert that datasets is not None
        assert datasets is not None, "Expected datasets to be OnsDataList, got None"
        
        # Assert that datasets is a OnsDataList
        assert isinstance(datasets, OnsDataList), "Expected datasets to be OnsDataList"

        # Assert that datasets.datasets is a list
        assert isinstance(datasets.datasets, list), "Expected datasets.datasets to be a list"
        
        # Optionally, if you want to check that the list is not empty
        assert len(datasets.datasets) > 0, "Expected datasets.datasets to be non-empty"
        
        # Assert that each item in datasets is an instance of OnsDataset
        # This assumes you have a way to verify an item is an OnsDataset, like isinstance or checking a specific attribute
        for dataset in datasets.datasets:
            assert isinstance(dataset, OnsDataset), f"Expected each dataset to be an instance of OnsDataset, got {type(dataset)}"
