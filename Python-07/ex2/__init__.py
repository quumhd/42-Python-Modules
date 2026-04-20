
__version__ = "1.0.0"
__author__ = "jdreissi"

from .strategies import DefensiveStrategy
from .strategies import BattleStrategy, NormalStrategy, AggressiveStrategy

__all__ = [
    "BattleStrategy",
    "NormalStrategy",
    "AggressiveStrategy",
    "DefensiveStrategy"
    ]
