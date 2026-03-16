#!/usr/bin/env python3


from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ValidationError, Field, model_validator


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """AlientContact BaseModel"""
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=100.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str = Field(default=None, min_length=0, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def custom_rules(self) -> None:
        if not self.contact_id.startswith("AC"):
            raise ValidationError("Contact ID does not start with \"AC\"")

        if self.contact_type == ContactType.PHYSICAL:
            if self.is_verified is False:
                raise TypeError("Physical contact types must be verified")

        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise TypeError(
                        "Telepathic contact type need at least 3 witnesses"
                        )

        if self.signal_strength > 7.0:
            if self.messages_received is None:
                raise TypeError("Strong Signals need a received message")


def alient_contact():
    """demonstrates the AlienContact class"""
    print("Alient Contact Log Validation")
    print("======================================")
    try:
        contact_1 = AlienContact(
                contact_id = "AC_2024_001",
                timestamp = "2023-10-01T10:00:00",
                location = "Area 51, Nevada",
                contact_type = ContactType.RADIO,
                signal_strength = 5.5,
                duration_minutes = 45,
                witness_count = 5,
                message_received = "test",
                is_verified = True
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


if __name__ == "__main__":
    alient_contact()
