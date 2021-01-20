from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    url: str
    checks: int
