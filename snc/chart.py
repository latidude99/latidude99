from dataclasses import dataclass, field


@dataclass
class ChartDTO:
    # directly from DB
    catalogue_id: str = ''
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
    polygons: [] = field(default_factory=list)
    panels: [] = field(default_factory=list)
    notices: [] = field(default_factory=list)
    last_nm_number: str = ''
    last_nm_date: str = ''
    # calculated
    max_scale_category: str = ''
    zoom_min: str = ''
    zoom_max: str = ''
    chart_centre: str = ''
    label_position: str = ''
    colour: str = ''



