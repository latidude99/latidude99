from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send(subject, template, context, sender, receiver):
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    from_email = 'From <' + sender + '>'
    print('just before sending')
    mail.send_mail(subject, plain_message, from_email, [receiver], html_message=html_message, fail_silently=False)