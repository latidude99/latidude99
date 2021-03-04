from dataclasses import dataclass, field


@dataclass
class PolygonDTO:
    positions: [] = field(default_factory=list)
    name: str =''





