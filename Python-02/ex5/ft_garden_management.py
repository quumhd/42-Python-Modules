#!/usr/bin/env python3

class GardenError(Exception):
    """base class for all garden related errors"""


class NameError(GardenError):
    """error for invalid plant names"""
    pass


class WaterError(GardenError):
    """error for bad water level"""
    pass


class SunError(GardenError):
    """error for bad sunlight hours"""
    pass


class Plant:
    """create new plants"""
    def __init__(self, name: str, water: int, sunlight: int) -> None:
        self.name = self.set_name(name)
        self.water = self.set_water(water)
        self.sunlight = self.set_sunlight(sunlight)

    def set_name(self, name: str) -> None:
        if name is None or name == "":
            raise NameError("Name cannot be empty")
        else:
            self.name = name

    def set_water(self, water: str) -> None:
        if water < 1:
            raise WaterError(f"Plants need at least 1l of water: {water}l")
        elif water > 10:
            raise WaterError(f"Plant can only handel up to 10l: {water}l")
        else:
            self.water = water

    def set_sunlight(self, sunlight: int) -> None:
        if sunlight < 2:
            raise SunError(f"Plants need at least 2h of sunlight: {sunlight}h")
        elif sunlight > 12:
            raise SunError(f"Plants dry out with more that 12h of"
                           f"sunlight: {sunlight}")
        else:
            self.sunlight = sunlight

    def get_name(self) -> str:
        """returns the name of the plant"""
        return self.name


class GardenManager:
    """GardenManager that raises errors, when something went wrong"""
    def __init__(self, manager_name: str) -> None:
        self.manager_name = manager_name
        self.garden = {}

    def add_plant(self, name: str, water: int, sunlight: int) -> None:
        new_plant = Plant(name, water, sunlight)
        self.garden[name] = new_plant
        print(f"{name} has been added to {self.manager_name}'s garden")

    def water_plants(self) -> None:
        try:
            print("Watering plants")
            for plant in self.garden:
                print(f"Watering {plant.name} - sucess")
                plant.water += 2
        finally:
            print("Closing watering systems (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.garden:
            print(self.garden)
            raise GardenError(f"{name} does not exist in this garden")
        else:
            print("in garden")


def test_plant_checks() -> None:
    alice = GardenManager("alice")
    print("Adding plants to garden:")
    try:
        alice.add_plant("tulip", 6, 4)
        alice.add_plant("cactus", 9, 3)
        alice.add_plant(None, 8, 6)
    except NameError as error:
        print(f"NameError: {error}")
    except WaterError as error:
        print(f"WaterError: {error}")
    except SunError as error:
        print(f"SunError: {error}")
    try:
        alice.check_plant_health("tulip")
    except WaterError as error:
        print(f"WaterError: {error}")
    except NameError as error:
        print(f"NameError: {error}")
    except GardenError as error:
        print(f"GardenError: {error}")


if __name__ == "__main__":
    test_plant_checks()
