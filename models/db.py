from models.models import Sheep
from typing import Dict, List


class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:  # take in new sheep data as parameter
        if sheep.id in self.data:
            raise ValueError('Sheep already exists with this ID')

        self.data[sheep.id] = sheep
        return sheep

    def delete_sheep(self, id: int):
        # input sheep id
        # find sheep with id in database
        # remove entry
        # return status code
        if id in self.data:
            del self.data[id]
        else:
            raise KeyError('sheep with id not found')

    def update_sheep(self, sheep: Sheep) -> Sheep:
        # input new sheep
        # find sheep in db
        # update found sheep with new information
        # return new
        if sheep.id in self.data:
            self.data[sheep.id] = sheep
            return sheep
        else:
            raise KeyError('sheep with id not found')

    def read_all_sheep(self) -> List:
        # return list of the dict
        return list(self.data.values())


db = FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram"),
    3: Sheep(id=3, name="Deedee", breed="Jacobs Four Horns", sex="ram"),
    4: Sheep(id=4, name="Rommy", breed="Romney", sex="ewe"),
    5: Sheep(id=5, name="Vala", breed="Valais Blacknose", sex="ewe"),
    6: Sheep(id=6, name="Esther", breed="Border Leicester", sex="ewe")
}
