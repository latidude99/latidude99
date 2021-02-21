from dataclasses import dataclass


@dataclass
class ProductDTO:
    username: str = ''
    email: str = ''
    product_count: str = '' # active
    total_product_count: str = '' # total
    url: str = ''
    duration: int = 0
    duration_left: int = 0
    start_date: str = ''
    end_date: str = ''
    voucher_code: str = ''
    name: str = ''
    initial_price: str = ''
    previous_price: str = ''
    current_price: str = ''
    price_diff: float = 0
    price_labels: str = ' '
    price_values: float = 0.00
    price: int = 0
    currency: str = ''
    status: str = ''
    app_link: str = ''
    track_code: str = ''
    track_link: str = ''
    stop_code: str = ''
    stop_link: str = ''
    confirm_code: str = ''
    confirm_link: str = ''
    confirmed: str = ''
    threshold_up: str =''
    threshold_down: str = ''
    code = ''
    error: str = ''
    error1: str = ''
    error2: str = ''
    error3: str = ''




