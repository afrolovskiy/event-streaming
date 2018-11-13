from django import forms


class OrderForm(forms.Form):
    SINGLE_CAMERA = '1 camera'
    TWO_CAMERAS = '2 cameras'
    THREE_CAMERAS = '3 cameras'
    SIGNLE_COMMENTATOR = '1 commentator'
    TWO_COMMENTATORS = '2 commentators'
    THREE_COMMENTATORS = '3 commentators'
    OUR_INTERNET = 'our internet'
    OPTIONS = ((x, x) for x in (
        SINGLE_CAMERA,
        TWO_CAMERAS,
        THREE_CAMERAS,
        SIGNLE_COMMENTATOR,
        TWO_COMMENTATORS,
        THREE_COMMENTATORS,
        OUR_INTERNET,
    ))

    event = forms.CharField(max_length=255)
    place = forms.CharField(max_length=255)
    date = forms.DateField()
    name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=64)
    email = forms.CharField(max_length=255)
    options = forms.MultipleChoiceField(choices=())
    comments = forms.CharField(max_length=512)

    def send_email(self):
        pass
