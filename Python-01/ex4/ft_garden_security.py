#!/usr/bin/env python3

class SecurePlant:
    """a secure plats that checks and protects its data"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """initialise class parameters"""
        self.name = name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)
        print("Plant created: {self.name}")

    def set_height(self, height: int) -> None:
        if height >= 0:
            self.height = height
        else:
            print("\033[31m[KO]\033[0m Height cannot be a negative:", height)

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.age = age
        else:
            print("\033[31m[KO]\033[0m Age cannot be a negative:", age)

    def get_info(self) -> None:
        """prints the parameters"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 30)

    rose.get_info()
    rose.set_height(35)
    rose.set_age(21)
    print("updated: Rose")
    rose.get_info()
    rose.set_height(-5)
    rose.set_age(-1)
    rose.get_info()
