from pricecheck.models import *
import latidude99.settings as settings
import pytz
from pricecheck.text import *
from pricecheck.models import *
from pricecheck.dto import *
import datetime as dt

def convert_product_db2dto(db):
    dto = ProductDTO()
    dto.username = db.user.name
    dto.email = db.user.email
    dto.product_count =  db.user.product_set.filter(tracked=True).count()
    dto.url = db.url
    dto.start_date = db.start_date
    dto.end_date = db.end_date
    dto.duration = str(db.duration) + 'day(s)'
    timedelta = db.end_date - dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
    dto.duration_left = str(timedelta.days)
    dto.voucher_code = ''
    dto.name = db.name
    dto.initial_price = db.initial_price

    prices = db.price_set.all()
    price_currencies = [x.currency for x in prices]
    price_labels = [x.date.strftime('%d %b %Y, %H:%M') for x in prices]
    price_values = [x.price for x in prices]
    labels_filler = ['waiting'] * (timedelta.days * 3)
    values_filler = [0] * (timedelta.days * 3)
    dto.price_labels = price_labels + labels_filler
    dto.price_values = price_values + values_filler

    dto.initial_price = price_values[0]
    if len(dto.price_values) > 1:
        dto.previous_price = price_values[-2]
    else:
        dto.previous_price = price_values[-1]
    dto.current_price = price_values[-1]
    price_diff = db.initial_price - dto.current_price

    dto.price = dto.current_price
    dto.currency = price_currencies[-1]
#    dto.status = db.status
    dto.track_code = db.track_code
    dto.stop_code = db.stop_code
    dto.threshold_up = db.threshold_up
    dto.threshold_down = db.threshold_down
    dto.error = ''
    dto.error1 = ''
    dto.error2 = ''
    dto.error3 = ''
    return dto
















