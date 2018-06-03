import random

from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import UpdateView

from .models import SeedFortune


def result(request):
    """
    Show the results of the fortune cookie.
    :param request:
    :return:
    """

    fortunes = SeedFortune.objects.all()
    fortune = fortunes[random.randrange(0, len(fortunes))]
    template = loader.get_template('pages/result.html')
    context = {
        'fortune': fortune
    }

    return HttpResponse(template.render(context, request))


class FortuneUpdate(UpdateView):
    model = SeedFortune
    fields = ['description']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse("home")
