from django import forms
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class OrderForm(forms.Form):
    SINGLE_CAMERA = '1 camera'
    TWO_CAMERAS = '2 cameras'
    THREE_CAMERAS = '3 cameras'
    SIGNLE_COMMENTATOR = '1 commentator'
    TWO_COMMENTATORS = '2 commentators'
    OUR_INTERNET = 'our internet'
    EDITING = 'editing'
    OPTIONS = (
        (SINGLE_CAMERA, 'Съемка в 1 камеру'),
        (TWO_CAMERAS, 'Съемка в 2 камеры'),
        (THREE_CAMERAS, 'Съемка в 3 камеры'),
        (SIGNLE_COMMENTATOR, '1 комментатор'),
        (TWO_COMMENTATORS, '2 комментатора'),
        (OUR_INTERNET, 'Наш интернет'),
        (EDITING, 'Монтаж'),
    )

    event = forms.CharField(max_length=255, label='Мероприятие')
    place = forms.CharField(max_length=255, label='Место проведения')
    date = forms.DateField(label='Дата проведения', input_formats=['%d/%m/%Y'])
    name = forms.CharField(max_length=255, label='Как к Вам обращаться')
    phone = forms.CharField(max_length=64, label='Контактный телефон')
    email = forms.CharField(max_length=255, label='Электронная почта')
    options = forms.MultipleChoiceField(choices=OPTIONS, label='Необходимо')
    comments = forms.CharField(max_length=512, label='Комментарии',
                               required=False)

    def send_email(self):
        subject = 'Новая заявка на онлайн трансляцию'
        option_names = dict(self.OPTIONS)
        options = [option_names[opt] for opt in self.cleaned_data['options']]
        context = {
            'event': self.cleaned_data['event'],
            'place': self.cleaned_data['place'],
            'date': self.cleaned_data['date'],
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
            'options': ','.join(options),
            'comments': self.cleaned_data['comments'],
        }
        msg_text = render_to_string('emails/order.txt', context)
        msg_html = render_to_string('emails/order.html', context)
        msg = EmailMultiAlternatives(
            subject, msg_text,
            to=settings.NOTIFIED_EMAILS,
            reply_to=[self.cleaned_data['email']],
        )
        msg.attach_alternative(msg_html, "text/html")
        msg.send()
        pass
