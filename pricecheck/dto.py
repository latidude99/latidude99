from dataclasses import dataclass
import datetime as dt
import pytz

@dataclass
class ProductDTO:
    username: str = ''
    email: str = ''
    url: str = ''
    duration: int = 3
    start_date: str = ''
    end_date: str = ''
    promocode: str = ''
    name: str = ''
    price: int = 0
    currency: str = ''
    tracked: bool = True
    track_code: str = ''
    stop_code: str = ''


