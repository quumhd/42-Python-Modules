#!/usr/bin/env python3

class Plant:
    """defines the Plant class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialise parameters"""
        self.__name = name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """checks that height cannot be negative"""
        if height >= 0:
            self.__height = height
        else:
            print("\033[31m[KO]\033[0m Height cannot be a negative:", height)

    def set_age(self, age: int) -> None:
        """checks that age cannot be negative"""
        if age >= 0:
            self.__age = age
        else:
            print("\033[31m[KO]\033[0m Age cannot be a negaive:", age)

    def get_name(self) -> None:
        """returns the name of the flower"""
        return self.__name

    def get_height(self) -> None:
        """returns the height of the flower"""
        return self.__height

    def get_age(self) -> None:
        """returns the age of the flower"""
        return self.__age

    def print_plant_info(self) -> None:
        print(f"{self.__name}: {self.__height} cm, {self.__age} days")


class FloweringPlant(Plant):
    """defines the FloweringPlant class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialise parameters"""
        super().__init__(name, age, height)


class PrizeFlower(Plant):
    """defines the PrizeFlower class"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialise parameters"""
        super().__init__(name, age, height)


class GardenManager:
    """class GardenManager"""
    all_gardens = []
    harvested = 0
    planted = 0
    growth = 0

    def __init__(self, manager_name: str) -> None:
        """initialise parameters"""
        self.manager_name = manager_name
        self.garden = {}
        self.stats = self.GardenStats(self)

    @classmethod
    def create_garden_network(cls, names: list["GardenManager"]) -> list["GardenManager"]:
        """creates a garden network of multiple managers"""
        for name in names:
            cls.all_gardens.append(name)
        return cls.all_gardens


    def add_garden(self, name: str) -> None:
        """adds gardens to the manager"""
        if name in self.garden:
            print(f"{self.get_name()} already exists")
        else:
            self.garden[name] = []

    def add_plant(self, name: str, plant: Plant) -> None:
        """adds plant to gardens"""
        if name in self.garden:
            self.garden[name].append(plant)
            GardenManager.planted += 1
            print(f"Added {plant.get_name()} to {name}")
        else:
            print(f"Garden {name} does not exist")

    def harvest_plant(self, name: str, to_harvest: Plant) -> None:
        """harvest a plant from a garden"""
        if name not in self.garden:
            print(f"Garden {name} does not exist")
        elif to_harvest not in self.garden[name]:
            print(f"{to_harvest.get_name()} does not exits in {name}")
        else:
            self.garden[name].remove(to_harvest)
            GardenManager.harvested += 1


    def grow_all_plants(self, name: str, amount: int) -> None:
        """grows all plants in the garden by amount"""
        if name in self.garden:
            print(f"{self.manager_name} helps all the plants in {name} to grow")
            for Plant in self.garden[name]:
                Plant.set_height(Plant.get_height() + amount)
                print("- ", end = "")
                print(f"{Plant.get_name()} grew {amount} cm")
                GardenManager.growth += amount
        else:
            print(f"Garden {name} does not exist")

    def age_all_plants(self, name: str, amount: int) -> None:
        """ages all plants in the garden by amount"""
        if name in self.garden:
            for Plant in self.garden[name]:
                Plant.set_age(Plant.get_age() + amount)
        else:
            print(f"{name} does not exist")

       
    class GardenStats:
        """Manages the statistics of the garden"""
        def __init__(self, manager: "GardenManager") -> None:
            self.manager = manager

        def get_planted_amount(self) -> None:
            """return the total amount of plants planted"""
            return GardenManager.planted
 
        def get_harvest_amount(self) -> None:
            """returns the amount of harvested plants in a garden"""
            return GardenManager.harvested

        def get_growth_amount(self) -> None:
            """returns the amount of growht that happent"""
            return GardenManager.growth

        def get_flowering_amount(self) -> None:
            """returns the amount of flowering plants in the garden"""
            flowering = 0
            for garden in self.manager.garden:
                for plant in self.manager.garden[garden]:
                    if isinstance(plant, FloweringPlant):
                        flowering += 1
            return flowering

        def get_prize_amount(self) -> None:
            """returns the amount of prize winning plants in the garden"""
            prize_winning = 0
            for garden in self.manager.garden:
                for plant in self.manager.garden[garden]:
                    if isinstance(plant, PrizeFlower):
                        prize_winning += 1
            return prize_winning

        def get_regular_amount(self) -> None:
            """returns the amount of regular plants in the garden"""
            regular = self.get_planted_amount() - self.get_flowering_amount()
            regular -= self.get_prize_amount()
            return regular

        def get_gardens_managed(self) -> None:
            """returns the total amount of gardens manages by the manager"""
            amount = 0
            for i in self.manager.garden:
                amount += 1
            return amount

        def get_garden_score(self) -> None:
            total_score = 0;
            total_score += self.get_gardens_managed() * 50
            total_score += self.get_regular_amount() * 10
            total_score += self.get_flowering_amount() * 25
            total_score += self.get_prize_amount() * 50
            return total_score

        def print_garden_information(self, name: str) -> None:
            """prints the information about a garden"""
            if name not in self.manager.garden:
                print(f"Garden {name} does not exist")
            else:
                print(f"=== {self.manager.manager_name}'s garden report about {name} ===")
                print("Plants in garden:")
                for Plant in self.manager.garden[name]:
                    print("- ", end = "")
                    Plant.print_plant_info()




if __name__ == "__main__":
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")
    alice.add_garden("Backyard")
    alice.add_garden("Garden2")
    bob.add_garden("balcony")
    manager = GardenManager.create_garden_network([alice, bob])
    oak_tree = Plant("Oak Tree", 112, 752)
    rose = FloweringPlant("Rose", 36, 63)
    tulip = PrizeFlower("Tulip", 24, 22)
    print("=== Garden Management System ===")
    alice.add_plant("Backyard", oak_tree)
    alice.add_plant("Backyard", rose)
    alice.add_plant("Backyard", tulip)
    # alice.harvest_plant("Backyard", oak_tree)
    print()
    alice.grow_all_plants("Backyard", 2)
    print()
    alice.stats.print_garden_information("Backyard")
    print()
    print(f"Plants added: {alice.stats.get_planted_amount()}")
    print(f"Plants harvested: {alice.stats.get_harvest_amount()}")
    print(f"Regular plants: {alice.stats.get_regular_amount()}")
    print(f"Flowering plants: {alice.stats.get_flowering_amount()}")
    print(f"Prize winning plants: {alice.stats.get_prize_amount()}")
    print()
    print("=== Utility functions ===")
    print(f"Garden Scores")
    print(f"Alice: {alice.stats.get_garden_score()}")
    print(f"Bob: {bob.stats.get_garden_score()}")
    print()
    print(f"Gardens Managed")
    print(f"Alice: {alice.stats.get_gardens_managed()}")
    print(f"Bob: {bob.stats.get_gardens_managed()}")
    print()
    print("All manager in the garden network:")
    for person in manager:
        print(person.manager_name)
    print()
    print("=== Error Tests ===")
    alice.add_plant("x", tulip)
    alice.harvest_plant("x", tulip)
    x = Plant("x", 1, 1)
    alice.harvest_plant("Backyard", x)
    alice.grow_all_plants("x", 2)
    alice.stats.print_garden_information("x")


