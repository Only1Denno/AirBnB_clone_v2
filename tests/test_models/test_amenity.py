#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Select the Amenities """

    def __init__(self, *args, **kwargs):
        """Collects Information Selected """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Creates New Name """
        new = self.value()
        self.assertEqual(type(new.name), str)
