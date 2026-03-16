#!/usr/bin/env python3


from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, Field


class SpaceStation(BaseModel):
    """validates fields and inherits from BaseModel"""
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=0, le=100)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def space_station() -> None:
    """print the space_station information"""
    print("Space Station Validation Data")
    print("========================================")
    try:
        iss = SpaceStation(
                station_id="ISS001",
                name="International Space Station",
                crew_size=6,
                power_level=88.2,
                oxygen_level=95.3,
                last_maintenance="2023-10-01T10:00:00",
                is_operational=True,
                notes="test_nodes"
                )
        print("Valid station created:")
        print(f"ID: {iss.station_id}")
        print(f"Name: {iss.name}")
        print(f"Crew: {iss.crew_size} people")
        print(f"Power: {iss.power_level}%")
        print(f"Oxygen: {iss.oxygen_level}%")
        if iss.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: Not Operational")
    except ValidationError as e:
        print("Validation error creating space station")
        print(e)
    print("========================================")

if __name__ == "__main__":
    space_station()
