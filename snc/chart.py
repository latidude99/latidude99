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
    notices: [] = field(default_factory=list)
    polygon: [] =  field(default_factory=list)
    panel: [] =  field(default_factory=list)
    import_date: str = ''





