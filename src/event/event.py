from dataclasses import dataclass
from .event_type import EventType
from typing import Any

@dataclass
class Event:
    type: EventType
    data: dict
    source: Any = None
    delete_after_proccesing: bool = True
