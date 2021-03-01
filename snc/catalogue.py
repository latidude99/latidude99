from dataclasses import dataclass, field


@dataclass
class CatalogueDTO:
    file_identifier: str = ''
    organisation_name: str = ''
    fax: str = ''
    phone: str = ''
    deliveryPoint: str = ''
    city: str = ''
    administrative_area: str = ''
    postal_code: str = ''
    country: str = ''
    email: str = ''
    date: str = ''
    charts: [] = field(default_factory=list)






