from dataclasses import dataclass, field


@dataclass
class PanelDTO:
    panel_id: str = ''
    area: str = ''
    name: str = ''
    scale: str = ''
    polygons: [] =  field(default_factory=list)





