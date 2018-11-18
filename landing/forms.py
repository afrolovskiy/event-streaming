from django import forms


class OrderForm(forms.Form):
    SINGLE_CAMERA = '1 camera'
    TWO_CAMERAS = '2 cameras'
    THREE_CAMERAS = '3 cameras'
    SIGNLE_COMMENTATOR = '1 commentator'
    TWO_COMMENTATORS = '2 commentators'
    THREE_COMMENTATORS = '3 commentators'
    OUR_INTERNET = 'our internet'
    OPTIONS = (
        (SINGLE_CAMERA, 'Съемка в 1 камеру'),
        (TWO_CAMERAS, 'Съемка в 2 камеры'),
        (THREE_CAMERAS, 'Съемка в 3 камеры'),
        (SIGNLE_COMMENTATOR, '1 комментатор'),
        (TWO_COMMENTATORS, '2 комментатора'),
        (THREE_COMMENTATORS, '3 комментатора'),
        (OUR_INTERNET, 'Наш интернет'),
    )

    event = forms.CharField(max_length=255, label='Мероприятие')
    place = forms.CharField(max_length=255, label='Местро проведения')
    date = forms.DateField(label='Дата проведения')
    name = forms.CharField(max_length=255, label='Как к Вам обращаться')
    phone = forms.CharField(max_length=64, label='Контактный телефон')
    email = forms.CharField(max_length=255, label='Электронная почта')
    options = forms.MultipleChoiceField(choices=OPTIONS, label='Необходимо')
    comments = forms.CharField(max_length=512, label='Комментарии',
                               required=False)

    def send_email(self):
        pass
