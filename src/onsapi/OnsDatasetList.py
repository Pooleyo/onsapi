from pydantic import BaseModel
from typing import List
from . import OnsDataset

class OnsDatasetList(BaseModel):
    #@context
    count: int
    limit: int
    offset: int
    total_count: int
    items: List[OnsDataset]
    
    def __str__(self):
        # Pretty print implementation
        return (
            f"OnsDatasetList:\n"
            f"  Count: {self.count}\t\t\n"
            f"  Limit: {self.limit}\t\t\n"
            f"  Offset: {self.offset}\t\t\n"
            f"  Total count: {self.total_count}\t\t\n"
            f"  Items: {len(self.items)} datasets\t\t\n"
        )