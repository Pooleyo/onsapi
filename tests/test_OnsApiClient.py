from onsapi import OnsApiClient

class TestOnsApiClient:
    
    def setup_method(self, method):
        self.client = OnsApiClient()

    def test_list_datasets(self):
        # Tests if an OnsDatasetList is returned
        datasets = self.client.list_datasets()
        assert datasets
