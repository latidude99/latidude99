from dataclasses import dataclass, field


@dataclass
class ChartDTO:
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






