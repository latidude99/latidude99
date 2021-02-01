from dataclasses import dataclass, field
import datetime as dt
import pytz

@dataclass
class ProductDTO:
    username: str = ''
    email: str = ''
    product_count: str = '' # active
    total_product_count: str = '' # total
    url: str = ''
    duration: int = 3
    duration_left: int = 0
    start_date: str = ''
    end_date: str = ''
    voucher_code: str = ''
    name: str = ''
    initial_price: str = ''
    current_price: str = ''
    price_labels: str = ' '
    price_values: float = 0.00
    price: int = 0
    currency: str = ''
    status: str = ''
    track_code: str = ''
    stop_code: str = ''
    threshold_up: str =''
    threshold_down: str = ''
    code = ''
    error: str = ''
    error1: str = ''
    error2: str = ''
    error3: str = ''




