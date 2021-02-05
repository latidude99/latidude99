from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import latidude99.settings as settings

def send_email(product_dto, sub, templ):
    context = {'product_dto': product_dto,
               'url': product_dto.url,
               'name': product_dto.name,
               'username': product_dto.username,
               'email': product_dto.email,
               'product_count': product_dto.product_count,
               'duration': product_dto.duration,
               'duration_left': product_dto.duration_left,
               'start_date': product_dto.start_date,
               'end_date': product_dto.end_date,
               'voucher_code': product_dto.voucher_code,
               'initial_price': product_dto.initial_price,
               'current_price': product_dto.current_price,
               'currency': product_dto.currency,
               'status': product_dto.status,
               'track_code': product_dto.track_code,
               'stop_code': product_dto.stop_code,
               'threshold_up': product_dto.threshold_up,
               'threshold_down': product_dto.threshold_down,
               'error': product_dto.error,
               'error2': product_dto.error2,
               'error3': product_dto.error3,
               }
    subject = sub
    template = templ
    sender = settings.EMAIL_HOST_USER
    receiver = product_dto.email
    send(subject, template, context, sender, receiver)
    print('pricecheck email sent to ' + product_dto.email)


def send(subject, template, context, sender, receiver):
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    from_email = 'From <' + sender + '>'
    print('just before sending')
    mail.send_mail(subject, plain_message, from_email, [receiver], html_message=html_message, fail_silently=False)