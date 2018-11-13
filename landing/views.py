from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from landing.forms import OrderForm


class IndexView(TemplateView):
    template_name = 'index.html'


class OrderView(FormView):
    template_name = 'order.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('landing:index')
