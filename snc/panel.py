from dataclasses import dataclass, field


@dataclass
class PanelDTO:
    # directly from DB
    panel_id: str = ''
    area: str = ''
    name: str = ''
    scale: str = ''
    polygons: [] = field(default_factory=list)
    # calculated
    panel_centre: str = ''
    label_position: str = ''
    colour: str = ''




