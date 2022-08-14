from dataclasses import dataclass


@dataclass
class Job:
    title: str
    url: str
    description: str
    other: str
