from dataclasses import dataclass, field


@dataclass
class ChartDTO:
    panel_id: str = ''
    area: str = ''
    name: str = ''
    scale: str = ''
    polygon: [] =  field(default_factory=list)





