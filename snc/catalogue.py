from dataclasses import dataclass, field


@dataclass
class CatalogueDTO:
    file_identifier: str = ''
    organisation_name: str = ''
    fax: str = ''
    phone: str = ''
    delivery_point: str = ''
    city: str = ''
    administrative_area: str = ''
    postal_code: str = ''
    country: str = ''
    email: str = ''
    date: str = ''
    charts: [] = field(default_factory=list)
    charts_count: int = ''





