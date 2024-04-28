from pydantic import BaseModel
from typing import List

class OnsDataList(BaseModel):
    datasets: List

    def __getitem__(self, index):
        return self.datasets[index]

    def __len__(self):
        return len(self.datasets)

    def __iter__(self):
        return iter(self.datasets)

    def __str__(self):
        return ''.join(f"  Title: {dataset.title}\n" for dataset in self.datasets)

    def save_to_sqlite(self, file_path: str):
        for dataset in self.datasets:
            dataset.save_to_sqlite(file_path)
        print("Saved OnsDataList to SQLite database at:", file_path)

