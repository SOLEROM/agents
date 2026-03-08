"""
Data models for _example module.

Replace with your actual models.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ExampleModel:
    """Example data model."""

    id: str
    name: str
    status: str = "active"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
