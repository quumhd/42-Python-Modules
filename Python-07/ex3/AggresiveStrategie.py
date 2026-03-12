
from ex3.GameStrategy import GameStrategie


class AggressiveStrategie(GameStrategie):
    """proratieses many cards on field and attacking"""
    def executing_turn(self, hand: list, battlefield: list) -> dict:
        """exetures a turn"""
        pass

    def get_strategy(self) -> str:
        """returns the strategie name"""
        return "AgressiveStrategie"

    def prioritize_targets(self, availible_targets: list) -> list:
        """return a list with the prioritised targets sorted in the list"""
        pass
