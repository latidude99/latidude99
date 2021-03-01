from dataclasses import dataclass, field


@dataclass
class ChartDTO:
    number: str = ''
    title: str = ''
    scale: str = ''
    folio: str = ''
    cat_number: str = ''
    int_number: str = ''
    status: str = ''
    status_date: str = ''
    new_edition_date: str = ''
    import_date: str = ''
    polygons: [] =  field(default_factory=list)
    panels: [] =  field(default_factory=list)
    notices: [] = field(default_factory=list)





