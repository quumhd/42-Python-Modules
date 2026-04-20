#!/usr/bin/env python3


from enum import Enum
from datetime import datetime
try:
    from pydantic import BaseModel, ValidationError, Field, model_validator
except ImportError:
    print("Pydantic missing: pip install pydantic")
    exit(1)


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, min_length=0,
                                         max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact types must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError(
                "Telepathic contact type needs at least 3 witnesses"
                )

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals need a received message")

        return self


def alient_contact():
    """demonstrates the AlienContact class"""
    print("Alient Contact Log Validation")
    print("======================================")
    try:
        contact_1 = AlienContact(
                contact_id="AC_2024_001",
                timestamp="2023-10-01T10:00:00",
                location="Area 51, Nevada",
                contact_type=ContactType.RADIO,
                signal_strength=5.5,
                duration_minutes=45,
                witness_count=5,
                message_received="test",
                is_verified=True
                )
        print("Valid contact report:")
        print(f"ID: {contact_1.contact_id}")
        print(f"Type: {contact_1.contact_type.value}")
        print(f"Location: {contact_1.location}")
        print(f"Signal: {contact_1.signal_strength}/10")
        print(f"Duration: {contact_1.duration_minutes} minutes")
        print(f"Witnesses: {contact_1.witness_count}")
        print(f"Message: {contact_1.message_received}")
    except (ValidationError, TypeError) as e:
        print("Alien Contact has false information")
        print(e)
    print("======================================")
    print("Expected Validation Error")
    try:
        contact_1 = AlienContact(
                contact_id="AC_2024_001",
                timestamp="2023-10-01T10:00:00",
                location="Area 51, Nevada",
                contact_type=ContactType.TELEPATHIC,
                signal_strength=5.5,
                duration_minutes=45,
                witness_count=1,
                message_received="test",
                is_verified=True
                )
        print("Valid contact report:")
        print(f"ID: {contact_1.contact_id}")
        print(f"Type: {contact_1.contact_type.value}")
        print(f"Location: {contact_1.location}")
        print(f"Signal: {contact_1.signal_strength}/10")
        print(f"Duration: {contact_1.duration_minutes} minutes")
        print(f"Witnesses: {contact_1.witness_count}")
        print(f"Message: {contact_1.message_received}")
    except (ValidationError, TypeError) as e:
        print("Alien Contact has false information")
        print(e)


if __name__ == "__main__":
    alient_contact()
