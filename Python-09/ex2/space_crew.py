#!/usr/bin/env python3

from enum import Enum
from typing import Any
from datetime import datetime
try:
    from pydantic import BaseModel, ValidationError, Field, model_validator
except ImportError:
    print("Pydantic missing: pip install pydantic")
    exit(1)


class Rank(Enum):
    """defines the crew ranks"""
    CADET = "cadet"
    OFFICER = 'officer'
    LIEUTENANT = "lieuteneant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """defines a CrewMember model"""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """defines the SpaceMission Model"""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_id(self) -> Any:
        """checks if the mission if starts with an M"""
        if not self.mission_name.startswith("M"):
            raise ValueError("Mission name has to start with an M")

        """checks if least 50% of the crew is experienced on a long mission"""
        if self.duration_days > 365:
            crew_size = len(self.crew)
            experienced_member = 0
            for member in self.crew:
                if member.years_experience > 4:
                    experienced_member += 1
            if crew_size / 2 > experienced_member:
                raise ValueError("Long mission need a 50% experienced crew")

        """checks if every member of the crew is active"""
        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All members of the crew must be active")

        """checks if the crew an an Commander or Captain"""
        if self.crew is None:
            return
        has_leader = False
        for member in self.crew:
            if member.rank == Rank.CAPTAIN or member.rank == Rank.COMMANDER:
                has_leader = True
        if has_leader is False:
            raise ValueError(
                "Crew must have at least one captain or commander"
                )

        return self


def space_crew() -> None:
    """demonstrates the members and missions"""
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        crew = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=42,
                specialization="Mission Command",
                years_experience=12,
                is_active=True,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=6,
                is_active=True,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=30,
                specialization="Engineering",
                years_experience=5,
                is_active=True,
            ),
        ]
    except ValidationError as e:
        print("Failed to create crew members:")
        print(e)
        print("=========================================")
        return

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 7, 1),
            duration_days=900,
            crew=crew,
            mission_status="planned",
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print("Mission validation failed:")
        print(e)
        print("=========================================")
        return
    except ValueError as e:
        print("Mission validation failed:")
        print(e)
        print("=========================================")
        return

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")
    print("=========================================")


if __name__ == "__main__":
    space_crew()
