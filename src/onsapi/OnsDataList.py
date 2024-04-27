from pydantic import BaseModel


class OnsDataList(BaseModel):
    datasets: list

    def __str__(self):
        return ''.join(f"  Title: {dataset.title}\n" for dataset in self.datasets)
