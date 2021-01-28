from dataclasses import dataclass, field
import datetime as dt
import pytz

@dataclass
class ProductDTO:
    username: str = ''
    email: str = ''
    product_count: str = ''
    url: str = ''
    duration: int = 3
    duration_left: int = 0
    start_date: str = ''
    end_date: str = ''
    promocode: str = ''
    name: str = ''
    initial_price: str = ''
    current_price: str = ''
    prices_labels: str = ' '
    prices_values: float = 0.00
    price: int = 0
    currency: str = ''
    tracked: bool = True
    track_code: str = ''
    stop_code: str = ''
    threshold_up: str =''
    threshold_down: str = ''
    error: str = ''


