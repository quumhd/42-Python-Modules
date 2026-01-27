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
        self.set_name(name)
        self.set_water(water)
        self.set_sunlight(sunlight)

    def set_name(self, name: str) -> None:
        if name is None or name == "":
            raise NameError("Name cannot be empty")
        else:
            self.name = name

    def set_water(self, water: int) -> None:
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

    def get_water(self) -> int:
        """returns the amount of water the plant has"""
        return self.water

    def get_sunlight(self) -> int:
        """returns the amount of sunlight the plant gets"""
        return self.sunlight


class GardenManager:
    """GardenManager that raises errors, when something went wrong"""
    def __init__(self, manager_name: str) -> None:
        self.manager_name = manager_name
        self.garden = {}

    def add_plant(self, name: str, water: int, sunlight: int) -> None:
        new_plant = Plant(name, water, sunlight)
        self.garden[name] = new_plant
        print(f"{name} has been added to {self.manager_name}'s garden")

    def water_plants(self, amount: int) -> None:
        try:
            print("Opening watering systems")
            for plant in self.garden:
                self.garden[plant].set_water(self.garden[plant].get_water()
                                             + amount)
                print(f"Watering {self.garden[plant].get_name()} - sucess")
        finally:
            print("Closing watering systems (cleanup)")

    def check_plant_health(self, name: str) -> None:
        if name not in self.garden:
            raise GardenError(f"{name} does not exist in this garden")
        else:
            water = self.garden[name].get_water()
            if water < 1:
                raise WaterError(f"Plants need at least 1l of water: {water}l")
            elif water > 10:
                raise WaterError(f"Plant can only handel up to 10l: {water}l")
            sunlight = self.garden[name].get_sunlight()
            if sunlight < 2:
                raise SunError(f"Plants need at least 2h of"
                               f"sunlight: {sunlight}h")
            elif sunlight > 12:
                raise SunError(f"Plants dry out with more that 12h of"
                               f"sunlight: {sunlight}")
        print(f"{name}: healthy (water: {water}, sun: {sunlight})")


def test_plant_checks() -> None:
    alice = GardenManager("alice")
    print()
    print("Adding plants to garden:")
    try:
        alice.add_plant("tulip", 6, 4)
    except NameError as error:
        print(f"NameError: {error}")
    except WaterError as error:
        print(f"WaterError: {error}")
    except SunError as error:
        print(f"SunError: {error}")
    try:
        alice.add_plant(None, 8, 6)
    except NameError as error:
        print(f"NameError: {error}")
    except WaterError as error:
        print(f"WaterError: {error}")
    except SunError as error:
        print(f"SunError: {error}")
    try:
        alice.add_plant("carrot", 9, 4)
    except NameError as error:
        print(f"NameError: {error}")
    except WaterError as error:
        print(f"WaterError: {error}")
    except SunError as error:
        print(f"SunError: {error}")
    print()
    print("Watering Plants:")
    try:
        alice.water_plants(4)
    except WaterError as error:
        print(f"WaterError: {error}")
    print()
    print("Checking plant health:")
    try:
        alice.check_plant_health("tulip")
    except WaterError as error:
        print(f"WaterError: {error}")
    except NameError as error:
        print(f"NameError: {error}")
    except GardenError as error:
        print(f"GardenError: {error}")
    try:
        alice.check_plant_health("carrot")
    except WaterError as error:
        print(f"WaterError: {error}")
    except NameError as error:
        print(f"NameError: {error}")
    except GardenError as error:
        print(f"GardenError: {error}")
    print()
    print("All error raising tests complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_plant_checks()
