from onsapi import OnsApiClient

client = OnsApiClient()
l = client.list_datasets()
l.save_to_sqlite('data_onsapi/ons_data_list.db')
